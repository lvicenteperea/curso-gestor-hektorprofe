import os
import helpers
import db.clientes as db
import terminal.menu_acciones as accion
import db.modelos.usuario_mod as usuario


# --------------------------------------------------------------------
def pinta(usu: usuario.Usuario):
    helpers.limpiar_pantalla()

    # Definir el array de cadenas
    menu = ("=",
            "Bienvenido al Gestor",
            f"{usu.get_nombre()}",
            "=",
            "[1] Listar los clientes ",
            "[2] API Listar clientes ",
            "[3] Buscar un cliente   ",
            "[4] Añadir un cliente   ",
            "[5] Modificar un cliente",
            "[6] Borrar un cliente   ",
            " ",
            "[0] Cerrar el Gestor    ",
            "=")

    # Encontrar la longitud de la cadena más larga
    max_length = max(len(item) for item in menu)

    # Crear una cadena de "=" con la longitud de la cadena más larga
    separator = "=" * max_length

    # Imprimir el menú con la línea de separación correcta
    for item in menu:
        if item == "=":
            print("   " + separator)
        elif item.startswith("["):
            print("   " + item)
        else:
            print("   " + item.center(max_length))


# --------------------------------------------------------------------
# INICIAR MENU
#  --------------------------------------------------------------------
def iniciar(usu: usuario.Usuario):
    opcion = None
    acciones = {'1': 'listar',
                '2': 'listar_API',
                '3': 'buscar',
                '4': 'add',
                '5': 'modificar',
                '6': 'borrar',
                '0': 'salir'
                }

    while opcion != '0':
       
        pinta(usu)

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion in list(acciones.keys()):
            # ejecutamos la acción asignada a cada opción
            eval(f"accion.{acciones[opcion]}()")
            input("\nPresiona ENTER para continuar...")

    helpers.limpiar_pantalla()
