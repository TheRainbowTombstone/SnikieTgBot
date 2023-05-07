from aiogram import types
from gino import Gino

from sqlalchemy import (Column, Integer, BigInteger, String, Sequence)
from sqlalchemy import sql
from gino.schema import GinoSchemaVisitor

from tgbot.config import load_config

config = load_config(".env")

db = Gino()

class User(db.Model):
    __tabelname__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(BigInteger)
    fullname = Column(String(100))
    username = Column(String(50))

    query: sql.Select

class Task(db.Model):
    __tabelname__ = "tasks"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    task = Column(String(300))
    deadline = Column(String(20))

class DBComands():
    async def showTask(self):
        tasks = await Task.query.gino.all()
        return tasks


async def create_db():
    await db.set_bind(f"postgresql://{config.db.user}:{config.db.password}@{config.db.host}/snikuser")
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()
