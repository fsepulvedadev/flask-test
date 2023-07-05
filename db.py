import pymysql


def obtener_conexion():
    return pymysql.connect(
        host="localhost", user="fsepulvedadev", password="orejasnrc123", db="juegos"
    )
