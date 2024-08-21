from fastapi import APIRouter
from Models.Personaje import personaje as Bpersonaje
from fastapi import  Path, Query, Depends
from fastapi.responses import JSONResponse,HTMLResponse


personaje_router = APIRouter()


@personaje_router.get('/personaje', tags =["Personajes"], response_model=Bpersonaje) #response_model=Bpersonaje, status_code=200)
def get_personage():
    resul: Bpersonaje
    return JSONResponse(content=resul)
    
