from db import obtener_conexion


def controller_insertar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
            (nombre, descripcion, precio),
        )
    conexion.commit()
    conexion.close()


def controller_obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos


def controller_eliminar_juego(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM juegos WHERE id=%s", (id,))
    conexion.commit()
    conexion.close()


def controller_obtener_juego_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM juegos WHERE id=%s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def controller_actualizar_juego(nombre, descripcion, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
            (nombre, descripcion, precio, id),
        )
        conexion.commit()
        conexion.close()
