'''
este fichero ha sido la base del ejercicio, pero tiene todo lo necesario para realizar
el ejercicio de cliente, en un solo fichero y tirando de un csv como bbdd

Desde este se han sacado o sería lo que con BBDD es:
- db
  +- esquemas
    -- cliente.py
  +- modulos
    -- cliente.py

  -- dbcliente.py
'''

import csv
import config

def cliente_schema(cliente_cursor) -> dict:
    print("Aqui estamos2 ", type(cliente_cursor))
    return {"dni": cliente_cursor["dni"],
            "nombre": cliente_cursor["nombre"],
            "apellido": cliente_cursor["apellido"]
            }

def clientes_schema(clientes_cursor) -> list:
    return [cliente_schema(cliente) for cliente in clientes_cursor]


class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellido': self.apellido}

'''
    El código proporcionado is a Python script that includes unit tests for a database module. It uses the unittest library to define test cases for different database operations like searching, creating, modifying, and deleting client records.

    Aquí hay un resumen de los componentes principales y funcionalidades del código:

       - El script importa los módulos necesarios: copy, unittest y un módulo personalizado llamado base de datos (alias db). 
       - Se define una clase TestDatabase que hereda de unittest.TestCase. Esta clase contiene cuatro métodos de prueba: setUp, test_buscar_cliente, test_crear_cliente, test_modificar_cliente y test_borrar_cliente. 
       - El método setUp es un método especial que se ejecuta antes de cada prueba en la clase. En este método, se crea una lista de objetos de clientes y se asigna al atributo 'lista' de la clase Clientes en el módulo de la base de datos. 
       - El método test_buscar_cliente prueba la funcionalidad del método 'buscar' en la clase Clientes comprobando si recupera correctamente los objetos de clientes existentes y maneja los clientes que no existen. 
       - El método test_crear_cliente prueba el método 'crear' creando un nuevo objeto de cliente, verificando si la lista de clientes ha aumentado en tamaño y verificando los detalles del nuevo cliente. 
       - El método test_modificar_cliente prueba el método 'modificar' copiando un cliente existente, modificándolo y luego verificando si los cambios se reflejan correctamente. 
       - El método test_borrar_cliente prueba el método 'borrar' eliminando un cliente y asegurándose de que ya no esté presente en la lista de clientes. 
    
    Finalmente, el script ejecuta las pruebas unitarias usando unittest.main() cuando se ejecuta directamente (if name=='main':).

    El código está bien estructurado y sigue los principios de pruebas unitarias para verificar la corrección de las operaciones del módulo de la base de datos en relación con la gestión de clientes.
'''
class Clientes:

    lista = []

    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=config.DELIMITER_FIELDS)
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)
     
    @staticmethod
    def listar():
        mi_lista = []
        for cliente in Clientes.lista:
            mi_lista.append(cliente.to_dict())
        
        return mi_lista
    
    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni, nombre, apellido):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellido))