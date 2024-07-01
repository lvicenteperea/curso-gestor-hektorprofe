import os
import helpers
import db.clientes as db
import terminal.menu_acciones as accion


def iniciar():
    opcion = None
    acciones = {'1': 'listar',
                '2': 'buscar',
                '3': 'add',
                '4': 'modificar',
                '5': 'borrar',
                '6': 'salir'
                }
    
    while opcion != '6':
        helpers.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor  ")
        print("========================")
        print("[1] Listar los clientes ")
        print("[2] Buscar un cliente   ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion in list(acciones.keys()):
            # ejecutamos la acción asignada a cada opción
            eval(f"accion.{acciones[opcion]}()")
            input("\nPresiona ENTER para continuar...")

    helpers.limpiar_pantalla()
