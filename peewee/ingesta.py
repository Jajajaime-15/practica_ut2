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

db.drop_tables([Libros, Editorial, Genero, Autor], safe= True)
db.create_tables([Editorial, Genero, Autor, Libros], safe= True)

editorial = [('nova'), ('egregius'), ('dykinson'), ('hidra'), ('rba')]
genero = [('fantasia'), ('ciencia ficcion'), ('policiaca'), ('ensayo'), ('horror')]
autor = [('brandon sanderson',50), ('jaime ruiz',23), ('pierce brown',37), ('rebecca kuang',30), ('vicente garrido',67)]
libros = [('el camino de los reyes',1,1,1,1100), ('analisis de la discriminacion hacia la mujer en los videojuegos',2,4,3,25), 
('juramentada',1,1,1,1300), ('nacidos de la bruma',1,1,1,650), ('la mujer en los videojuegos: desigualdad y discriminación',2,4,3,6)]

logger.info(f'Tablas tiradas y recreadas. Iniciando inserción múltiple de {len(editorial)} filas')
EditorialRepository.ingesta_multiple(editorial)
logger.info(f'Inserción múltiple completa, el número de registros es de : {Editorial.select().count()}')
logger.info(f'Iniciando inserción múltiple de {len(genero)} filas')
GeneroRepository.ingesta_multiple(genero)
logger.info(f'Inserción múltiple completa, el número de registros es de : {Genero.select().count()}')
logger.info(f'Iniciando inserción múltiple de {len(autor)} filas')
AutorRepository.ingesta_multiple(autor)
logger.info(f'Inserción múltiple completa, el número de registros es de : {Autor.select().count()}')
logger.info(f'Iniciando inserción múltiple de {len(libros)} filas')
LibrosRepository.ingesta_multiple(libros)
logger.info(f'Inserción múltiple completa, el número de registros es de : {Libros.select().count()}')