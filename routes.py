#Thank god, we be in python
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from models import db, User, Score
from forms import SignUpForm, LoginForm, PicScoreForm

#Got to get that app.
app = Flask(__name__)

#Connection String
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///learningflask'
db.init_app(app) #Initialize app
#Need to generate forms with secure items. Again this is a demo for learning. otherwise certain items would have been .gitignore d.

app.secret_key = "development-key"

#Setup route for the index
@app.route("/") #Define Route
def index():
    return render_template("index.html")
#Setup the route for about
@app.route("/about")
def about():
    return render_template("about.html")

#Running into trouble.
@app.route("/picscore",methods=['GET','POST'])
def picscore():
    form = PicScoreForm()
    finalScores = []
    otherScores = []
    #need 10 different instances of the score object.
    for j in range(10):
        idxScore = "score0" + str(j)
        otherScores.append(form[idxScore])
    i = 0
    myNumbers = "Start:"
    if request.method =="POST":
        if form.validate() == False:

            newScoreEmail = "utkeitarol@gmail.com"
            i = 0
            for i in range(10):
                if(i < 10):
                    #newScoreEmail = otherScores[i]
                    currentImageName = "image00"+ str(i)+".png"
                    currentScore = Score(newScoreEmail, currentImageName, otherScores[i].data)
                    #db.session.add(currentScore)
                #elif(i<100):
                #    finalScore.append(Score(newScoreEmail, "image0"+i+".png", form.scoreArray[i].data))
            for z in range(10):
                myNumbers += str(otherScores[z].data) + " "
            #return myNumbers + " Check it"
            return jsonify(otherScores)
    elif request.method =="GET":
        return render_template('picscore.html', form=form, i=0,j='0',numbers=myNumbers,scores = otherScores)
#Pic Score 3... Lets see
@app.route("/picscore3",methods=['GET','POST'])
def radialScore():
    #need 10 different instances of the score object.
    i = 0
    j = 0
    myNumbers = "Start:"
    options = []
    myOptions = {}

    if request.method =="POST":
        newScoreEmail = "utkeitarol@gmail.com"
        i = 0
        myOptions['email'] = newScoreEmail
        for z in range(10):
            currentScore = "score" + str(z)
            picture = "img" + str(z)
            options.append(request.form[currentScore])
            myOptions[picture] = request.form[currentScore]

            #Adding this for database addition.
            newScore = Score(str(myOptions['email']), str(picture),int(request.form[currentScore]))
            db.session.add(newScore)
            db.session.commit()
            #this should do it.
            
        options.append(newScoreEmail)
        #return myNumbers + " Check it"
        return jsonify(myOptions)
    elif request.method =="GET":
        return render_template('picscore3.html', i=0,j='0')
#Homepage
@app.route("/home")
def home():
    return render_template("home.html")
#Setup the route for SignUp
@app.route("/signup", methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if request.method =="POST":
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            newuser = User(form.first_name.data,form.last_name.data, form.email.data, form.password.data)
            db.session.add(newuser)
            db.session.commit()
            #Adding for sessions. This tells you that the email portion of the post data is being used.
            session['email'] = newuser.email #Using for models.py, has constructor. This is a parameter of the objectself.
            #This is where the user is added to the session.
            db.session.add(newuser)
            db.session.commit()

            #return "You've been Successfully Signed up!"
            return redirect(url_for('home'))

    elif request.method =="GET":
        return render_template('signup.html', form=form)
#This is the end.
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
