import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:postgre@localhost:5432/inlove', echo=True)

Session = sessionmaker(bind=engine)


# підключення до бази даних
conn = psycopg2.connect(database="inlove", user="postgres", password="postgre", host="localhost")