import envyte # type: ignore
import libsql # type: ignore

db_url = envyte.get("DB_URL")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)

cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS editorial (
                    id_editorial INTEGER PRIMARY KEY,
                    nombre TEXT
                )
                ''')
cursor.execute('''
                CREATE TABLE IF NOT EXISTS genero (
                    id_genero INTEGER PRIMARY KEY,
                    nombre TEXT
                )
                ''')
cursor.execute('''
                CREATE TABLE IF NOT EXISTS autor (
                    id_autor INTEGER PRIMARY KEY,
                    nombre TEXT,
                    apellido TEXT,
                    edad INTEGER
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
cursor.execute("INSERT INTO ")
conn.commit()
conn.sync()
conn.close()