import helpers
import db.db_mysql as db
#import db.clientes as db
#import requests
#import config

def valida_usuario() -> bool:

    usu = helpers.leer_texto(2, 12, "introduce tu usuario")
    pwd = helpers.leer_texto(2, 12, "introduce tu pwd")
    
    return db.busca_usuario(usu, pwd)
