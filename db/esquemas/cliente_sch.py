def cliente_schema(cliente_cursor) -> dict:
    print("Aqui estamos2 ", type(cliente_cursor))
    return {"dni": cliente_cursor["dni"],
            "nombre": cliente_cursor["nombre"],
            "apellido": cliente_cursor["apellido"]
            }

def clientes_schema(clientes_cursor) -> list:
    return [cliente_schema(cliente) for cliente in clientes_cursor]

