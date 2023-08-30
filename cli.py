#!/usr/bin/env python3
from simple_term_menu import TerminalMenu
from models import Garden, Vegetable
from prettycli import red, yellow, green
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# import ipdb
# ipdb.set_trace()

# Session below only for testing purposes
# engine = create_engine("sqlite:///main.db")
# Session = sessionmaker(bind=engine)
# session = Session()

class Cli():

    def __init__(self):
        pass
    
# Main menu        
    def start(self):
        self.clear_screen(15)

        print(green("Welcome to my Garden Management App\n"))
        print(green("What would you like to do?\n"))

        options = [
            "View all Vegetables",
            "Add a vegetable",
            "Remove a vegetable",
            "Update the quantity",
            "Order by quantity",
            "Exit"
        ]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "View all Vegetables":
            self.choose_garden_menu("view_all_from_garden")       
        elif options[menu_entry_index] == "Add a vegetable":
            self.choose_garden_menu("add_vegetable") 
        elif options[menu_entry_index] == "Remove a vegetable":
            self.choose_garden_menu("remove_vegetable") 
        elif options[menu_entry_index] == "Update the quantity":
            self.choose_garden_menu("update_vegetable") 
        elif options[menu_entry_index] == "Order by quantity":
            self.choose_garden_menu("order_by")        
        else:
            self.exit()


# Choose the garden sub menu
    def choose_garden_menu(self, arg_name):
        self.clear_screen(15)
        print(green("Please choose the Garden"))
  
        options = ["Greenwood Garden", "West Side Community Garden", "Duke Farms Community Garden", "Home"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
#Checking if Home was selected        
        if options[menu_entry_index] == "Home":
            self.start()
        else:
# Checking which method to run based on the chosen garden and main menu option    
            if arg_name == "view_all_from_garden":
                self.view_all_from_garden(options[menu_entry_index])
            elif arg_name == "add_vegetable":
                self.add_vegetable((options[menu_entry_index]))
            elif arg_name == "remove_vegetable":
                self.remove_vegetable((options[menu_entry_index]))
            elif arg_name == "update_vegetable":
                self.update_vegetable((options[menu_entry_index]))
            elif arg_name == "order_by":
                self.order_by((options[menu_entry_index]))
            else:
                print(red("Oops, something went wrong")) 


# View all vegetables based on garden selected
    def view_all_from_garden(self, garden_name):       
        self.clear_screen(15) 
        print(green(f"Here is everything from {garden_name}...\n\n"))

        Garden.query_all_vegs(garden_name)
        self.home_option()


# Add a new vegetable to the DB  based on the user input
    def add_vegetable(self, garden_name):
        self.clear_screen(15)
        print(green(f"Let's add to {garden_name}...\n\n"))

#input collected from user and validated in the models.py
        question = "Enter the new vegetable's name: "

        name = Vegetable.validate_name_input(question)
        quantity = Vegetable.validate_quantity_input()
        ripeness = Vegetable.validate_ripeness_input()

        print(green(f"\n\n{name} has been added successfully:"))

        selected_garden_id = Garden.get_garden_id(garden_name)
        Vegetable.add_veg(name, quantity, ripeness, selected_garden_id)

        print(green("\n\nHere is the fully updated list\n"))
        Garden.query_all_vegs(garden_name)

        self.home_option()


# Removes a vegetable from the DB based on name entered
    def remove_vegetable(self, garden_name):
        self.clear_screen(5)
        print(green(f"Let's remove from {garden_name}...\n\n"))

        Garden.query_all_vegs(garden_name)

        question = "\nPlease enter the name of the vegetable you'd like to remove: "
        name = Vegetable.validate_name_input(question)

        check_name_exist = Vegetable.check_name_exist(name, garden_name)
        if check_name_exist:
            print(green("\nVegetable found..."))
        else:
            print(yellow("\nThat vegetable doesn't exist, please try again\n"))
            self.remove_vegetable(garden_name)

        g_id = Garden.get_garden_id(garden_name)
        Vegetable.remove_veg(name, g_id)
        print(green(f"\n{name} has been removed"))

        print(green(f"\nHere is the updated list\n"))
        Garden.query_all_vegs(garden_name)

        self.home_option()


# Updates a vegetables quantity based on user selection
    def update_vegetable(self, garden_name):
        self.clear_screen(5)
        print(green(f"Let's update the quantity at {garden_name}...\n\n"))

        Garden.query_all_vegs(garden_name)

        question = "\nPlease enter the name of the vegetable you'd like to update: "
        name = Vegetable.validate_name_input(question)

        check_name_exist = Vegetable.check_name_exist(name, garden_name)
        if check_name_exist:
            print(green("\nVegetable found..."))
        else:
            print(yellow("\nThat vegetable doesn't exist, please try again\n"))
            self.update_vegetable(garden_name)
        
        new_qty = Vegetable.validate_quantity_input()
        g_id = Garden.get_garden_id(garden_name)
        Vegetable.update_quantity(name, new_qty, g_id)
        
        print(green(f"\n{name}'s quantity has been updated to {new_qty}.\n"))
        Garden.query_all_vegs(garden_name)

        self.home_option()


# Order by the quantity
    def order_by(self, garden_name):
        self.clear_screen(15) 
        
        print(green(f"Here is everything from {garden_name} ordered by quantity...\n\n"))

        Vegetable.order_by_asc(garden_name)
        self.home_option()
       

# Home option to return to the homepage
    def home_option(self):
        self.clear_screen(5)

        options = ["Home"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Home":
            self.start()
        
# exit option to close program
    def exit(self):
        print("\n" * 30)
        print(green("Thank you for visiting, Goodbye!"))
        print("\n" * 20)

# To add room between menus, default set but override possible
    def clear_screen(self, lines=30):
        print("\n" * lines)

if __name__ == '__main__':
    app = Cli()
    app.start()

    