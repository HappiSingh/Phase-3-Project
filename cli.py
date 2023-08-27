#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import ipdb
# ipdb.set_trace() 

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()


class Cli():

    def __init__(self):
        pass
    
    def start(self):
        self.clear_screen(15)

        print("Welcome to my Garden Management App\n")
        print("What would you like to do?\n")

        options = [
            "View all vegetables from Greenwood Garden", 
            "View all vegetables from West Side Community Garden", 
            "View all vegetables from Duke Farms Community Garden", 
            "Add a vegetable to Greenwood Garden",
            "Add a vegetable to West Side Community Garden",
            "Add a vegetable to Duke Farms Community Garden",
            "Remove a vegetable from Greenwood Garden",
            "Remove a vegetable from West Side Community Garden",
            "Remove a vegetable from Duke Farms Community Garden",
            "Update the quanity from Greenwood Garden",
            "Update the quanity from West Side Community Garden",
            "Update the quanity from Duke Farms Community Garden",
            "Exit"
            ]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

#Viewing from DB
        if options[menu_entry_index] == "View all vegetables from Greenwood Garden":
            self.view_all_from_garden("Greenwood Garden")

        elif options[menu_entry_index] == "View all vegetables from West Side Community Garden":
            self.view_all_from_garden("West Side Community Garden")

        elif options[menu_entry_index] == "View all vegetables from Duke Farms Community Garden":
            self.view_all_from_garden("Duke Farms Community Garden")

#Adding to DB
        elif options[menu_entry_index] == "Add a vegetable to Greenwood Garden":
            self.add_vegetable("Greenwood Garden")

        elif options[menu_entry_index] == "Add a vegetable to West Side Community Garden":
            self.add_vegetable("West Side Community Garden")

        elif options[menu_entry_index] == "Add a vegetable to Duke Farms Community Garden":
            self.add_vegetable("Duke Farms Community Garden")

#Remove from DB
        elif options[menu_entry_index] == "Remove a vegetable from Greenwood Garden":
            print("Remove from Greenwood Garden...")
            self.remove_vegetable("Greenwood Garden")

        elif options[menu_entry_index] == "Remove a vegetable from West Side Community Garden":
            print("Remove from West Side Community Gardenn...")
            self.remove_vegetable("West Side Community Garden")

        elif options[menu_entry_index] == "Remove a vegetable from Duke Farms Community Garden":
            print("Remove from Duke Farms Community Garden...")
            self.remove_vegetable("Duke Farms Community Garden")

#Update the DB
        elif options[menu_entry_index] == "Update the quanity from Greenwood Garden":
            print("Update quanity on Greenwood Garden...")
            self.update_vegetable("Greenwood Garden")

        elif options[menu_entry_index] == "Update the quanity from West Side Community Garden":
            print("Update quanity on West Side Community Garden...")
            self.update_vegetable("West Side Community Garden")

        elif options[menu_entry_index] == "Update the quanity from Duke Farms Community Garden":
            print("Update quanity on Duke Farms Community Garden...")
            self.update_vegetable("Duke Farms Community Garden")
#Exit 
        else:
            self.exit()


   
# View all vegetables based on garden selected
    def view_all_from_garden(self, garden_name):
        
        self.clear_screen() 
        print(f"Here is everything from {garden_name}...\n\n")

        Garden.query_all_vegs(garden_name)

        self.home_option()



# Add a new vegetable to the DB  based on the user input
    def add_vegetable(self, garden_name):
        
        self.clear_screen()
        print(f"Let's add to {garden_name}...\n\n")

        name = input("Enter the vegetable's name: ")
        quanity = int(input("Enter the vegetables quanity: "))
        ripeness = input("Enter the ripeness: [Not Ripe, Almost Ripe, Ripe, Over-Ripe]: ")

        print("\nVegetable has been added successfully:")

        selected_garden_id = Garden.get_garden_id(garden_name)
        Vegetable.add_veg(name, quanity, ripeness, selected_garden_id)

        self.home_option()



# Removes a vegetable from the DB based on name entered
    def remove_vegetable(self, garden_name):
        
        self.clear_screen()
        print(f"Let's remove from {garden_name}...\n\n")

        Garden.query_all_vegs(garden_name)

        name = input("Please enter the name of the vegetable you'd like to remove: ")

        Vegetable.remove_veg(name)

        print(f"\n{name} has been removed")
        print(f"\nHere is the updated list")

        session.expire_all()
        Garden.query_all_vegs(garden_name)

        self.home_option()



# Updates a vegetables quanity based on user selection
    def update_vegetable(self, garden_name):

        self.clear_screen()
        print(f"Let's update {garden_name}...\n\n")


        Garden.query_all_vegs(garden_name)

        name = input("Please enter the name of the vegetable you'd like update: ")
        print(name)

        new_qty = input(f"Please enter the new quanity of {name}: ")
        print(new_qty)

        Vegetable.update_quanity(name, new_qty)
        # session.query(Vegetable).filter(Vegetable.veg_name == name).update({'quanity': new_qty})
        # session.commit()
    


        session.expire_all()

        


        print(f"{name}'s quanity has been updated to {new_qty}.")
        print(g1)

        self.home_option()



















    # Home option to return to the homepage [start()]
    def home_option(self):
        self.clear_screen(2)

        options = ["Home"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Home":
            self.start()
        



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












    def filter_by_ripeness(self):
        pass

    def filter_by_quanity(self):
        pass




# exit option to close program
    def exit(self):
        print("\n" * 30)
        print("Thank you for visiting, Goodbye!")
        print("\n" * 20)


# To add room between menus, default set but override possible
    def clear_screen(self, lines=40):
        print("\n" * lines)


if __name__ == '__main__':
    app = Cli()
    app.start()