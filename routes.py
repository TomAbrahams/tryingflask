#Thank god, we be in python
from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignUpForm, LoginForm

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
@app.route("/picscore",methods=['GET','POST'])
def picscore():
    form = PicScoreForm()
    if request.method =="POST":
        if form.validate() == False:
            return render_template('picscore.html',form=form)
        else:
            newScoreEmail = "utkeitarol@gmail.com"

            score000 = Score(newScoreEmail, "image000.png", form.score000.data)
            score001 = Score(newScoreEmail, "image001.png", form.score001.data)
            score002 = Score(newScoreEmail, "image002.png", form.score002.data)
            score003 = Score(newScoreEmail, "image003.png", form.score003.data)
            score004 = Score(newScoreEmail, "image004.png", form.score004.data)
            score005 = Score(newScoreEmail, "image005.png", form.score005.data)
            score006 = Score(newScoreEmail, "image006.png", form.score006.data)
            score007 = Score(newScoreEmail, "image007.png", form.score007.data)
            score008 = Score(newScoreEmail, "image008.png", form.score008.data)
            score009 = Score(newScoreEmail, "image009.png", form.score009.data)

            score010 = Score(newScoreEmail, "image010.png", form.score010.data)
            score011 = Score(newScoreEmail, "image011.png", form.score011.data)
            score012 = Score(newScoreEmail, "image012.png", form.score012.data)
            score013 = Score(newScoreEmail, "image013.png", form.score013.data)
            score014 = Score(newScoreEmail, "image014.png", form.score014.data)
            score015 = Score(newScoreEmail, "image015.png", form.score015.data)
            score016 = Score(newScoreEmail, "image016.png", form.score016.data)
            score017 = Score(newScoreEmail, "image017.png", form.score017.data)
            score018 = Score(newScoreEmail, "image018.png", form.score018.data)
            score019 = Score(newScoreEmail, "image019.png", form.score019.data)

            score020 = Score(newScoreEmail, "image020.png", form.score020.data)
            score021 = Score(newScoreEmail, "image021.png", form.score021.data)
            score022 = Score(newScoreEmail, "image022.png", form.score022.data)
            score023 = Score(newScoreEmail, "image023.png", form.score023.data)
            score024 = Score(newScoreEmail, "image024.png", form.score024.data)
            score025 = Score(newScoreEmail, "image025.png", form.score025.data)
            score026 = Score(newScoreEmail, "image026.png", form.score026.data)
            score027 = Score(newScoreEmail, "image027.png", form.score027.data)
            score028 = Score(newScoreEmail, "image028.png", form.score028.data)
            score029 = Score(newScoreEmail, "image029.png", form.score029.data)

            score030 = Score(newScoreEmail, "image030.png", form.score030.data)
            score031 = Score(newScoreEmail, "image031.png", form.score031.data)
            score032 = Score(newScoreEmail, "image032.png", form.score032.data)
            score033 = Score(newScoreEmail, "image033.png", form.score033.data)
            score034 = Score(newScoreEmail, "image034.png", form.score034.data)
            score035 = Score(newScoreEmail, "image035.png", form.score035.data)
            score036 = Score(newScoreEmail, "image036.png", form.score036.data)
            score037 = Score(newScoreEmail, "image037.png", form.score037.data)
            score038 = Score(newScoreEmail, "image038.png", form.score038.data)
            score039 = Score(newScoreEmail, "image039.png", form.score039.data)

            score040 = Score(newScoreEmail, "image040.png", form.score040.data)
            score041 = Score(newScoreEmail, "image041.png", form.score041.data)
            score042 = Score(newScoreEmail, "image042.png", form.score042.data)
            score043 = Score(newScoreEmail, "image043.png", form.score043.data)
            score044 = Score(newScoreEmail, "image044.png", form.score044.data)
            score045 = Score(newScoreEmail, "image045.png", form.score045.data)
            score046 = Score(newScoreEmail, "image046.png", form.score046.data)
            score047 = Score(newScoreEmail, "image047.png", form.score047.data)
            score048 = Score(newScoreEmail, "image048.png", form.score048.data)
            score049 = Score(newScoreEmail, "image049.png", form.score049.data)

            score050 = Score(newScoreEmail, "image050.png", form.score050.data)
            score051 = Score(newScoreEmail, "image051.png", form.score051.data)
            score052 = Score(newScoreEmail, "image052.png", form.score052.data)
            score053 = Score(newScoreEmail, "image053.png", form.score053.data)
            score054 = Score(newScoreEmail, "image054.png", form.score054.data)
            score055 = Score(newScoreEmail, "image055.png", form.score055.data)
            score056 = Score(newScoreEmail, "image056.png", form.score056.data)
            score057 = Score(newScoreEmail, "image057.png", form.score057.data)
            score058 = Score(newScoreEmail, "image058.png", form.score058.data)
            score059 = Score(newScoreEmail, "image059.png", form.score059.data)

            score060 = Score(newScoreEmail, "image060.png", form.score060.data)
            score061 = Score(newScoreEmail, "image061.png", form.score061.data)
            score062 = Score(newScoreEmail, "image062.png", form.score062.data)
            score063 = Score(newScoreEmail, "image063.png", form.score063.data)
            score064 = Score(newScoreEmail, "image064.png", form.score064.data)
            score065 = Score(newScoreEmail, "image065.png", form.score065.data)
            score066 = Score(newScoreEmail, "image066.png", form.score066.data)
            score067 = Score(newScoreEmail, "image067.png", form.score067.data)
            score068 = Score(newScoreEmail, "image068.png", form.score068.data)
            score069 = Score(newScoreEmail, "image069.png", form.score069.data)

            score070 = Score(newScoreEmail, "image070.png", form.score070.data)
            score071 = Score(newScoreEmail, "image071.png", form.score071.data)
            score072 = Score(newScoreEmail, "image072.png", form.score072.data)
            score073 = Score(newScoreEmail, "image073.png", form.score073.data)
            score074 = Score(newScoreEmail, "image074.png", form.score074.data)
            score075 = Score(newScoreEmail, "image075.png", form.score075.data)
            score076 = Score(newScoreEmail, "image076.png", form.score076.data)
            score077 = Score(newScoreEmail, "image077.png", form.score077.data)
            score078 = Score(newScoreEmail, "image078.png", form.score078.data)
            score079 = Score(newScoreEmail, "image079.png", form.score079.data)

            score080 = Score(newScoreEmail, "image080.png", form.score080.data)
            score081 = Score(newScoreEmail, "image081.png", form.score081.data)
            score082 = Score(newScoreEmail, "image082.png", form.score082.data)
            score083 = Score(newScoreEmail, "image083.png", form.score083.data)
            score084 = Score(newScoreEmail, "image084.png", form.score084.data)
            score085 = Score(newScoreEmail, "image085.png", form.score085.data)
            score086 = Score(newScoreEmail, "image086.png", form.score086.data)
            score087 = Score(newScoreEmail, "image087.png", form.score087.data)
            score088 = Score(newScoreEmail, "image088.png", form.score088.data)
            score089 = Score(newScoreEmail, "image089.png", form.score089.data)

            score090 = Score(newScoreEmail, "image070.png", form.score090.data)
            score091 = Score(newScoreEmail, "image071.png", form.score091.data)
            score092 = Score(newScoreEmail, "image072.png", form.score092.data)
            score093 = Score(newScoreEmail, "image073.png", form.score093.data)
            score094 = Score(newScoreEmail, "image074.png", form.score094.data)
            score095 = Score(newScoreEmail, "image075.png", form.score095.data)
            score096 = Score(newScoreEmail, "image076.png", form.score096.data)
            score097 = Score(newScoreEmail, "image077.png", form.score097.data)
            score098 = Score(newScoreEmail, "image078.png", form.score098.data)
            score099 = Score(newScoreEmail, "image079.png", form.score099.data)
            )
#Homepage
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/login")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
