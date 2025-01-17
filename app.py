from flask import Flask, flash, redirect, render_template, request, session, abort
import wikipedia

app = Flask(__name__)

def getobjnet(name):
    if name == "Hexahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Hexahedron_flat_color.svg/240px-Hexahedron_flat_color.svg.png"
    elif name == "Octahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Octahedron_flat.svg/240px-Octahedron_flat.svg.png"
    elif name == "Tetrahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Tetrahedron_flat.svg/240px-Tetrahedron_flat.svg.png"
    elif name == "Icosahedron":
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Icosahedron_flat.svg/240px-Icosahedron_flat.svg.png"
    elif name == "Dodecahedron":
        url = "https:/upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Dodecahedron_flat.svg/240px-Dodecahedron_flat.svg.png"
    else:
        url = "/"
    return url


def getobjdef(name):
    objdef = wikipedia.WikipediaPage(title = name).summary
    return objdef

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
    'object.html',name=name, imgurl=getobjectimg(name), objdef=getobjdef(name), objnet=getobjnet(name))


if __name__ == "__main__":
    # app.run(host='127.0.0.1', port=80)
    app.run(host='localhost', port=5050)
