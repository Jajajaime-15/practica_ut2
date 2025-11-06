from database import db, logger
from peewee import * # type: ignore
from models.libros import Libros
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Autor
from repositories.editorial_repo import EditorialRepository
from repositories.genero_repo import GeneroRepository
from repositories.autor_repo import AutorRepository
from repositories.libros_repo import LibrosRepository 

db.execute_sql("PRAGMA foreign_keys = ON;")

db.drop_tables([Libros], [Editorial], [Genero], [Autor], safe= True)
db.create_tables([Editorial], [Genero], [Autor], [Libros], safe= True)


editorial = []
genero = []
autor = []
libros = []

logger.info(f'Tablas tiradas y recreadas. Iniciando inserción múltiple de {len(editorial)} filas')
EditorialRepository.ingesta_multiple()
logger.info(f'Inserción múltiple completa, el número de registros es de : {Editorial.select().count()}')
logger.info(f'Tablas tiradas y recreadas. Iniciando inserción múltiple de {len(genero)} filas')
GeneroRepository.ingesta_multiple()
logger.info(f'Inserción múltiple completa, el número de registros es de : {Genero.select().count()}')
logger.info(f'Tablas tiradas y recreadas. Iniciando inserción múltiple de {len(autor)} filas')
AutorRepository.ingesta_multiple()
logger.info(f'Inserción múltiple completa, el número de registros es de : {Autor.select().count()}')
logger.info(f'Tablas tiradas y recreadas. Iniciando inserción múltiple de {len(libros)} filas')
LibrosRepository.ingesta_multiple()
logger.info(f'Inserción múltiple completa, el número de registros es de : {Libros.select().count()}')

