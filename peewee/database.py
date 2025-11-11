from peewee import * # type: ignore
import logging
from pathlib import Path

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "libros.db"

if not DB_PATH.exists():
    logger.error(f"La base de datos {DB_PATH} no existe, se creará al conectar")
else:
    logger.info(f"Conectando con la base de datos {DB_PATH}")

db = SqliteDatabase(DB_PATH) #, pragmas={'foreign_keys': 1} #no se si esto funciona y se puede anyadir, segun la documentacion esto arregla los on delete