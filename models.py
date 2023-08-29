
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate


import ipdb
# ipdb.set_trace()

Base = declarative_base()

#Comment out Session code after esting is completed
engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()

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
    
# Query that reads all the vegetables given the name (garden selected) 
    @classmethod
    def query_all_vegs(cls, garden_name):

        selected_garden = session.query(cls).filter(cls.name == garden_name).first()
        veg_list = []

        for veg in selected_garden.vegetables:
            veg_list.append([veg.id, veg.veg_name, veg.quanity, veg.ripeness])
        
        headers = ["id", "name", "quanity", "ripeness"]

        print(tabulate(veg_list, headers=headers, tablefmt="grid"))
        


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


# Query that adds a new vegetable
    @classmethod
    def add_veg(cls, name, quanity, ripeness, selected_garden_id):
        new_veg = Vegetable(veg_name=name, quanity=quanity, ripeness=ripeness, garden_id=selected_garden_id)
        session.add(new_veg)
        session.commit()

        veg_list = [new_veg.id, new_veg.veg_name, new_veg.quanity, new_veg.ripeness]
        
        headers = ["id", "name", "quanity", "ripeness"]

        print(tabulate([veg_list], headers=headers, tablefmt="grid"))
    
    
# Query that removes a selected vegetable
    @classmethod
    def remove_veg(cls, name):
        session.query(cls).filter(cls.veg_name == name).delete()
        session.commit()


# Query that updates the quanity of a vegetable
    @classmethod
    def update_quanity(cls, name, new_qty):
        session.query(Vegetable).filter(Vegetable.veg_name == name).update({'quanity': new_qty})
        session.commit()


# Order by quanity based on the selected garden: ASC
    @classmethod
    def order_by_asc(cls, garden_name):
        
        ordered_list = session.query(Vegetable).join(Garden).filter(Garden.name == garden_name).order_by(Vegetable.quanity).all()
        veg_list = []

        for veg in ordered_list:
            veg_list.append([veg.id, veg.veg_name, veg.quanity, veg.ripeness])
        
        headers = ["id", "name", "quanity", "ripeness"]

        print(tabulate(veg_list, headers=headers, tablefmt="grid"))

    
    @classmethod
    def validate_ripeness_input(cls):
        ripeness_list = ["Unripe", "Almost Ripe", "Ripe", "Overripe"]

        ripeness = input("Enter the ripeness: (Unripe, Almost Ripe, Ripe, Overripe): ")

        while ripeness.title() not in ripeness_list:
            print("Not a valid option, Please choose from the list")
            ripeness = input("Enter the ripeness: (Unripe, Almost Ripe, Ripe, Overripe): ")

        return ripeness.title()
    

    
    @classmethod
    def validate_quanity_input(cls):
        while True:
            try:
                quanity = int(input("Enter the quanity (between 1 and 100): "))
                if 1 <= quanity <= 100:
                    return quanity  # Exit the loop if input is valid
                else:
                    print("Quanity must be at least 1 and no more than 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    
    @classmethod
    def validate_name_input(cls, question):
        while True:
            name = input(question)
            if name.isalpha():
                return name.title()  # Exit the loop if input is valid
            else:
                print("Invalid name. Please enter a name containing only letters.")

        
    
    @classmethod
    def check_name_exist(cls, name, garden_name):
        
        
        check_exist = session.query(Vegetable).join(Garden).filter(Garden.name == garden_name).filter(Vegetable.veg_name == name).first()
          
        return check_exist