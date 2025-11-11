from peewee import * # type: ignore
from database import db, logger
from models.libros import Libros
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Autor
from repositories.editorial_repo import EditorialRepository
from repositories.genero_repo import GeneroRepository
from repositories.autor_repo import AutorRepository
from repositories.libros_repo import LibrosRepository 

def mostrar():
    # Mostrar todos
    EditorialRepository.consulta_todos()
    GeneroRepository.consulta_todos()
    AutorRepository.consulta_todos()
    LibrosRepository.consulta_todos()

def actualizar():
    # Actualizar
    EditorialRepository.actualizar_editorial("nova","nova2")
    EditorialRepository.consulta_todos()
    GeneroRepository.actualizar_genero("fantasia","fantasia2")
    GeneroRepository.consulta_todos()
    AutorRepository.actualizar_autor("jaime ruiz","JAIME RUIZ")
    AutorRepository.consulta_todos()
    LibrosRepository.actualizar_libro("juramentada","juramentada2")
    LibrosRepository.consulta_todos()

def eliminar():
    # Eliminar
    EditorialRepository.eliminar_editorial("nova2")
    EditorialRepository.consulta_todos()
    GeneroRepository.eliminar_genero("fantasia2")
    GeneroRepository.consulta_todos()
    AutorRepository.eliminar_autor("JAIME RUIZ")
    AutorRepository.consulta_todos()
    LibrosRepository.eliminar_libro("juramentada2")
    LibrosRepository.consulta_todos()

def consultas():
    query1 = Autor.select(Autor.nombre, Autor.edad).order_by(Autor.edad.desc())
    for autor in query1.dicts():
        logger.info(autor)
    
    query2 = Libros.select(Libros.titulo, Autor.nombre.alias('autor'), Autor.edad).join(Autor).where(Autor.edad < 30)
    for libro in query2.dicts():
        logger.info(libro)
        
    logger.info("---------")
    # el switch entre join a veces funciona, en este caso no PORQUE NO TENIA ALIAS
    # tambien se puede hacer join(Tabla, on=(Tabla.dato == Tabla2.dato2))
    # en este caso pruebo con join_from
    # los parentesis en la query permiten que pueda espaciarlo en lineas distintas
    # IMPORTANTE QUE NO SALIAN AMBOS ELEMENTOS DEBIDO A QUE SE LLAMAN IGUAL, POR LO QUE TENIA QUE PONERLES ALIAS
    # CON SWITCH: query3 = (Libros.select(Editorial.nombre.alias('Editorial'), Genero.nombre.alias('Genero')).join(Editorial).switch(Libros).join(Genero).group_by(Genero.nombre).order_by(fn.COUNT(Genero.nombre).desc()).limit(1))
    query3 = (Libros.select(Editorial.nombre.alias('Editorial'), Genero.nombre.alias('Genero')).join_from(Libros, Editorial).join_from(Libros, Genero)
              .group_by(Genero.nombre).order_by(fn.COUNT(Genero.nombre).desc()).limit(1))
    for editorial in query3.dicts():
        logger.info(editorial)

def main():
    #db.execute_sql("PRAGMA foreign_keys = ON;") #funciona con esto tmb pero cuidado porque a veces va raro
    #mostrar()
    #actualizar()
    #eliminar()
    consultas()


if __name__ == '__main__':
    main()