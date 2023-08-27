
from simple_term_menu import TerminalMenu
from models import Garden, Vegetable
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



# import ipdb

engine = create_engine("sqlite:///main.db")
Session = sessionmaker(bind=engine)
session = Session()

class Cli():

    def __init__(self):
        pass
    
    
    def start(self):
        self.clear_screen()

        print("Welcome to our Gardening App\n")
        print("Please choose a garden to visit\n")

        options = ["Greenwood Garden", "West Side Community Garden", "Duke Farms Community Garden", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Greenwood Garden":
            print("You selected Garden 1")
            self.show_options("Greenwood Garden")
        elif options[menu_entry_index] == "West Side Community Garden":
            print("You selected Garden 2")
            self.show_options("West Side Community Garden")
        elif options[menu_entry_index] == "Duke Farms Community Garden":
            print("You selected Garden 3")
            self.show_options("Duke Farms Community Garden")
        else:
            self.exit()


    def show_options(self, garden):
        self.clear_screen()
        print("you made it to show_options")
        
        print(garden)


        print("Please choose from 2nd list\n")

        options = ["View all vegetables", "Add a vegetable", "Remove a vegetable", "Update the quanity", "Home"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "View all vegetables":
            print("You selected View all vegetables")
            self.view_all_vegetable(garden)
            
        elif options[menu_entry_index] == "Add a vegetable":
            print("You selected Add a vegetable")
            
        elif options[menu_entry_index] == "Remove a vegetable":
            print("You selected Remove a vegetable")

        elif options[menu_entry_index] == "Update the quanity":
            print("You selected Update the quanity")  

        else:
            self.start()



    def view_all_vegetable(self, garden):
        self.clear_screen()
        print(garden)
        veggies = Vegetable.query_all()
        
        for v in veggies:  
            print(v)



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





    def exit(self):
        self.clear_screen()
        print("Thank you for visiting, Goodbye!")

    
    def clear_screen(self):
        print("\n" * 30)

    
app = Cli()
app.start()

#if __name__ == '__main__':