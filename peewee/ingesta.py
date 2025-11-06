from database import db, logger
from peewee import * # type: ignore
from models.libros import Libros
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Autor

db.execute_sql("PRAGMA foreign_keys = ON;")

db.drop_tables([Libros], [Editorial], [Genero], [Autor], safe= True)
db.create_tables([Editorial], [Genero], [Autor], [Libros], safe= True)



