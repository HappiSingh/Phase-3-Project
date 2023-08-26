# from models import Doctor, Patient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from faker import Faker 
# import ipdb

# if __name__ == '__main__':

#     engine = create_engine("sqlite:///main.db")
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     # doctors = [
#     #     Doctor(first_name="John", last_name="Smith", speciality="Cardiologist"),
#     #     Doctor(first_name="Andy", last_name="Adkins", speciality="Pediatrics"),
#     #     Doctor(first_name="Samantha", last_name="Urban", speciality="Dermatology")
#     # ]

#     ipdb.set_trace()

#     # session.bulk_save_objects(doctors)
#     # session.commit()

#     doc_1 = Doctor(first_name="John", last_name="Smith", speciality="Cardiologist")
#     doc_2 = Doctor(first_name="Andy", last_name="Adkins", speciality="Pediatrics")

#     session.bulk_save_objects([doc_1, doc_2])
#     session.commit()
