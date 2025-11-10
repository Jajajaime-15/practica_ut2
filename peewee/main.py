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

def main():
    #db.execute_sql("PRAGMA foreign_keys = ON;") #funciona con esto tmb pero cuidado porque a veces va raro
    mostrar()
    actualizar()
    eliminar()


if __name__ == '__main__':
    main()