import envyte # type: ignore
import libsql # type: ignore

#Metodo menu tablas donde devolvemos la seleccion escrita por consola para usarla en el match
def menu_tablas(): 
    print("------------")
    print("Tablas: Libros, Editorial, Genero y Autor")
    print("Si desea salir del programa introduce [salir]")
    seleccion = input("¿Que tabla desea utilizar?\t")

    return seleccion.lower().strip()
#Metodo menu acciones donde devolvemos la seleccion escrita por consola para usarla en el match
def menu_acciones(): 
    print("------------")
    print("Acciones: Crear, Borrar, Mostrar Todos, Actualizar")
    print("Si desea regresar al menu de tablas introduce [regresar]")
    seleccion = input("¿Que accion desea realizar?\t")

    return seleccion.lower().strip()

# COMIENZO DE METODOS DE CREAR
def crear_editorial(nombre):#Metodo donde insertamos en la base de datos los datos necesarios en editorial
    id_editorial = buscar_id_editorial(nombre)
    
    if not id_editorial:
        cursor.execute('''
            INSERT INTO editorial (nombre) VALUES (?)
                ''', (nombre,))
        conn.commit()
        print("Editorial creada correctamente") 
    else: # si no se encuentra alguno indicamos que revise los datos
        print("Editorial repetida")

def crear_genero(nombre):#Metodo donde insertamos en la base de datos los datos necesarios en genero
    id_genero = buscar_id_genero(nombre)
    
    if not id_genero:
        cursor.execute('''
            INSERT INTO genero (nombre) VALUES (?)
                ''', (nombre,))
        conn.commit()
        print("Genero creado correctamente")
    else: # si no se encuentra alguno indicamos que revise los datos
        print("Genero repetido")
    
def crear_autor(nombre, edad):#Metodo donde insertamos en la base de datos los datos necesarios en autor
    id_autor = buscar_id_autor(nombre)
    
    if not id_autor:
        cursor.execute('''
            INSERT INTO autor (nombre_completo , edad) VALUES (?, ?)
                ''', (nombre,edad))
        conn.commit()
        print("Autor creado correctamente")            
    else: # si no se encuentra alguno indicamos que revise los datos
        print("Autor repetido")   

def crear_libro(titulo, nom_autor, nom_genero, nom_editorial, paginas):# Metodo donde insertamos en la base de datos los datos necesarios en libro
    cursor.execute('''SELECT titulo FROM libros WHERE titulo = ? 
                  ''', (titulo,))#Buscamos  si el titulo esta repetido
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    
    # buscamos los ids correspondientes al nombre que se introduce por teclado
    if not resultado:
        id_autor = buscar_id_autor(nom_autor)
        id_genero = buscar_id_genero(nom_genero)
        id_editorial = buscar_id_editorial(nom_editorial)

        # comprobamos que los id se encuentran
        if id_editorial and id_autor and id_genero:
            cursor.execute('''
                    INSERT INTO libros (titulo, id_autor, id_genero, id_editorial, num_pags) VALUES (?, ?, ?, ?, ?)
                        ''', (titulo, id_autor, id_genero, id_editorial, paginas))
            conn.commit()
            print("Libro creado correctamente")
        else: # si no se encuentra alguno indicamos que revise los datos
            print("Error al crear el libro, comprueba todos los campos.")
    else:
        print("Ya existe un libro con el mismo titulo")

# FIN DE METODOS DE CREAR

# COMIENZO DE METODOS DE ACTUALIZAR
def actualizar_editorial(): # actualizamos en la tabla editorial

    nombre = input("Introduce el nombre de la editorial que deseas actualizar: ").lower()
    nuevo_nombre = input("Introduce el nuevo nombre de la editorial: ").lower()

    if not nuevo_nombre:
        nuevo_nombre = nombre

    cursor.execute('''SELECT id_editorial FROM editorial WHERE nombre = ?''', (nuevo_nombre, nombre))
    resultado = cursor.fetchone()

    if not resultado:
        cursor.execute(''' UPDATE editorial SET nombre = ? WHERE nombre = ?
                    ''', (nuevo_nombre,nombre))
        conn.commit()
        print("Editorial actualizada correctamente")
    else:
        print("ERROR. Ya existe una editorial con ese nombre.")

