#pip install mysql-connector-python
import mysql.connector

# ----------------------------------------------
# conectamos a la BBDD de MySQL
# ----------------------------------------------
def conectar() -> mysql.connector:
    try:
        # Establecer la conexión con la base de datos MySQL local
        return mysql.connector.connect(host='localhost',
                                       user='root',  # Reemplaza con tu nombre de usuario de MySQL
                                       password='admin',  # Reemplaza con tu contraseña de MySQL
                                       database='curso_gestor_hektor'  # Reemplaza con el nombre de tu base de datos
                                      )
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")

# ----------------------------------------------
# desconectamos de la BBDD de MySQL
# ----------------------------------------------
def desconectar(conn: mysql.connector):
    try:
        if conn.is_connected():
            conn.close()
            print("Conexión a MySQL cerrada")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

# ----------------------------------------------
# Retornamos un cursor para una select de la BBDD
# ----------------------------------------------
def cursor_select(conn: mysql.connector, consulta: str, *args):

    try:
        # Crear un objeto cursor usando el método cursor()
        cursor = conn.cursor()
        
        # Ejecutar la consulta SQL con parámetros
        cursor.execute(consulta, args)
        
        # Obtener el registro de la tabla 'usuarios' que coincide con el nombre de usuario
        return cursor.fetchone()


    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        # Cerrar el cursor y la conexión
        cursor.close()
