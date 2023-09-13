from sqlalchemy import Column, Integer, String, Float, ForeignKey, SmallInteger
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nik_name = Column(String(length=255), nullable=False, unique=True)
    hashed_password = Column(String(length=255), nullable=False)
    salt = Column(String(length=255), nullable=False)
    email = Column(String(length=50), nullable=False, unique=True)