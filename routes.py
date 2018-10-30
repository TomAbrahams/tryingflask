#Thank god, we be in python
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from models import db, User, Score
from forms import SignUpForm, LoginForm, PicScoreForm
from cliArrayThread import frontendSide
from getTheCSV import makeCSV
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


#Pic Score 3... Lets see
@app.route("/picscore3",methods=['GET','POST'])
def picscore3():
    #need 10 different instances of the score object.
    i = 0
    j = 0
    myNumbers = "Start:"
    options = []
    myOptions = {}

    if request.method =="POST":
        newScoreEmail = "utkeitarol@gmail.com"
        i = 0
        #myOptions['email'] = newScoreEmail
        for z in range(50):
            currentScore = "score" + str(z)
            picture = "img" + str(z)
            if(z < 10):
                #newScoreEmail = otherScores[i]
                picture = "img00"+ str(z)+".png"
            elif(z < 100):
                picture = "img0" +str(z) + ".png"
            else:
                picture = "img" +str(z) + ".png"


            options.append(request.form[currentScore])
            myOptions[picture] = request.form[currentScore]

            #Adding this for database addition.
            newScore = Score(str(request.form['email']), picture,int(request.form[currentScore]))
            db.session.add(newScore)
            db.session.commit()
            #this should do it.

        options.append(newScoreEmail)
        #return myNumbers + " Check it"
        makeCSV(newScoreEmail)
        #This will train the item.
        finalScore = frontendSide(newScoreEmail)
        print(finalScore)
        return str(finalScore)
        #return jsonify(myOptions)
    elif request.method =="GET":
        return render_template('picscore3.html', i=0,j='0')

#Load transition stage....
@app.route("/compare",methods=['GET','POST'])
def compare():
    #need the 6 pictures of the item with the scores.
    #need 10 different instances of the score object.
    i = 0
    j = 0
    myNumbers = "Start:"
    options = []
    myOptions = {}

    if request.method =="POST":
        return jsonify(myOptions)
    elif request.method =="GET":
        return render_template('compare.html', i=0,j='0')
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
