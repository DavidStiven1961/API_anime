from fastapi import APIRouter
from Models.Personaje import personaje as Bpersonaje
from fastapi import  Path, Query, Depends
from fastapi.responses import JSONResponse,HTMLResponse
from Config.database import Session
from Services.SCharacters import Pservices
from fastapi.encoders import jsonable_encoder


personaje_router = APIRouter()
db = Session()


@personaje_router.get('/personaje', tags =["Personajes"], response_model=list[Bpersonaje]) #response_model=Bpersonaje, status_code=200)
def get_personage() ->list[Bpersonaje]:
    db = Session()
    resul = Pservices(db).retonar_personajes()
    return JSONResponse(content=jsonable_encoder(resul))

@personaje_router.get('/personaje/{id}', tags =["Personajes"], response_model=Bpersonaje) 
def get_personage(id: int = Path(ge=1)) ->Bpersonaje:
    db = Session()
    resul = Pservices(db).retornar_personaje(id)
    if not resul:
        return JSONResponse(status_code=404, content={"menssage":"Personaje no encontrado"})
    return JSONResponse(content=jsonable_encoder(resul))

@personaje_router.get('/personaje/anime/', tags =["Personajes"], response_model=list[Bpersonaje]) 
def get_personage(anime : str) ->list[Bpersonaje]:
    db = Session()
    resul = Pservices(db).Character_by_anime(anime)
    if not resul:
        return JSONResponse(status_code=404, content={"menssage":"Personajes no encontrados"})
    return JSONResponse(content=jsonable_encoder(resul))

@personaje_router.post('/personaje/create/', tags =["Personajes"], response_model= dict)
def pots_create_personaje(personaje: Bpersonaje) -> dict:
    db = Session()
    resul = Pservices(db).Create_personaje(personaje)
    return JSONResponse(status_code=202, content={"menssage":"Personajes Creado"})

@personaje_router.put('/personaje/update/{id}', tags =["Personajes"], response_model= dict)
def put_personaje(personajes: Bpersonaje, id : int = Path(ge=1)) -> dict:
    db = Session()
    resul = Pservices(db).update_personaje(id, personajes)
    return JSONResponse(status_code=202, content={"menssage":"El Personaje a Sido Actualizado"})

@personaje_router.delete('/personaje/delete/{id}', tags =["Personajes"], response_model= dict)
def delete_Personaje(id : int = Path(ge=1)):
    db = Session()
    resul = Pservices(db).delte_personaje(id)
    return JSONResponse(status_code=202, content={"menssage":"El Personaje a Eliminado"})





    
