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
