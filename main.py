from fastapi import FastAPI
from Config.database import Session, engine
from fastapi.responses import JSONResponse, HTMLResponse
from Routers.Personaje import personaje_router
from BModel.PersonajesB import Base

app = FastAPI()
app.include_router(personaje_router)

app.title = "Mi primera API hecha solo"
app.version = "0.01"

Base.metadata.create_all(bind=engine)

@app.get('/')
def message():
    return JSONResponse(content="Biemvenido a mi API")