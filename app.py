from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Flask App!"

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template(
    'test.html',name=name)


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=80)
    app.run(host='localhost', port=5050)
