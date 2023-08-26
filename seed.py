from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
# from faker import Faker 
# import ipdb

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
ripeness: str
Garden_id: int FK
"""
gardens = [
    Garden(name="Greenwood Garden", location="New Jersey", size="8,000 sqft"),
    Garden(name=" West Side Community Garden", location="New York", size="6,000 sqft"),
    Garden(name="Duke Farms Community Garden", location="New Jersey", size="5,000 sqft")
]

session.bulk_save_objects(gardens)

db_gardens = session.query(Garden).all()


# vegetable_names = ["Carrot", "Tomato", "Cabbage", "Spinach", "Broccoli", "Okra", "Eggplant", "Cauliflower"]
# vegetable_ripeness = ["Not Ripe", "Almost Ripe", "Ripe", "Over-Ripe"]


# for garden in db_gardens:
#     for _ in range(3):
#         random_veg_name = random.choice(vegetable_names)
#         random_quanity = random.randint(15,40)
#         random_ripeness = random.choice(vegetable_ripeness)
#         new_vegetable = Vegetable(veg_name=random_name, quanity=random_color, ripeness=garden)
#         session.add(new_vegetable)



# session.add()
# session.commit()
# session.close()

print("Done seeding.")