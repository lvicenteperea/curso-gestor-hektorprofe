import os
import helpers
import db.clientes as db
import terminal.menu_acciones as accion


def iniciar():
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
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los clientes ")
        print("[2] API Listar clientes ")
        print("[3] Buscar un cliente   ")
        print("[4] Añadir un cliente   ")
        print("[5] Modificar un cliente")
        print("[6] Borrar un cliente   ")
        print("[0] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion in list(acciones.keys()):
            # ejecutamos la acción asignada a cada opción
            eval(f"accion.{acciones[opcion]}()")
            input("\nPresiona ENTER para continuar...")

    helpers.limpiar_pantalla()
