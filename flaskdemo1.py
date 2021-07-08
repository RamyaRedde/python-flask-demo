from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "my 1st api"