import envyte # type: ignore
import libsql # type: ignore

db_url = envyte.get("DB_URL")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)

cursor = conn.cursor()

# Eliminamos las tablas cada vez que se realiza la ingesta, comenzando por libros para que no haya problemas con las FK
cursor.execute('''DROP TABLE IF EXISTS libros''')
cursor.execute('''DROP TABLE IF EXISTS editorial''')
cursor.execute('''DROP TABLE IF EXISTS genero''')
cursor.execute('''DROP TABLE IF EXISTS autor''')

# Crearemos las tablas, siendo la ultima la de libros para poder realizar las referencias directamente al crear la tabla
cursor.execute('''
                CREATE TABLE IF NOT EXISTS editorial (
                    id_editorial INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
                ''')
cursor.execute('''
                CREATE TABLE IF NOT EXISTS genero (
                    id_genero INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
                ''')
cursor.execute('''
                CREATE TABLE IF NOT EXISTS autor (
                    id_autor INTEGER PRIMARY KEY,
                    nombre_completo TEXT NOT NULL,
                    edad INTEGER NOT NULL
                )
                ''')
# Queremos poder poner los libros sin referenciar ningun genero, ni editorial ni autor, en caso de que sean desconocidos
# Ademas, asi podremos permitir el set null al borrar de las otras tablas, en vez de borrar el libro entero
# La actualizacion si la haremos en cascada
cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    titulo TEXT PRIMARY KEY,
                    id_autor INTEGER, 
                    id_genero INTEGER,
                    id_editorial INTEGER,
                    num_pags INTEGER NOT NULL,
                    FOREIGN KEY (id_autor) REFERENCES autor (id_autor) ON DELETE SET NULL ON UPDATE CASCADE, 
                    FOREIGN KEY (id_genero) REFERENCES genero (id_genero) ON DELETE SET NULL ON UPDATE CASCADE, 
                    FOREIGN KEY (id_editorial) REFERENCES editorial (id_editorial) ON DELETE SET NULL ON UPDATE CASCADE
                )
                ''')

# Realizamos las inserciones de datos para tener varios valores en las tablas nada mas realizar la ingesta
cursor.execute('''
                INSERT INTO editorial (nombre) VALUES ('Nova'), ('Egregius'), ('Dykinson'), ('Hidra'), ('RBA')
                ''')
cursor.execute('''
                INSERT INTO autor (nombre_completo, edad) 
                VALUES ('Brandon Sanderson','50'), ('Jaime Ruiz','23'), ('Pierce Brown','37'), 
                    ('Rebecca Kuang','30'), ('Vicente Garrido','67')
                ''')
cursor.execute('''
                INSERT INTO genero(nombre) VALUES ('Fantasia'), ('Ciencia Ficcion'), ('Policiaca'), ('Ensayo'), ('Horror')
                ''')
cursor.execute('''
                INSERT INTO libros (titulo, id_autor, id_genero, id_editorial, num_pags) 
                VALUES ('El Camino de los Reyes',1,1,1,1100), ('Analisis de la discriminacion hacia la mujer en los videojuegos',2,4,3,25), 
                ('Juramentada',1,1,1,1300), ('Nacidos de la Bruma',1,1,1,650), ('La mujer en los videojuegos: desigualdad y discriminación',2,4,3,6)
                ''')

# Validamos los cambios, los sincronizamos con turso y cerramos el conector
conn.commit()
conn.sync()
conn.close()