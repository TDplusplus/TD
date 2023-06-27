
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, redirect, url_for, render_template, request, flash,jsonify
import pymysql

MySQL=pymysql.connect(host="TDPP.mysql.pythonanywhere-services.com",user="TDPP",password="2580369Pefer.")
connection=MySQL.cursor()
connection.execute("use TDPP$games;")


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("Home.html")


@app.route("/Truth_or_Dare")
def truth_or_dare():
    return render_template("Custom.html")


@app.route("/Truth_or_Dare_play" , methods=["post",'POST','get'])
def truth_or_dare_play():
    Level=request.form.get("Family")
    Level1 = request.form.get("Friendly")
    Level2 = request.form.get("Dirty")

    if(Level=="on"):
        query="SELECT * FROM `game_data` where `Level`='Adult' and `Type`='dare' limit 1 OFFSET 2"
        return render_template("Game.html",Current_Level="Family",Question="Welcome to Truth or Dare")
    elif(Level1=="on"):
        return render_template("Game.html",Current_Level="Friendly",Question="Welcome to Truth or Dare")
    elif (Level2 == "on"):
        return render_template("Game.html",Current_Level="Adult",Question="Welcome to Truth or Dare")

    else:
        return render_template("Custom.html")



@app.route("/Truth_or_Dare_play_continuously/<index>/<type>/<level>")
def truth_or_dare_play_continously(index,type,level):
    #print(index,type)
    return render_template("Game.html",Current_Level=level,index=index)


@app.route("/Truth_or_Dare_play_continuous" ,methods=["POST"])
def truth_or_dare_play_continous():
    print(request.form.get("json"))
    content=eval(request.form.get("json"))
    #print(str(content['index']))
    connection.execute("SELECT * FROM `game_data` WHERE `Type`='"+content['type']+"' and `Level`='"+content['level']+"' limit 1 offset "+str(content['index'])+";")
    questions = connection.fetchall()
    #print(questions)
    return jsonify({"Current_Level": "friendly"," index":1, "Question": questions[0][1]})





@app.route("/live")
def Live():
    return render_template('index.html')

