from flask import Flask

app = Flask('server')

@app.route("/")
def hello_world():
    return "Hello World!"