from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from Routers.Personaje import personaje_router

app = FastAPI()
app.include_router(personaje_router)

app.title = "Mi primera API hecha solo"
app.version = "0.01"

@app.get('/')
def message():
    return JSONResponse(content="Biemvenido a mi API")