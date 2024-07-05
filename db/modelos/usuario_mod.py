import db.db_mysql as db_mysql
import error.mi_error as ctr_errores
import inspect

class Usuario():

    tipo = 'Normal'

    def __init__(self, nombre, pwd) -> None:
        self.nombre = nombre
        self.pwd = pwd


    def get_nombre(self):
        return self.nombre + (self.tipo)

    # Función para conectar a la base de datos MySQL y obtener datos de la tabla 'usuarios' basado en el nombre de usuario
    def valida_usu_pwd(username: str, password: str) -> bool:

        usuario = None
        query = "SELECT pwd FROM usuarios WHERE usuario = %s"

        try:
            # Obtener el registro de la tabla 'usuarios' que coincide con el nombre de usuario
            result = db_mysql.cursor_select(None,   # no enviamos conexión pra que se conecte la propia función
                                            query,
                                            username
                                           )
            
            # Verificar si se encontró un usuario y comparar la contraseña
            if isinstance(result, tuple):  # not ..... ctr_errores.MiError):
                stored_password = result[0]
                # Suponiendo que 'ppp' está almacenado como un hash SHA256 de la contraseña
                password_hash = password   # sha256(password.encode()).hexdigest()
                ret = (password_hash == stored_password)
                if ret:
                    usuario = Usuario(username, password)
                #print(f"resultado: {ret}")
            else:
                ctr_errores.MiError("Error acceso BBDD", query)
                #print(f"Error: en la llamada")                

        except Exception as e:
            ctr_errores.MiError(f"Error ({inspect.currentframe().f_code.co_name})", str(e))
        
        finally:
            return usuario

'''
# Función para conectar a la base de datos MySQL y obtener datos de la tabla 'usuarios' basado en el nombre de usuario
    def valida_usu_pwd(username: str, password: str) -> bool:

        ret = False

        try:
            # Establecer la conexión con la base de datos MySQL local
            connection = db_mysql.conectar()
            
            # Crear un objeto cursor usando el método cursor()
            cursor = connection.cursor()
            
            # Ejecutar la consulta SQL con parámetros
            query = "SELECT pwd FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (username,))
            
            # Obtener el registro de la tabla 'usuarios' que coincide con el nombre de usuario
            result = cursor.fetchone()
            
            # Verificar si se encontró un usuario y comparar la contraseña
            if result:
                stored_password = result[0]
                # Suponiendo que 'ppp' está almacenado como un hash SHA256 de la contraseña
                password_hash = password   # sha256(password.encode()).hexdigest()
                ret = password_hash == stored_password
                print(f"resultado: {ret}")


        except mysql.connector.Error as error:
            print(f"Error: {error}")
        finally:
            # Cerrar el cursor y la conexión
            cursor.close()
            db_mysql.desconectar(connection)
            return ret
'''


'''
# Función para conectar a la base de datos MySQL y obtener datos de la tabla 'usuarios'
def fetch_users():
    try:
        # Establecer la conexión con la base de datos MySQL local
        connection = mysql.connector.connect(
            host='localhost',
            user='tu_usuario',  # Reemplaza con tu nombre de usuario de MySQL
            password='tu_contraseña',  # Reemplaza con tu contraseña de MySQL
            database='nombre_de_tu_base_de_datos'  # Reemplaza con el nombre de tu base de datos
        )
        
        # Crear un objeto cursor usando el método cursor()
        cursor = connection.cursor()
        
        # Ejecutar la consulta SQL
        cursor.execute("SELECT * FROM usuarios")
        
        # Obtener todas las filas de la tabla 'usuarios'
        users = cursor.fetchall()
        
        # Imprimir los datos obtenidos
        for user in users:
            print(user)
        
    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        # Cerrar el cursor y la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


'''