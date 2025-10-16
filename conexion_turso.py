import envyte # type: ignore
import libsql # type: ignore

db_url = envyte.get("DB_URL")
auth_token = envyte.get("API_TOKEN")

conn = libsql.connect("practicaut2",sync_url = db_url, auth_token = auth_token)

cursor = conn.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS prueba (
                    col1 INTEGER PRIMARY KEY,
                    col2 TEXT NOT NULL,
                    col3 TEXT NOT NULL
                )
                ''')
# julio estuvo aqui
cursor.execute('''INSERT INTO prueba (col2, col3) VALUES ('valorPrueba1','valorPrueba2')''')
# alba está probando
conn.commit()
conn.sync()


conn.close()