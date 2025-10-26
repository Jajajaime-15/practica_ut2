import envyte # type: ignore
import libsql # type: ignore

db_url = envyte.get("DB_URL")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)

cursor = conn.cursor()

#Metodo menu tablas donde devolvemos la seleccion escrita por consola para usarla en el match
def menuTablas(): 
    print("------------")
    print("Tablas: Libros, Editorial, Genero y Autor")
    
    seleccion = input("¿Que tabla desea utilizar? ")

    return seleccion
#Metodo menu acciones donde devolvemos la seleccion escrita por consola para usarla en el match
def menuAcciones(): 
    print("------------")
    print("Acciones: Crear, Borrar, Mostrar Todos, Actualizar")
    seleccion = input("¿Que accion desea realizar? ")

    return seleccion

tabla = menuTablas() #le asginamos el valor devuelto del metodo menutablas a tabla para usarlo en el match
accion = menuAcciones() #le asginamos el valor devuelto del metodo menuAcciones a tabla para usarlo en el match

# METODOS PARA BUSCAR POR NOMBRE LOS IDS

def buscarId_autor(nombre):
    # buscamos el id del autor donde el nombre introducido coincida con el nombre en la tabla de autores
    cursor.execute(''' SELECT id_autor FROM autor WHERE nombre = ?
                   ''', (nombre,))
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    if resultado: # comprobamos si hay resultado de la consulta y lo devolvemos
        return resultado[0]
    else:
        print(f"Autor {nombre} no encontrado en la base de datos")
        return None
    
def buscarId_genero (nombre):
    # buscamos el id del genero donde el nombre introducido coincida con el nombre en la tabla de genero
    cursor.execute('''SELECT id_genero FROM genero WHERE nombre = ?
                   ''', (nombre,))
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    if resultado: # comprobamos si hay resultado de la consulta y lo devolvemos
        return resultado[0]
    else:
        print(f"Genero {nombre} no encontrado en la base de datos")
        return None

def buscarId_editorial (nombre):
    # buscamos el id de la editorial donde el nombre introducido coincida con el nombre en la tabla de editorial
    cursor.execute('''SELECT id_editoral FROM editorial WHERE nombre = ?
                   ''', (nombre,))
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    if resultado: # comprobamos si hay resultado de la consulta y lo devolvemos
        return resultado[0]
    else:
        print(f"Editorial {nombre} no encontrado en la base de datos")
        return None

# METODOS PARA ACTUALIZAR DATOS DE LAS TABLAS DE LA BBDD

def actualizarEditorial (id_editorial,nombre): # actualizamos en la tabla editorial
    cursor.execute(''' UPDATE editorial SET nombre = ? WHERE id_editorial = ?
                   ''', (nombre, id_editorial))
    conn.commit()
    print("Editorial actualizada correctamente")

def actualizarLibro (titulo, nuevo_titulo, id_autor, id_genero, id_editorial, paginas): # actualizamos en la tabla libro
    if not nuevo_titulo:
        nuevo_titulo = titulo

    # buscamos los ids correspondientes al nombre que se introduce por teclado
    id_autor = buscarId_autor(nombre)
    id_genero = buscarId_genero(nombre)
    id_editorial = buscarId_editorial(nombre)

    # comprobamos que los id se encuentran
    if id_editorial and id_autor and id_genero:
        cursor.execute(''' UPDATE libros SET titulo = ?, id_autor = ?, id_genero = ?, id_editorial = ?, paginas = ? WHERE titulo = ?
                    ''', (nuevo_titulo, id_autor, id_genero, id_editorial, paginas, titulo))
        conn.commit()
        print("Libro actualizado correctamente")
    else: # si no se encuentra alguno indicamos que revise los datos
        print("Error al actualizar el libro, comprueba todos los campos.")

def actualizarAutor (id_autor, nombre, edad): # actualizamos en la tabla autor
    cursor.execute('''UPDATE autor SET nombre = ?, edad = ? WHERE id_autor = ?
                   ''', (nombre, edad, id_autor))
    conn.commit()
    print("Autor actualizado correctamente")

def actualizarGenero(id_genero, nombre): # actualizamos en la tabla genero
    cursor.execute('''
                   UPTDATE genero SET nombre = ? WHERE id_genero = ?
                   ''', (nombre, id_genero))
    conn.commit()
    print("Genero actualizado correctamente")

# METODOS PARA ELIMINAR DATOS DE LAS TABLAS DE LA BBDD

def borrarEditorial(id_editorial): # eliminamos informacion de la tabla editorial 
    cursor.execute('''DELETE FROM editorial WHERE id_editorial = ?
                   ''', (id_editorial,))
    conn.commit()
    print("Editorial borrada correctamente")

