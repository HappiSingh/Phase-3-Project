# Phase 3 Python Command Line Project Notes

-------------------------------------------------------------------------------------
# To-Do's
1. create virtual environment (pipenv --python 3.8.13)
2. install dependencies (pipenv install sqlalchemy==1.4.41 alembic ipdb faker)
    - SQLAlchemy 1.4.41
    - Alembic (migrations manager)
    - ipdb
    - faker (to generate fake data)
3. create migration environment (in shell: alembic init migrations)
(sqlite:///main.db)(render_as_batch=True)(target_metadata = Base.metadata)(from models import Base)
4. to configure the migigration envirnment (alembic.ini and env.py) (batch=true)
5. create Base
6. Create Schema (python classes or models)
7. populate the database with seeds file
8. test relationships (one to many)
9. query the data to test it 

-------------------------------------------------------------------------------------
# Migrations Notes

### Generating a new migration

`alembic --autogenerate -m 'name that describes updates to the schema'`

### Executing a migration (upgrade)

`alembic upgrade head`

### Undo last migration

`alembic downgrade -1`

### Downgrade to revision down_id

`alembic downgrade [down_id_in_migration_script_file]`

### Rollback DB to the initial state

`alembic downgrade base`

-------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
# You will need to import your own models
from models import ModelOne, ModelTwo   
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Query the DB with session example: session.query(ModelOne).all()
engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session() 

# Use ipdb to interact with DB using session
# Dont forget to add ipdb as a dependency - pipenv install ipdb
import ipdb; ipdb.set_trace() 

# For generating Fake data: https://faker.readthedocs.io/en/master/providers.html
from faker import Faker 

# For working with an API and retrieving json data
import requests
import json

# Example request
response = requests.get(API_URL)
json_data = json.loads(response.text)

-------------------------------------------------------------------------------------

 # options = [
        #     "View all vegetables from Greenwood Garden", 
        #     "View all vegetables from West Side Community Garden", 
        #     "View all vegetables from Duke Farms Community Garden", 
        #     "Add a vegetable to Greenwood Garden",
        #     "Add a vegetable to West Side Community Garden",
        #     "Add a vegetable to Duke Farms Community Garden",
        #     "Remove a vegetable from Greenwood Garden",
        #     "Remove a vegetable from West Side Community Garden",
        #     "Remove a vegetable from Duke Farms Community Garden",
        #     "Update the quanity from Greenwood Garden",
        #     "Update the quanity from West Side Community Garden",
        #     "Update the quanity from Duke Farms Community Garden",
        #     "Order by quanity",
        #     "View all Vegetables",
        #     "Exit"
        #     ]

# #Viewing from DB
#         if options[menu_entry_index] == "View all vegetables from Greenwood Garden":
#             self.view_all_from_garden("Greenwood Garden")

#         elif options[menu_entry_index] == "View all vegetables from West Side Community Garden":
#             self.view_all_from_garden("West Side Community Garden")

#         elif options[menu_entry_index] == "View all vegetables from Duke Farms Community Garden":
#             self.view_all_from_garden("Duke Farms Community Garden")

# #Adding to DB
#         elif options[menu_entry_index] == "Add a vegetable to Greenwood Garden":
#             self.add_vegetable("Greenwood Garden")

#         elif options[menu_entry_index] == "Add a vegetable to West Side Community Garden":
#             self.add_vegetable("West Side Community Garden")

#         elif options[menu_entry_index] == "Add a vegetable to Duke Farms Community Garden":
#             self.add_vegetable("Duke Farms Community Garden")

# #Remove from DB
#         elif options[menu_entry_index] == "Remove a vegetable from Greenwood Garden":          
#             self.remove_vegetable("Greenwood Garden")

#         elif options[menu_entry_index] == "Remove a vegetable from West Side Community Garden":           
#             self.remove_vegetable("West Side Community Garden")

#         elif options[menu_entry_index] == "Remove a vegetable from Duke Farms Community Garden":          
#             self.remove_vegetable("Duke Farms Community Garden")

# #Update the DB
#         elif options[menu_entry_index] == "Update the quanity from Greenwood Garden":           
#             self.update_vegetable("Greenwood Garden")

#         elif options[menu_entry_index] == "Update the quanity from West Side Community Garden":           
#             self.update_vegetable("West Side Community Garden")

#         elif options[menu_entry_index] == "Update the quanity from Duke Farms Community Garden":
#             self.update_vegetable("Duke Farms Community Garden")



 # def show_options(self, garden):
    #     self.clear_screen()
    #     print("you made it to show_options")
        
    #     print(garden)


    #     print("Please choose from 2nd list\n")

    #     options = ["View all vegetables", "Add a vegetable", "Remove a vegetable", "Update the quanity", "Home"]
    #     terminal_menu = TerminalMenu(options)
    #     menu_entry_index = terminal_menu.show()

    #     if options[menu_entry_index] == "View all vegetables":
    #         print("You selected View all vegetables")
    #         self.view_all_vegetable(garden)
            
    #     elif options[menu_entry_index] == "Add a vegetable":
    #         print("You selected Add a vegetable")
            
    #     elif options[menu_entry_index] == "Remove a vegetable":
    #         print("You selected Remove a vegetable")

    #     elif options[menu_entry_index] == "Update the quanity":
    #         print("You selected Update the quanity")  

    #     else:
    #         self.start()
