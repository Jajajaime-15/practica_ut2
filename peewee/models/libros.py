from peewee import * # type: ignore
from database import db
from base_model import BaseModel
from editorial import Editorial
from genero import Genero
from autor import Autor

class Libros(BaseModel):
    titulo = TextField(primary_key=True)
    nPaginas = IntegerField()
    id_editorial = ForeignKeyField(Editorial, backref="editorial", on_delete="set null", on_update="cascade")
    id_genero = ForeignKeyField(Genero, backref="genero", on_delete="set null", on_update="cascade")
    id_autor = ForeignKeyField(Autor, backref="autor", on_delete="set null", on_update="cascade")