def actualizar_libro(): # actualizamos en la tabla libro

    titulo = input("Introduce el titulo del libro que deseas actualizar: ").lower()
    nuevo_titulo = input("Introduce el nuevo titulo del libro: ").lower()
    nom_autor = input("Introduce el nombre del autor: ").lower()
    nom_genero = input("Introduce el nombre del genero: ").lower()
    nom_editorial = input("Introduce el nombre de la editorial: ").lower()
    num_pags = input("Introduce el nuevo numero de paginas del libro: ")

    if not nuevo_titulo:
        nuevo_titulo = titulo

    # buscamos los ids correspondientes al nombre que se introduce por teclado
    id_autor = buscar_id_autor(nom_autor)
    id_genero = buscar_id_genero(nom_genero)
    id_editorial = buscar_id_editorial(nom_editorial)

    # comprobamos que los id se encuentran
    if id_editorial and id_autor and id_genero:
        cursor.execute(''' UPDATE libros SET titulo = ?, id_autor = ?, id_genero = ?, id_editorial = ?, num_pags = ? WHERE titulo = ?
                    ''', (nuevo_titulo, id_autor, id_genero, id_editorial, num_pags, titulo))
        conn.commit()
        print("Libro actualizado correctamente")
    else: # si no se encuentra alguno indicamos que revise los datos
        print("Error al actualizar el libro, comprueba todos los campos.")

def actualizar_autor(id_autor, nombre, edad): # actualizamos en la tabla autor
    cursor.execute('''SELECT id_autor FROM autor WHERE nombre = ?''', (nombre,))
    resultado = cursor.fetchone()
    if not resultado:
        cursor.execute('''UPDATE autor SET nombre = ?, edad = ? WHERE id_autor = ?
                    ''', (nombre, edad, id_autor))
        conn.commit()
        print("Autor actualizado correctamente")
    else:
        print("ERROR. Ya existe un autor con ese nombre.")

def actualizar_genero(id_genero, nombre): # actualizamos en la tabla genero
    cursor.execute('''SELECT id_genero FROM genero WHERE nombre = ?''', (nombre,))
    resultado = cursor.fetchone()
    if not resultado:
        cursor.execute('''
                    UPDATE genero SET nombre = ? WHERE id_genero = ?
                    ''', (nombre, id_genero))
        conn.commit()
        print("Genero actualizado correctamente")
    else:
        print("ERROR. Ya existe un genero con ese nombre.")
# FIN DE METODOS DE ACTUALIZAR

# COMIENZO DE METODOS DE BORRAR
def borrar_editorial(id_editorial): # eliminamos informacion de la tabla editorial 
    cursor.execute('''SELECT * FROM editorial WHERE id_editorial = ?''', (id_editorial,))
    resultado = cursor.fetchone()
    if resultado:
        cursor.execute('''DELETE FROM editorial WHERE id_editorial = ?
                    ''', (id_editorial,))
        conn.commit()
        print("Editorial borrada correctamente")
    else:
        print("ERROR. No hay ninguna editorial con ese ID.")

def borrar_libro(titulo): # eliminamos informacion de la tabla libros
    cursor.execute('''SELECT * FROM libros WHERE titulo = ?''', (titulo,))
    resultado = cursor.fetchone()
    if resultado:
        cursor.execute('''DELETE FROM libros WHERE id_libro = ?
                    ''', (titulo,))
        conn.commit()
        print("Libro borrado correctamente")
    else:
        print("ERROR. No existe ningun libro con este titulo.")

def borrar_autor(id_autor): # eliminamos informacion de la tabla autor
    cursor.execute('''SELECT * FROM autor WHERE id_autor = ?''', (id_autor,))
    resultado = cursor.fetchone()
    if resultado:
        cursor.execute('''DELETE FROM autor WHERE id_autor = ?
                    ''', (id_autor,))
        conn.commit()
        print("Autor borrado correctamente")
    else:
        print("ERROR. No existe ningun autor con ese ID.")

def borrar_genero(id_genero): # eliminamos informacion de la tabla genero
    cursor.execute('''SELECT * FROM genero WHERE id_genero = ?''', (id_genero,))
    resultado = cursor.fetchone()
    if resultado:
        cursor.execute('''DELETE FROM genero WHERE id_genero = ?
                    ''', (id_genero,))
        conn.commit()
        print("Genero borrado correctamente")
    else:
        print("ERROR. No existe ningun genero con ese ID.")
# FIN DE METODOS DE BORRAR

# COMIENZO DE METODOS DE MOSTRAR TODOS
def mostrar_todos_editorial():
    cursor.execute("SELECT * FROM editorial")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)

def mostrar_todos_libros():
    cursor.execute("SELECT * FROM libros")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)     

def mostrar_todos_autores():
    cursor.execute("SELECT * FROM autor")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)       

def mostrar_todos_generos():
    cursor.execute("SELECT * FROM genero")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)                    
# FIN DE METODOS DE MOSTRAR TODOS

# COMIENZO DE METODOS DE BUSCAR IDS
def buscar_id_autor(nombre):
    # buscamos el id del autor donde el nombre introducido coincida con el nombre en la tabla de autores
    cursor.execute(''' SELECT id_autor FROM autor WHERE nombre_completo = ?
                   ''', (nombre,))
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    if resultado != None: # comprobamos si hay resultado de la consulta y lo devolvemos
        return resultado[0]
    else:
        print(f"Autor {nombre} no encontrado en la base de datos. Debes darlo de alta primero.")
        return None
    
