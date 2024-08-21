from pydantic import BaseModel, Field
from typing import Optional


class personaje(BaseModel):


    anime: str 
    nombre: str = Field(max_length=15)
    nacimiento: str
    edad: int = Field(ge=0,le=100)
    altura: str
    tipo_sangre: str = Field(max_length=1)
    interes: str

    class config:
        json_schema_extra = {
            "example":{
                "anime": "Amagami",
                "nombre": "Haruka",
                "nacimiento": "00/00/0000",
                "edad": 18,
                "altura": "169 cm",
                "tipo_sangre": "B",
                "interes": "joder" 
            }
        }




