from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator

import db.clientes as db
import helpers


headers = {"content-type": "charset=utf-8"}

class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)

class ModeloCrearCliente(ModeloCliente):
    @validator("dni")
    def validar_dni(cls, dni):
        if not helpers.dni_valido(dni, db.Clientes.lista):
            raise ValueError("Cliente ya existente o DNI incorrecto")
        
        return dni


router = FastAPI(title="API del Gestor de clientes",
              description="Ofrece diferentes funciones para gestionar los clientes.",
              #prefix="/clientes", # ver documentación para ver como hay que hacer las llamadas
              tags=["Clientes"],  # es para que en la documentación separe los servicios de esta API
              #responses= {404: {"message": "No encontrado"}}
             )



@router.get("/clientes/", tags=["Clientes"])
async def clientes():
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)


@router.get("/clientes/buscar/{dni}/", tags=["Clientes"])
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return JSONResponse(content=cliente.to_dict(), headers=headers)

@router.post("/clientes/crear/")
async def clientes_crear(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    
    raise HTTPException(status_code=404)

@router.put("/clientes/actualizar/", tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.modificar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
        
    raise HTTPException(status_code=404)


@router.delete("/clientes/borrar/{dni}/", tags=["Clientes"])
async def clientes_borrar(dni: str):
    if db.Clientes.buscar(dni=dni):
        cliente = db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    
    raise HTTPException(status_code=404)