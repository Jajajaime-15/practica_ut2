from peewee import * # type: ignore
from database import db

class BaseModel(Model):
    class Meta:
        database = db