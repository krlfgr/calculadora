from flask import Flask, request, render_template
from livereload import Server
from operaciones import sumar
from operaciones import division_piso

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/suma")
def ruta_suma():
    numero1=request.args.get("numero1",type=float)
    numero2=request.args.get("numero2",type=float)
    if numero1 is None or numero2 is None:
        return "Faltan datos"
    return f"El resultado de la suma es {sumar(numero1,numero2)}"

@app.route("/division_piso")
def ruta_division_piso():
    numero1=request.args.get("numero1",type=float)
    numero2=request.args.get("numero2",type=float)
    if numero1 is None or numero2 is None:
        return "Faltan datos"
    return f"El resultado de la division piso es {division_piso(numero1,numero2)}"

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()