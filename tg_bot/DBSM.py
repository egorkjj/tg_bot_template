from sqlalchemy import create_engine, Column, Integer, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environs import Env

env = Env()
env.read_env(".env")
user_db = env.str("DB_USER")
passw = env.str("DB_PASSWORD")
host = env.str("DB_HOST")
name = env.str("DB_NAME")


DATABASE_URL = f"postgresql+psycopg2://{user_db}:{passw}{host}/{name}"

# Создание объекта Engine
engine = create_engine(DATABASE_URL)

# Создание базового класса для моделей
Base = declarative_base()

Base.metadata.create_all(engine)
