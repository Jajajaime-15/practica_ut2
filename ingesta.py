import envyte # type: ignore
import libsql # type: ignore

db_url = envyte.get("DB_URL")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)

cursor = conn.cursor()

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
cursor.execute('''
                CREATE TABLE IF NOT EXISTS libros (
                    titulo TEXT PRIMARY KEY,
                    id_autor INTEGER NOT NULL,
                    id_genero INTEGER NOT NULL,
                    id_editorial INTEGER NOT NULL,
                    num_pags INTEGER NOT NULL,
                    FOREIGN KEY (id_autor) REFERENCES autor (id_autor), 
                    FOREIGN KEY (id_genero) REFERENCES genero (id_genero), 
                    FOREIGN KEY (id_editorial) REFERENCES editorial (id_editorial)
                )
                ''')


cursor.execute('''
                INSERT INTO editorial VALUES ('Nova'), ('Egregius'), ('Dykinson'), ('Hidra'), ('RBA')
                ''')
cursor.execute('''
                INSERT INTO autor (nombre, apellido, edad) 
                VALUES ('Brandon','Sanderson','50'), ('Jaime','Ruiz','23'), ('Pierce','Brown','37'), 
                    ('Rebecca','Kuang','30'), ('Vicente','Garrido','67')
                ''')
cursor.execute('''
                INSERT INTO genero VALUES ('Fantasia'), ('Ciencia Ficcion'), ('Policiaca'), ('Ensayo'), ('Horror')
                ''')
cursor.execute('''
                INSERT INTO libros (titulo, id_autor, id_genero, id_editorial, num_pags) 
                VALUES ('El Camino de los Reyes',1,1,1,1100), ('Analisis de la discriminacion hacia la mujer en los videojuegos',2,4,3,25), 
                (Juramentada',1,1,1,1300), ('Nacidos de la Bruma',1,1,1,650), ('La mujer en los videojuegos: desigualdad y discriminación',2,4,3,6)
                ''')

conn.commit()
conn.sync()
conn.close()