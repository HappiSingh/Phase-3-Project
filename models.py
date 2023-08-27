
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
# import ipdb

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


"""
Garden Manager 

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
    
    vegetables = relationship("Vegetable", backref="gardens")


    def __repr__(self):
       return (
           f"<Garden: id={self.id},\n"
           f"         name='{self.name}',\n"
           f"         location='{self.location}',\n"
           f"         size='{self.size}'>\n\n"
       )
    
    @classmethod
    def query_g1(cls, name):
        g1 = session.query(cls).filter(cls.name == name).first()
        return g1.vegetables
    
    @classmethod
    def get_garden_id(cls, name):
        g2 = session.query(cls).filter(cls.name == name).first()
        return g2.id



class Vegetable(Base):
    __tablename__ = "vegetables"

    id = Column(Integer, primary_key=True)
    veg_name = Column(String, nullable=False)
    quanity = Column(Integer, nullable=False)
    ripeness = Column(String, nullable=False)

    garden_id = Column(Integer, ForeignKey("gardens.id"))


    def __repr__(self):
       return (
           f"<Vegetable: id={self.id},\n"
           f"            veg_name='{self.veg_name}',\n"
           f"            quanity='{self.quanity}',\n"
           f"            ripeness='{self.ripeness}'>\n\n"
       )


    @classmethod
    def add_veg(cls, name, quanity, ripeness, g2):
        new_veg = Vegetable(veg_name=name, quanity=quanity, ripeness=ripeness, garden_id=g2)
        session.add(new_veg)
        session.commit()

        return new_veg