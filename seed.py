from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
# from faker import Faker 
# import ipdb
# ipdb.set_trace()


if __name__ == '__main__':

    engine = create_engine("sqlite:///main.db")
    Session = sessionmaker(bind=engine)
    session = Session()


    print("Deleting existing DB sample data...")

# Resetting DB data before seeding again
    session.query(Garden).delete()
    session.query(Vegetable).delete()


#######################################################################################################################################
# Creating the garden instances using dictionary
gardens = {
    "Greenwood Garden": ["New Jersey", "8,000 sqft"],
    "West Side Community Garden": ["New York", "6,000 sqft"],
    "Duke Farms Community Garden": ["New Jersey", "5,000 sqft"]
    }

garden_instances = []

for garden_name, garden_values in gardens.items():
    garden_location, garden_size = garden_values
    garden_instance = Garden(name=garden_name, location=garden_location, size=garden_size)
    garden_instances.append(garden_instance)

#######################################################################################################################################

session.bulk_save_objects(garden_instances)

db_gardens = session.query(Garden).all()



vegetable_names = ["Carrot", "Broccoli", "Tomato", "Spinach", "Cucumber", "Bell Pepper", "Zucchini", "Lettuce", "Cabbage", "Onion", "Peas", "Radish"]
vegetable_ripeness = ["Unripe", "Almost Ripe", "Ripe", "Overripe"]

# Assigning vegetable data to each garden at random from list above
for garden in db_gardens:
    for _ in range(4):
        random_veg_name = random.choice(vegetable_names)
        random_quanity = random.randint(15,85)
        random_ripeness = random.choice(vegetable_ripeness)
        new_vegetable = Vegetable(veg_name=random_veg_name, quanity=random_quanity, ripeness=random_ripeness, garden_id = garden.id )
        session.add(new_vegetable)


session.commit()

print("New data seeded successfully.")
print("Seeding Complete")

session.close()
# ipdb.set_trace()