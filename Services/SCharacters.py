from BModel.PersonajesB import Character
from Models.Personaje import personaje
class Pservices():

    def __init__(self, db) -> None:
        self.db = db

    def retonar_personajes(self):
        resul = self.db.query(Character).all()
        return resul
    
    def retornar_personaje(self, id):
        resul = self.db.query(Character).filter(Character.id == id).first()
        return resul
    
    def Character_by_anime(self, anime):
        resul = self.db.query(Character).filter(Character.anime == anime).all()
        return resul
    
    def Create_personaje(self, personaje: personaje):
        new_personaje = Character(**personaje.dict())
        self.db.add(new_personaje)
        self.db.commit()
        return
    
    def delte_personaje(self,id):
        personaje= self.db.query(Character).filter(Character.id == id).first()
        self.db.delete(personaje)
        self.db.commit()
        return
    
    def update_personaje(self,id, data: personaje):
        personaje= self.db.query(Character).filter(Character.id == id).first()
        personaje.anime = data.anime
        personaje.nombre= data.nombre
        personaje.nacimiento = data.nacimiento
        personaje.edad= data.edad
        personaje.altura= data.altura
        personaje.tipo_sangre= data.altura
        self.db.commit()
        return




    

