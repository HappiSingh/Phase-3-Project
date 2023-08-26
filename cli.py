
from simple_term_menu import TerminalMenu
from models import Garden, Vegetable


class Cli():

    def __init__(self):
        pass
       
    
    def start(self):
        self.clear_screen()
        
        print("Welcome to our Gardening App")
        print("Please choose a garden")
        
#names should come from DB
        options = ["Garden 1", "Garden 2", "Garden 3", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Garden 1":
            print("You selected Garden 1")
        elif options[menu_entry_index] == "Garden 2":
            print("You selected Garden 2")
        elif options[menu_entry_index] == "Garden 3":
            print("You selected Garden 3")
        else:
            self.exit()


    def view_all_vegetable(self):
        pass

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
        print("\n" * 40)

    
app = Cli()
app.start()