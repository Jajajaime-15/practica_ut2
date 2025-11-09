from peewee import * # type: ignore
from database import db
from models.base_model import BaseModel

class Genero(BaseModel):
    id_genero = AutoField()
    nombre = TextField(unique=True)