from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from faker import Faker 
import ipdb

if __name__ == '__main__':

    engine = create_engine("sqlite:///main.db")
    Session = sessionmaker(bind=engine)
    session = Session()


    print("Seeding DB...")

    # Reset DB
    session.query(Garden).delete()
    session.query(Vegetable).delete()
    
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
    # doctors = [
    #     Doctor(first_name="John", last_name="Smith", speciality="Cardiologist"),
    #     Doctor(first_name="Andy", last_name="Adkins", speciality="Pediatrics"),
    #     Doctor(first_name="Samantha", last_name="Urban", speciality="Dermatology")
    # ]

ipdb.set_trace()
   
session.commit()
  
