
# Welcome to my Garden Management App
### A Python Command Line Project using SQLAlchemy and Alembic

## Description
Welcome to my Garden Management CLI App, an essential tool for seamlessly interacting with your meticulously cultivated gardens. This project empowers you to effortlessly navigate through a range of CRUD functionalities, all tailored to enhance your gardening journey. Immerse yourself in the art of gardening by exploring and managing your selected garden's vegetables. Whether you're inspecting the array of vegetables, introducing new ones, adjusting quantities, or handling removals. This CLI App offers a cohesive and intuitive experience with Python and SQLAlchemy running under the hood. Elevate your vegetable management practices and make the most of your green haven.


## Features
+ Database models with SQLAlchemy ORM and Alembic
+ Python OOP back-end
+ Use of a variety data structures (lists, dicts, etc)
+ Use of external libraries (tabulate, simple_term_menu, etc)


## Installation

### Install and configure our environment
```python
pipenv install
```

### Enter the Python shell
```python
pipenv shell
``` 

### Create the Database
```python
alembic revision --autogenerate
```

```python
alembic upgrade head
```

### Populate with sample data
```python
python3 seed.py
```

### Run the CLI app
```python
./cli.py
```

## Usage
You begin on the main menu. Here, you are greeted with a welcome message and some options to get started. Use the up-and-down arrows on your keyboard to navigate the options menu. Each option you click will take you to a sub-menu where you select the garden you wish to perform the CRUD actions on. View all vegetables will show a table with all the data fetched from the selected garden. Add a vegetable will take your input, validate it, and create a new entry in the database. Remove a vegetable will delete an entry from the selected garden's database given your input. The Update option will let you update the quantity of your selected vegetable from your garden. Order by will sort the database in ascending order based on quantity for easy viewing. Finally, Exit will close the app. In all other sub-menus, a convenient Home option is provided to return to the main menu. 

## License
MIT License

Copyright (c) 2023 Harpreet Singh

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.