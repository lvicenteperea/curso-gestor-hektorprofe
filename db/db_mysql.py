#pip install mysql-connector-python
import mysql.connector
import mysql.connector.cursor

# ----------------------------------------------
# conectamos a la BBDD de MySQL
# ----------------------------------------------_
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
#
# tiene que haber algo que indique que no devuelve un cursor 
# cuando todo el OK, que cuando es Ko retorna una clase de tipo error o lo que sea
# ----------------------------------------------
def cursor_select(conn: mysql.connector, consulta: str, *args) -> mysql.connector.cursor:

    conectado = False

    try:
        # si no estamos conectados, nos conectamos
        if not conn:  ## .is_connected():   --> no hace falta, porque no vendría definida la variable
            conn = conectar()
            conectado = True

        # Crear un objeto cursor usando el método cursor()
        cursor = conn.cursor()
        
        # Ejecutar la consulta SQL con parámetros
        cursor.execute(consulta, args)
        
        # Obtener el registro de la tabla 'usuarios' que coincide con el nombre de usuario
        mi_cursor = cursor.fetchone()

        # si me he conectado en este llamada, me desconecto
        if conectado:
            desconectar(conn)

        return mi_cursor
    

    except mysql.connector.Error as error:
        print(f"Error: {error}")