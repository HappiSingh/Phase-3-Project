from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

#change the class name
class Table(Base):
    # add the table name 
    __tablename__ = ""

    id = Column("id", Integer, primary_key=True)
    name = Column("", String(50))

