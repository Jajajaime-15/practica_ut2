import envyte # type: ignore
import libsql # type: ignore

db_url = envyte.get("DB_URL")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)

cursor = conn.cursor()

def menuTablas(): #Metodo menu tablas donde devolvemos la seleccion escrita por consola para usarla en el match
    print("------------")
    print("Tablas: Libros, Editorial, Genero y Autor")
    
    seleccion = input("¿Que tabla desea utilizar? ")

    return seleccion

def menuAcciones(): #Metodo menu acciones donde devolvemos la seleccion escrita por consola para usarla en el match
    print("------------")
    print("Acciones: Crear, Borrar, Mostrar Todos, Actualizar")
    seleccion = input("¿Que accion desea realizar? ")

    return seleccion
tabla = menuTablas() #le asginamos el valor devuelto del metodo menutablas a tabla para usarlo en el match
accion = menuAcciones() #le asginamos el valor devuelto del metodo menuAcciones a tabla para usarlo en el match


def actualizar():#Metodo actualizar
    print()

def borrar(titulo):#Metodo borrar
    print()


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
                borrar()
            case "Actualizar":   
                actualizar() 
                 
    case "Libros":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre del libro: ")
                crearLibro(nombre)
            case "Mostrar todos":  
                 MostrarTodosLibros()
            case "Borrar":
                borrar()
            case "Actualizar":   
                actualizar() 

    case "Autor":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre del autor: ")
                edad = input("Introduce la edad del autor: ")
                crearAutor(nombre,edad)
            case "Mostrar todos":  
                 MostrarTodosAutores()
            case "Borrar":
                borrar()
            case "Actualizar":   
                actualizar() 

    case "Genero":
        match accion:
            case "Crear":
                nombre = input("Introduce el nombre del genero: ")
                crearGenero(nombre)
            case "Mostrar todos":  
                 MostrarTodosGeneros()
            case "Borrar":
                borrar()
            case "Actualizar":   
                actualizar()             





conn.commit()
conn.sync()
conn.close()