def buscar_id_genero(nombre):
    # buscamos el id del genero donde el nombre introducido coincida con el nombre en la tabla de genero
    cursor.execute('''SELECT id_genero FROM genero WHERE nombre = ?
                   ''', (nombre,))
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    if resultado: # comprobamos si hay resultado de la consulta y lo devolvemos
        return resultado[0]
    else:
        print(f"Genero {nombre} no encontrado en la base de datos. Debes crearlo primero.")
        return None

def buscar_id_editorial(nombre):
    # buscamos el id de la editorial donde el nombre introducido coincida con el nombre en la tabla de editorial
    cursor.execute('''SELECT id_editorial FROM editorial WHERE nombre = ?
                   ''', (nombre,))
    resultado = cursor.fetchone() # guardamos el resultado de la consulta en una variable
    if resultado: # comprobamos si hay resultado de la consulta y lo devolvemos
        return resultado[0]
    else:
        print(f"Editorial {nombre} no encontrado en la base de datos. Debes crearlo primero.")
        return None
# FIN DE METODOS DE BUSCAR IDS


if __name__ == "__main__":
    db_url = envyte.get("DB_URL")
    auth_token = envyte.get("API_TOKEN")

    conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)
    cursor = conn.cursor()

    while True:
        tabla = menu_tablas() # le asignamos el valor devuelto del metodo menu tablas para usarlo en el match
        match tabla:
            case "editorial":
                accion = menu_acciones() # le asignamos el valor devuelto del metodo menu acciones para usarlo en el match
                match accion:
                    case "crear":
                        nombre = input("Introduce el nombre de la editorial: ").lower()
                        crear_editorial(nombre)
                    case "mostrar todos":  
                        mostrar_todos_editorial()
                    case "borrar":
                        id_editorial = input("Introduce el ID de la editorial que deseas borrar: ").lower()
                        borrar_editorial(id_editorial)
                    case "actualizar":
                        actualizar_editorial() 
                    case "regresar":
                        continue
                    case _:
                        print("Error. Selecciona una opcion valida [crear, mostrar todos, borrar, actualizar]")
            case "libros":
                accion = menu_acciones()
                match accion:
                    case "crear":
                        titulo = input("Introduce el titulo del libro que deseas crear: ").lower()
                        nom_autor = input("Introduce el nombre del autor: ").lower()
                        nom_genero = input("Introduce el nombre del genero: ").lower()
                        nom_editorial = input("Introduce el nombre de la editorial: ").lower()
                        paginas = input("Introduce el numero de paginas del libro: ")
                        crear_libro(titulo,nom_autor,nom_genero,nom_editorial,paginas)
                    case "mostrar todos":  
                        mostrar_todos_libros()
                    case "borrar":
                        titulo = input("Introduce el titulo del libro que deseas borrar: ").lower()
                        borrar_libro(titulo)
                    case "actualizar":   
                        actualizar_libro() 
                    case "regresar":
                        continue
                    case _:
                        print("Error. Selecciona una opcion valida [crear, mostrar todos, borrar, actualizar]")
            case "autor":
                accion = menu_acciones()
                match accion:
                    case "crear":
                        nombre = input("Introduce el nombre del autor: ").lower()
                        edad = input("Introduce la edad del autor: ")
                        crear_autor(nombre,edad)
                    case "mostrar todos":  
                        mostrar_todos_autores()
                    case "borrar":
                        id_autor = input("Introduce el ID del autor que deseas eliminar: ").lower()
                        borrar_autor(id_autor)
                    case "actualizar":
                        id_autor = input("Introduce el ID del autor que deseas actualizar: ").lower()
                        nombre = input("Introduce el nuevo nombre del autor: ").lower()
                        edad = input("Introduce la nueva edad del autor: ")
                        actualizar_autor(id_autor, nombre, edad)
                    case "regresar":
                        continue
                    case _:
                        print("Error. Selecciona una opcion valida [crear, mostrar todos, borrar, actualizar]")
            case "genero":
                accion = menu_acciones()
                match accion:
                    case "crear":
                        nombre = input("Introduce el nombre del genero: ").lower()
                        crear_genero(nombre)
                    case "mostrar todos":  
                        mostrar_todos_generos()
                    case "borrar":
                        id_genero = input("Introduce el ID del genero que deseas eliminar: ").lower()
                        borrar_genero(id_genero)
                    case "actualizar":
                        id_genero = input("Introduce el ID del genero que deseas actualizar: ").lower()
                        nombre = input("Introduce el nuevo nombre del genero: ").lower()
                        actualizar_genero(id_genero, nombre) 
                    case "regresar":
                        continue
                    case _:
                        print("Error. Selecciona una opcion valida [crear, mostrar todos, borrar, actualizar, regresar]")
            case "salir":
                break
            case _:
                print("Error. Selecciona una opcion valida [libros, editorial, autor, genero, salir]")


conn.commit()
conn.sync()
conn.close()