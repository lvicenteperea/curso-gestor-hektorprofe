#pip install "fastapi[all]"
from fastapi import FastAPI

#pip install "uvicorn[standard]" 
#para ejecutar esto: uvicorn api:app --reload  --> que abre un servidor, normalmente en: http://127.0.0.1:8000
app = FastAPI(title="API del Gestor de clientes",
              description="Ofrece diferentes funciones para gestionar los clientes.",)

from routers import clientes, clientes_db
app.include_router(clientes.router)
app.include_router(clientes_db.router)


@app.get("/", tags=["general"])
async def root():
    return "Hola Curso Gestor"
