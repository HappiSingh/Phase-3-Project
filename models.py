from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey


Base = declarative_base()


class Doctor(Base):
    __tablename__ = "doctor"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    speciality = Column(String, nullable=False)
    
    patients = relationship("Patient", backref=("doctor"))


    def __repr__(self):
       return f"<Doctor {self.id} {self.first_name} {self.last_name} {self.speciality}>"

    
        
class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(), unique=True)

    doctor_id = Column(Integer, ForeignKey("doctor.id"))


    def __repr__(self):
        return f"<Patient {self.id} {self.first_name} {self.last_name} {self.email}>"
