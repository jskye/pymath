from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

def getobjectimg(name, url="/"):
    if name == "Hexahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Hexahedron.svg"
    elif name == "Octahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/0/07/Octahedron.svg"
    elif name =="Tetrahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/f/fc/Tetrahedron.svg"
    elif name == "Icosahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/b/b7/Icosahedron.svg"
    elif name == "Dodecahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/a/a4/Dodecahedron.svg"
    else:
        url = "/"
    return url

@app.route("/")
def index():
    return "Flask App!"

@app.route("/pymath/")
def math():
    return render_template(
    'index.html')

@app.route("/pymath/<string:name>/")
def object(name):
    print(name)
    return render_template(
    'object.html',name=name, imgurl=getobjectimg(name))


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=80)
    app.run(host='localhost', port=5050)
