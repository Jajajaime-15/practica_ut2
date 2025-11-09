from peewee import * # type: ignore
from database import db
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Autor
from models.base_model import BaseModel

class Libros(BaseModel):
    titulo = TextField(primary_key=True)
    n_paginas = IntegerField()
    id_editorial = ForeignKeyField(Editorial, backref="editorial", on_delete="set null", on_update="cascade")
    id_genero = ForeignKeyField(Genero, backref="genero", on_delete="set null", on_update="cascade")
    id_autor = ForeignKeyField(Autor, backref="autor", on_delete="set null", on_update="cascade")