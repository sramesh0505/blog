from flask import Flask,redirect,render_template,url_for
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")



#error pages samples
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404error.html"),404
@app.errorhandler(500)
def internal_error(error):
    return render_template("500error.html"),500

if __name__=="__main__":
    app.run(debug=True)
    