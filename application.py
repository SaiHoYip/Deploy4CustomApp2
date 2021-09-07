from flask import Flask, request, Response
from flask import render_template
import help
import sqlite3
import random
application = app = Flask(__name__)
@app.route("/")
def Guessgame():
    return render_template("home.html")


@app.route('/guess', methods=['POST'])
def result():
    global guessesTaken
    guessesTaken = 0
    number = random.randint(1,10)
    while guessesTaken != 6:
        if int(request.form['guess']) == number:
            answer = "Correct"
        elif int(request.form['guess']) < number:
            answer = "Too Low"
        else:
            answer = "Too High"
        guessesTaken += 1
        attempt = "you are on guess " + str(guessesTaken)
    return render_template("home.html", answer=answer, attempt=attempt)

app.run()