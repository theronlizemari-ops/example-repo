import os


# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function the following attributes are initialised:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):  # code to return the cost of each shoe item
        return self.cost

    def get_quantity(self):  # code to get the quantity of each shoe item
        return f"{self.product}: {self.quantity}"

    def __str__(self):  # code to return a string representation of a class
        return ("\n"
                f"Country:  {self.country}\n"
                f"Code:     {self.code}\n"
                f"Product:  {self.product}\n"
                f"Cost:     {self.cost}\n"
                f"Quantity: {self.quantity}\n"
                "\n"
                )


# =============Shoe list===========

shoe_list = []

# Using os.path to ensure the program reads the file from the correct path

file_name = "inventory.txt"

file_path = os.path.join(os.getcwd(), file_name)

# ==========Functions outside the class==============


def read_shoes_data():

    if os.path.exists(file_name):

        try:
            with open(file_name, "r") as f:

                f.readline()  # skips the first line

                for line in f:  # text file to a list of Classes
                    contents = line.split(",")

                    country = contents[0]
                    code = contents[1]
                    product = contents[2]
                    cost = int(contents[3])
                    quantity = int(contents[4])

                    shoe_object = Shoe(country, code, product, cost, quantity)
                    shoe_list.append(shoe_object)

        except Exception:
            print("An error occured."
                  f"Please check the integrity of {file_name}.")

    else:
        print(
         f"Error, please make sure {file_name} is downloaded "
         f"in your current working folder: \n{file_path}"
        )

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file
    represents data to create one object of shoes.
    It uses try-except for error handling ans skips the first line
    of the file using code.
    '''


def capture_shoes():

    while True:
        try:  # Input information about new item
            print("Please fill in the details about the shoe items:\n")
            country = input("Country: ")
            code = input("Code: ")
            product = input("Product: ")
            cost = int(input("Cost: "))
            quantity = int(input("Quantity: "))

            # append new item to text file
            # does not append to list, list updated with read_shoes_data()
            try:
                with open(file_name, "a") as file:
                    file.write(f"\n{country},{code},"
                               f"{product},{cost},{quantity}")

            except Exception:
                print("Something went wrong with updating your file.")
            break

        except Exception:
            print("An error occured. Please try again.")

    print("\nItem sucsesfully stored.\n")
    '''
    This function will allow a user to capture data
    about a shoe and use this data to append to the text file.
    '''


def view_all():
    shoe_list.sort(key=lambda s: s.product)  # Sort list in alfabetical order

    if not shoe_list:
        print("No shoes in the inventory.")
        return

    print("\nItems listed in alfabetical order according to product name:")
    for shoe in shoe_list:  # Iteration to print every shoe object
        print(shoe)
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''


def re_stock():

    if not shoe_list:
        print("No shoes in the inventory.")
        return

    else:
        # Find item with least amount of stock
        least_stock = min(shoe_list, key=lambda s: s.quantity)
        print("\nThis is the item with the least amount of stock: ")
        print(least_stock)

        while True:
            update_stock = input(
                "Do you want to update the stock? (yes/no): "
                ).lower()

            if update_stock in ["no", "n"]:  # No update to stock
                print("Program exit.")
                break

            elif update_stock in ["yes", "y"]:  # Update stock
                try:
                    add_stock = int(input("How much stock are your adding? "))
                    least_stock.quantity = least_stock.quantity + add_stock
                    print(f"\nStock has been updated: {least_stock}")

                    # update text file with new stock number
                    # this re-writes the entire file with the updated stock
                    # my skills not there yet to only re-write the number
                    with open(file_name, "w") as file:
                        file.write("Country,Code,Product,Cost,Quantity")
                        for least_stock in shoe_list:
                            file.write(f"\n{least_stock.country},"
                                       f"{least_stock.code},"
                                       f"{least_stock.product},"
                                       f"{least_stock.cost},"
                                       f"{least_stock.quantity}")
                    break
                except ValueError:
                    print("Invalid number.")

            else:
                print("Invalid input. Please try again.")
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. It asks the user if they
    want to add this quantity of shoes and then update it.
    This quantity is updated in the text file for this shoe.
    '''


def search_shoe():
    # Look for a particular item in list
    look_for = input("Type the code of the item you are looking for: ")

    while True:
        try:  # Search
            result = next(
                (shoe for shoe in shoe_list if shoe.code == look_for)
                )
            print(f"{result}")
            break

        except StopIteration:
            print("Item not found. Double-check your spelling.")
            break
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''


def value_per_item():

    shoe_list.sort(key=lambda s: s.product)  # sort in alfabetical order

    print("\nList of stock and their values.\n")
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)  # multiplication
        print(f"{shoe.product} is valued at {value}\n")
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():

    # Find maximum in list
    most_stock = max(shoe_list, key=lambda s: s.quantity)
    print("\nThis product has the most amount of stock and can go on sale:")
    print(most_stock)
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''


# ==========Main Menu=============

# Run function to read file
read_shoes_data()

# Menu that executes each function.
while True:
    menu = """
Would you like to:
    1. View all shoe items
    2. Add new shoe item
    3. Check least amount of stock or restock
    4. Search for a particular item
    5. Check value of each stock item
    6. See which items can go on sale
    7. Quit application

Enter selection:
"""
    user_choice = input(menu)

    if user_choice == "1":
        view_all()
    elif user_choice == "2":
        capture_shoes()
    elif user_choice == "3":
        re_stock()
    elif user_choice == "4":
        search_shoe()
    elif user_choice == "5":
        value_per_item()
    elif user_choice == "6":
        highest_qty()
    elif user_choice == "7":
        print("Quitting application.")
        break
    else:
        print("Invalid choice. Please select again.")
