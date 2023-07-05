from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from controlador_juegos import (
    controller_obtener_juegos,
    controller_obtener_juego_por_id,
    controller_actualizar_juego,
    controller_eliminar_juego,
    controller_insertar_juego,
)

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    juegos = controller_obtener_juegos()
    return render_template("index.html", juegos=juegos)


@views.route("/formulario_agregar_juego")
def form_agregar_juego():
    return render_template("agregar_juego.html")


@views.route("/agregar_juego", methods=["POST"])
def agregar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controller_insertar_juego(nombre, descripcion, precio)
    return redirect(url_for("views.home"))


@views.route("/actualizar_juego", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controller_actualizar_juego(nombre, descripcion, precio, id)
    return redirect(url_for("views.home"))


@views.route("/formulario_editar_juego/<int:id>")
def editar_juego(id):
    juego = controller_obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)


@views.route("/eliminar_juego", methods=["POST"])
def eliminar_juego():
    controller_eliminar_juego(request.form["id"])
    return redirect(url_for("views.home"))
