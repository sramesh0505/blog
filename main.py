from flask import Flask,redirect,render_template,url_for



app=Flask(__name__)

@app.route("/")
def index():
    return "hill"



if __name__=="__main__":
    app.run(debug=True)
    