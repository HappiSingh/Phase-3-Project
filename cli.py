
from simple_term_menu import TerminalMenu
from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



import ipdb
        # ipdb.set_trace() 

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()

class Cli():

    def __init__(self):
        pass
    
    
    def start(self):
        self.clear_screen(15)

        print("Welcome to our Gardening App\n")
        print("Please choose a garden to visit\n")

        options = [
            "View all vegetables from Greenwood Garden", 
            "View all vegetables from West Side Community Garden", 
            "View all vegetables from Duke Farms Community Garden", 
            "Exit"
            ]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "View all vegetables from Greenwood Garden":
            print("You selected Garden 1")
            self.view_from_g1("Greenwood Garden")

        elif options[menu_entry_index] == "View all vegetables from West Side Community Garden":
            print("You selected Garden 2")
            self.view_from_g1("West Side Community Garden")

        elif options[menu_entry_index] == "View all vegetables from Duke Farms Community Garden":
            print("You selected Garden 3")
            self.view_from_g1("Duke Farms Community Garden")

        else:
            self.exit(20)


    # View all vegetables based on garden selected
    def view_from_g1(self, name):

        self.clear_screen()

        g1 = Garden.query_g1(name)
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









    def add_vegetable(self):
        pass

    def update_vegetable(self):
        pass

    def remove_vegetable(self):
        pass

    def filter_by_ripeness(self):
        pass

    def filter_by_quanity(self):
        pass




    # exit option to close program
    def exit(self, lines):
        print("\n" * lines)
        print("Thank you for visiting, Goodbye!")

    # To add room between menus, default set but override possible
    def clear_screen(self, lines=30):
        print("\n" * lines)

    
app = Cli()
app.start()

#if __name__ == '__main__':