from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "hello from flask"

@app.route("/display")
def display():
    return "display from flask"


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5050)

