import helpers
import db.modelos.usuario_mod as usuario
#import db.clientes as db
#import requests
#import config

def valida_usuario() -> bool:

    usu = helpers.leer_texto(2, 12, "introduce tu usuario")
    pwd = helpers.leer_texto(2, 12, "introduce tu pwd")
    
    return usuario.Usuario.valida_usu_pwd(usu, pwd)
