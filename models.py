
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from tabulate import tabulate
from prettycli import red, blue, yellow
# import ipdb
# ipdb.set_trace()

Base = declarative_base()

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()

#############################################################################################################
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
    
# Query reads all the vegetables given the garden selected
    @classmethod
    def query_all_vegs(cls, garden_name):
        selected_garden = session.query(cls).filter(cls.name == garden_name).first()

        veg_list = []
        for veg in selected_garden.vegetables:
            veg_list.append([veg.id, veg.veg_name, veg.quantity, veg.ripeness])

        
        
        headers = ["ID", "NAME", "QUANTITY", "RIPENESS"]
        print(blue(tabulate(veg_list, headers=headers, tablefmt="grid")))

# Query gets the id of the slected garden
    @classmethod
    def get_garden_id(cls, garden_name):
        selected_garden = session.query(cls).filter(cls.name == garden_name).first()
        return selected_garden.id
        

#############################################################################################################
class Vegetable(Base):
    __tablename__ = "vegetables"

    id = Column(Integer, primary_key=True)
    veg_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    ripeness = Column(String, nullable=False)

    garden_id = Column(Integer, ForeignKey("gardens.id"))


    def __repr__(self):
       return (
           f"<Vegetable: id={self.id},\n"
           f"            veg_name='{self.veg_name}',\n"
           f"            quantity='{self.quantity}',\n"
           f"            ripeness='{self.ripeness}'>\n\n"
       )


# Query that adds new vegetable data to the selected garden
    @classmethod
    def add_veg(cls, name, quantity, ripeness, selected_garden_id):
        new_veg = Vegetable(veg_name=name, quantity=quantity, ripeness=ripeness, garden_id=selected_garden_id)
        session.add(new_veg)
        session.commit()

        veg_list = [new_veg.id, new_veg.veg_name, new_veg.quantity, new_veg.ripeness]
        headers = ["ID", "NAME", "QUANTITY", "RIPENESS"]
        print(blue(tabulate([veg_list], headers=headers, tablefmt="grid")))
    
    
# Query that removes a selected vegetable
    @classmethod
    def remove_veg(cls, name, g_id):
        session.query(cls).filter(cls.garden_id == g_id).filter(cls.veg_name == name).delete()
        session.commit()


# Query that updates the quantity of a vegetable
    @classmethod
    def update_quantity(cls, name, new_qty, g_id):
        session.query(cls).filter(cls.garden_id == g_id).filter(cls.veg_name == name).update({'quantity': new_qty})
        session.commit()


# Order by quantity based on the selected garden: ASC
    @classmethod
    def order_by_asc(cls, garden_name):
        ordered_list = session.query(cls).join(Garden).filter(Garden.name == garden_name).order_by(cls.quantity).all()

        veg_list = []
        for veg in ordered_list:
            veg_list.append([veg.id, veg.veg_name, veg.quantity, veg.ripeness])
        
        headers = ["ID", "NAME", "QUANTITY", "RIPENESS"]
        print(blue(tabulate(veg_list, headers=headers, tablefmt="grid")))

    
    @classmethod
    def validate_ripeness_input(cls):
        ripeness_list = ["Unripe", "Almost Ripe", "Ripe", "Overripe"]
        ripeness = input("Enter the ripeness: (Unripe, Almost Ripe, Ripe, Overripe): ")

        while ripeness.title() not in ripeness_list:
            print(red("Not a valid option, Please choose from the list"))
            ripeness = input("Enter the ripeness: (Unripe, Almost Ripe, Ripe, Overripe): ")
        return ripeness.title()
    
    
    @classmethod
    def validate_quantity_input(cls):
        while True:
            try:
                quantity = int(input("Enter the quantity (between 1 and 100): "))
                if 1 <= quantity <= 100:
                    return quantity  # Exit the loop if input is valid
                else:
                    print(yellow("quantity must be at least 1 and no more than 100."))
            except ValueError:
                print(red("Invalid input. Please enter a number."))


    @classmethod
    def validate_name_input(cls, question):
        while True:
            name = input(question)
            if name.isalpha():
                return name.title()  # Exit the loop if input is valid
            else:
                print(red("Invalid name. Please enter a name containing only letters."))

    
    @classmethod
    def check_name_exist(cls, name, garden_name):
        check_exist = session.query(cls).join(Garden).filter(Garden.name == garden_name).filter(cls.veg_name == name).first()
        return check_exist