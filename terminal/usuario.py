import helpers
import db.modelos.usuario_mod as usuario
import error.mi_error as ctr_errores
import inspect
#import db.clientes as db
#import requests
#import config

def valida_usuario() -> bool:

    usu = helpers.leer_texto(2, 12, "introduce tu usuario")
    
    if usu.upper() != "Q":
        pwd = helpers.leer_texto(2, 12, "introduce tu pwd")
        
        if pwd.upper() != "Q":
            mi_usuario = usuario.Usuario(usu, pwd)
            
            return mi_usuario.valida_usu_pwd()
        else:
            return ctr_errores.MiError(f"Error ({inspect.currentframe().f_code.co_name})", "Salida voluntaria del sistema")
    else:
        return ctr_errores.MiError(f"Error ({inspect.currentframe().f_code.co_name})", "Salida voluntaria del sistema")
