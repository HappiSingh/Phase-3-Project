
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
import ipdb

ipdb.set_trace()

Base = declarative_base()

"""
class Garden
id: int PK
name: str 
location: str
size: str

class Vegtables
id: int PK
veg name: str
quanity: int
ripe level: str
Garden_id: int FK
"""

class Garden(Base):
    __tablename__ = "gardens"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    size = Column(String, nullable=False)
    
    vegetables = relationship("Garden", backref=("gardens"))


    def __repr__(self):
       return f"<Garden {self.id} {self.name} {self.location} {self.size}>"

    
        
class Vegetable(Base):
    __tablename__ = "vegetables"

    id = Column(Integer, primary_key=True)
    veg_name = Column(String, nullable=False)
    quanity = Column(Integer, nullable=False)
    ripeness = Column(String, unique=True)

    garden_id = Column(Integer, ForeignKey("gardens.id"))


    def __repr__(self):
        return f"<Vegetable {self.id} {self.veg_name} {self.quanity} {self.ripeness}>"
    