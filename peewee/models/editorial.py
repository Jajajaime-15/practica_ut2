from peewee import * # type: ignore
from database import db
from models.base_model import BaseModel

class Editorial(BaseModel):
    id_editorial = AutoField()
    nombre = TextField(unique=True)