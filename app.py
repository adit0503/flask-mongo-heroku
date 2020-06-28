from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
app = Flask(__name__)


client = MongoClient("mongodb+srv://qxqt:aditya1234@cluster-demo-weusg.mongodb.net/gita?retryWrites=true&w=majority")
gita = client["gita"]
shloka = gita["shloka"]

@app.route("/")
def indexHomePage():
    return render_template("index.html")

@app.route("/submitShloka")
def submitShloka():
    return render_template("submitShloka.html")

@app.route("/submit", methods=['POST'])
def submit():
    b_id = request.values.get("book")
    ch_id = request.values.get("chapter")
    sh_id = request.values.get("shloka")
    id = str(b_id) + "ch" + str(ch_id) + "sh" + str(sh_id)
    sh = request.values.get("shlokatext")
    new_shloka = {"_id":id,"text":sh}
    shloka.insert_one(new_shloka)
    return redirect("/submitShloka")

@app.route("/bhagwadgita")
def bhagwadgita():
    return render_template("bhagwadgita.html")

@app.route("/display", methods=['POST','GET'])
def display():
    ch_id = request.values.get("chapter")
    sh_id = request.values.get("shloka")
    id = "BG" + "ch" + str(ch_id) + "sh" + str(sh_id)
    curr_shloka = shloka.find_one(id)
    if curr_shloka:
        return render_template("bhagwadgita.html",text=curr_shloka["text"].strip(),verse=curr_shloka["verse"].strip(),chapter=ch_id,shloka=sh_id)
    else:
        return redirect("/bhagwadgita")

if __name__ == "__main__":
    app.run(debug=True)
