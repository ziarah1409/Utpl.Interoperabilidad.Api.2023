from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="API de Clientes",
    description="API Clientes",
    version="1.0.1",
    contact={
        "name": "Ziarah Apolo Rivera",
        "email": "zlapolo@utpl.edu.ec",
        "url": "https://github.com/ziarah1409/Utpl.Interoperabilidad.Api.2023.git"
    },
    license_info={
        "name": "MIT License",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=[
        {
            "name": "Persona",
            "description": "Operaciones para el manejo de personas"
        }
    ]
)

# Modelo de datos para una persona
class Cliente(BaseModel):
    nombre: str
    direccion: str
    telefono: str
    id: int

# Lista para almacenar personas (simulación de base de datos)
cliente_db = []

# Operación para crear una persona
@app.post("/cliente/", response_model=Cliente)
def create_cliente(person: Cliente):
    cliente_db.append(person)
    return person

# Operación para obtener todas las personas
@app.get("/cliente/", response_model=List[Cliente])
def get_all_cliente():
    return cliente_db

# Operación para obtener una persona por ID
@app.get("/cliente/{cliente_id}", response_model=Cliente)
def get_cliente_by_id(cliente_id: int):
    for person in cliente_db:
        if person.id == cliente_id:
            return person
    raise HTTPException(status_code=404, detail="Cliente no encontrada")

# Operación para editar una persona por ID
@app.put("/cliente/{cliente_id}", response_model=Cliente)
def update_cliente(cliente_id: int, updated_cliente: Cliente):
    for index, person in enumerate(cliente_db):
        if person.id == cliente_id:
            cliente_db[index] = updated_cliente
            return updated_cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrada")

# Operación para eliminar una persona por ID
@app.delete("/cliente/{cliente_id}", response_model=Cliente)
def delete_cliente(cliente_id: int):
    for index, cliente in enumerate(cliente_db):
        if cliente_id == cliente_id:
            deleted_cliente = cliente_db.pop(index)
            return deleted_cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrada")