def borrarLibro(titulo): # eliminamos informacion de la tabla libros
    cursor.execute('''DELETE FROM libros WHERE id_libro = ?
                   ''', (titulo,))
    conn.commit()
    print("Libro borrado correctamente")

def borrarAutor(id_autor): # eliminamos informacion de la tabla autor
    cursor.execute('''DELETE FROM autor WHERE id_autor = ?
                   ''', (id_autor,))
    conn.commit()
    print("Autor borrado correctamente")

def borrarGenero(id_genero): # eliminamos informacion de la tabla genero
    cursor.execute('''DELETE FROM genero WHERE id_genero = ?
                   ''', (id_genero,))
    conn.commit()
    print("Genero borrado correctamente")


def crearEditorial(nombre):#Metodo donde insertamos en la base de datos los datos necesarios en editorial
    cursor.execute('''
                INSERT INTO editorial (nombre) VALUES (?)
                    ''', (nombre,))
    
    conn.commit()


def crearGenero(nombre):#Metodo donde insertamos en la base de datos los datos necesarios en editorial
    cursor.execute('''
                INSERT INTO genero (nombre) VALUES (?)
                    ''', (nombre,))
    
    conn.commit()    

def crearAutor(nombre, edad):#Metodo donde insertamos en la base de datos los datos necesarios en editorial
    cursor.execute('''
                INSERT INTO autor (nombre_completo , edad) VALUES (?, ?)
                    ''', (nombre,edad,))
    
    conn.commit()        

def crearLibro(titulo, id_autor, id_genero, id_editorial, paginas):#Metodo donde insertamos en la base de datos los datos necesarios en editorial
    cursor.execute('''
                INSERT INTO libros (nombre) VALUES (?)
                    ''', (nombre,))
    #HAY QUE TERMINARLO TODAVIA
    conn.commit()            

def MostrarTodosEditorial():
    cursor.execute("Select * FROM editorial")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)

def MostrarTodosLibros():
    cursor.execute("Select * FROM libros")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)     

def MostrarTodosAutores():
    cursor.execute("Select * FROM autor")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)       

def MostrarTodosGeneros():
    cursor.execute("Select * FROM genero")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)                    


match tabla:
    case "Editorial":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre de la editorial: ")
                crearEditorial(nombre)
            case "Mostrar todos":  
                 MostrarTodosEditorial()
            case "Borrar":
                id_editorial = input("Introduce el ID de la editorial que deseas borrar: ")
                borrarEditorial(id_editorial)
            case "Actualizar":
                id_editorial = input("Introduce el ID de la editorial que deseas actualizar: ") 
                nombre = input("Introduce el nuevo nombre de la editorial: ")
                actualizarEditorial(id_editorial, nombre) 
                 
    case "Libros":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre del libro: ")
                crearLibro(nombre)
            case "Mostrar todos":  
                 MostrarTodosLibros()
            case "Borrar":
                titulo = input("Introduce el titulo del libro que deseas borrar: ")
                borrarLibro(titulo)
            case "Actualizar":   
                titulo = input("Introduce el titulo del libro que deseas actualizar: ")
                nuevo_titulo = input("Introduce el nuevo titulo del libro: ")
                id_autor = input("Introduce el nuevo ID del autor: ")
                id_genero = input("Introduce el nuevo ID del genero: ")
                id_editorial = input("Introduce el nuevo ID de la editorial: ")
                paginas = input("Introduce el nuevo numero de paginas del libro: ")
                actualizarEditorial(titulo,nuevo_titulo, id_autor, id_genero, id_editorial, paginas) 

    case "Autor":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre del autor: ")
                edad = input("Introduce la edad del autor: ")
                crearAutor(nombre,edad)
            case "Mostrar todos":  
                 MostrarTodosAutores()
            case "Borrar":
                id_autor = input("Introduce el ID del autor que deseas eliminar: ")
                borrarAutor(id_autor)
            case "Actualizar":
                id_autor = input("Introduce el ID del autor que deseas actualizar: ") 
                nombre = input("Introduce el nuevo nombre del autor: ")
                edad = input("Introduce la nueva edad del autor: ")
                actualizarAutor(id_autor, nombre, edad) 

    case "Genero":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre del genero: ")
                crearGenero(nombre)
            case "Mostrar todos":  
                 MostrarTodosGeneros()
            case "Borrar":
                id_genero = input("Introduce el ID del genero que deseas eliminar: ")
                borrarGenero(id_genero)
            case "Actualizar":   
                id_genero = input("Introduce el ID del genero que deseas actualizar: ")
                nombre = input("Introduce el nuevo nombre del genero: ")
                actualizarGenero(id_genero, nombre)             





conn.commit()
conn.sync()
conn.close()




