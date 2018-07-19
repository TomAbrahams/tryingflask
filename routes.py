#Thank god, we be in python
from flask import Flask, render_template, request
from models import db
from forms import SignUpForm

#Got to get that app.
app = Flask(__name__)

#Connection String
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
db.init_app(app) #Initialize app
#Need to generate forms with secure items.
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
            return "Successful Signed up!"
    elif request.method =="GET":
        return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
