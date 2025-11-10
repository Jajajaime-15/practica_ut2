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

def main():
    db.execute_sql("PRAGMA foreign_keys = ON;")
    # Mostrar todos
    EditorialRepository.consulta_todos()
    GeneroRepository.consulta_todos()
    AutorRepository.consulta_todos()
    LibrosRepository.consulta_todos()

    # Actualizar
    EditorialRepository.actualizar_editorial("nova","nova2")
    EditorialRepository.consulta_todos()
    GeneroRepository.actualizar_genero("fantasia","fantasia2")
    GeneroRepository.consulta_todos()
    AutorRepository.actualizar_autor("","")
    AutorRepository.consulta_todos()



    # Eliminar
    EditorialRepository.eliminar_editorial("nova2")
    EditorialRepository.consulta_todos()
    LibrosRepository.consulta_todos()


if __name__ == '__main__':
    main()