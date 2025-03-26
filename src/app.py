from flask import Flask
import mysql.connector

app = Flask(__name__)

def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="rootpassword",
            database="testdb"
        )
        return conn
    except mysql.connector.Error as err:
        return None

@app.route("/")
def hola_mundo():
    conn = conectar_bd()
    if conn:
        return "¡Hola Mundo! Conexión a MySQL exitosa."
    else:
        return "¡Hola Mundo! Error al conectar con MySQL."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
