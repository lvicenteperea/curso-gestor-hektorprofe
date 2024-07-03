import helpers
import db.clientes as db
import requests
import config


def listar():
    print("Listando los clientes...\n")

    mi_lista = db.Clientes.listar()
    #for i, cli in enumerate(db.Clientes.listar()):
    for i, cli in enumerate(mi_lista):
        print(f"- Cliente {i} - {cli['dni']}")
        for clave, valor in cli.items():
            if clave != 'dni':
                print(f"   - {clave} - {valor}")
        print("")


def listar_API():

    print("Listando los clientes mediante API...\n")

    respuesta = requests.get(f"{config.URL}clientedb/")

    json = respuesta.json()

    for j in json:
        print(j)



def buscar():
    print("Buscando un cliente...\n")

    dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()

    cliente = db.Clientes.buscar(dni)

    print(cliente) if cliente else print("Cliente no encontrado.")



def add():
    print("Añadiendo un cliente...\n")

    dni = None
    while True:
        dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
        if helpers.dni_valido(dni, db.Clientes.lista):
            break

    nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
    apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()

    db.Clientes.crear(dni, nombre, apellido)

    print("Cliente añadido correctamente.")



def modificar():
    print("Modificando un cliente...\n")

    dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()
    cliente = db.Clientes.buscar(dni)

    if cliente:
        nombre   = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
        apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
        db.Clientes.modificar(cliente.dni, nombre, apellido)

        print("Cliente modificado correctamente.")
    else:
        print("Cliente no encontrado.")



def borrar():
    print("Borrando un cliente...\n")

    dni = helpers.leer_texto(3, 3, "DNI (2 int y 1 char)").upper()

    if db.Clientes.borrar(dni):
        print("Cliente borrado correctamente.") 
    else:
        print("Cliente no encontrado.")



def salir():
    print("Saliendo...\n")
