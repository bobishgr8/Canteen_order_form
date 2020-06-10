from flask import Flask, request , render_template
import datetime

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)