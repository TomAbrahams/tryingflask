#Thank god, we be in python
from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
