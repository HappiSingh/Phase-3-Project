
from sqlalchemy.orm import declarative_base, relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
# import ipdb

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

        for veg in selected_garden.vegetables:
            print(
                f"id={veg.id}\n"
                f"name= {veg.veg_name}\n"
                f"quanity= {veg.quanity}\n"
                f"ripeness= {veg.ripeness}\n"
            )
    

# Query that finds the garden id given the name (garden selected)     
    @classmethod
    def get_garden_id(cls, garden_name):
        selected_garden = session.query(cls).filter(cls.name == garden_name).first()
        return selected_garden.id



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

        print(
                f"\n"
                f"id={new_veg.id}\n"
                f"name= {new_veg.veg_name}\n"
                f"quanity= {new_veg.quanity}\n"
                f"ripeness= {new_veg.ripeness}\n"
            )
    
    
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
        g_id = Garden.get_garden_id(garden_name)
        ordered_list = session.query(Vegetable).filter(Vegetable.garden_id == g_id).order_by(Vegetable.quanity).all()

        for veg in ordered_list:
                print(
                    f"id={veg.id}\n"
                    f"name= {veg.veg_name}\n"
                    f"quanity= {veg.quanity}\n"
                    f"ripeness= {veg.ripeness}\n"
                )