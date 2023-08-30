from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettycli import green, yellow
import random
# import ipdb
# ipdb.set_trace()

if __name__ == '__main__':

    engine = create_engine("sqlite:///main.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    print(yellow("Deleting existing DB sample data..."))

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

session.bulk_save_objects(garden_instances)

#######################################################################################################################################

db_gardens = session.query(Garden).all()

vegetable_names = ["Carrot", "Broccoli", "Tomato", "Spinach", "Cucumber", "Potato", "Pepper", 
                   "Lettuce", "Cabbage", "Onion", "Radish", "Zucchini", "Eggplant", "Kale", "Beet"]
vegetable_ripeness = ["Unripe", "Almost Ripe", "Ripe", "Overripe"]

# Assigning vegetable data to each garden at random from list above
for garden in db_gardens:
    available_vegetable_names = list(vegetable_names)  # Create a copy of the list
    for _ in range(4):
        random_veg_name = random.choice(available_vegetable_names)
        available_vegetable_names.remove(random_veg_name)  # Remove the chosen name
        random_quantity = random.randint(15,85)
        random_ripeness = random.choice(vegetable_ripeness)
        new_vegetable = Vegetable(veg_name=random_veg_name, quantity=random_quantity, ripeness=random_ripeness, garden_id = garden.id )
        session.add(new_vegetable)

session.commit()

print(green("New data seeded successfully"))
print(green("Seeding Complete"))

session.close()
