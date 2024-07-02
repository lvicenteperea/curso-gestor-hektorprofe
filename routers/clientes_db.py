from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from db.modelos.cliente_mod import Cliente
from db.db_connect import db_connect
from db.esquemas.cliente_sch import cliente_schema, clientes_schema
from bson import ObjectId

headers = {"content-type": "charset=utf-8"}

router = APIRouter(prefix="/clientedb", # ver documentación para ver como hay que hacer las llamadas
                   tags=["Cliente BBDD"],  # es para que en la documentación separe los servicios de esta API
                   responses= {404: {"message": "No encontrado"}}
                  )


@router.get("/",)
async def clientes():

    lista = clientes_schema(db_connect.clientes.find())
    return JSONResponse(content=lista, headers=headers)

    '''
    lista = []
    #lista = [cliente.to_dict() for cliente in db.Clientes.lista]
    for cliente in db.Clientes.lista:
        lista.append(cliente.to_dict())

    return JSONResponse(content=lista, headers=headers)
    '''

'''
@router.get("/buscar/{dni}/")
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return JSONResponse(content=cliente.to_dict(), headers=headers)

@router.post("/crear/")
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    
    raise HTTPException(status_code=404)

@router.put("/actualizar/")
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
        
    raise HTTPException(status_code=404)


@router.delete("/borrar/{dni}/")
async def clientes_borrar(dni: str):
    if db.Clientes.buscar(dni=dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    
    raise HTTPException(status_code=404)
'''