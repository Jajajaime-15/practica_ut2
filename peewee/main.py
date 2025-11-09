from peewee import * # type: ignore
from models.libros import Libros
from models.editorial import Editorial
from models.genero import Genero
from models.autor import Autor
from repositories.editorial_repo import EditorialRepository
from repositories.genero_repo import GeneroRepository
from repositories.autor_repo import AutorRepository
from repositories.libros_repo import LibrosRepository 

def main():
    EditorialRepository.consulta_todos()


if __name__ == '__main__':
    main()