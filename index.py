from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "qwertyuiop_789456"

@app.route("/index")
def index():
	flash("What's your name?")
	return render_template("index.html")