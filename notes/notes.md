# Phase 3 Python Command Line Project Notes

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