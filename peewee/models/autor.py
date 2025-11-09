from peewee import * # type: ignore
from database import db
from models.base_model import BaseModel

class Autor(BaseModel):
    id_autor = AutoField()
    nombre = TextField(unique=True)
    edad = IntegerField(constraints=[Check("edad > 0")], null=True) # permitimos edad nula en el caso de autores fallecidos