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

User logins in the patient table
Based on speciality, you see list of available doctors
filtering the doctors table to show the right doctors
Connect to the doctor - 