"""
This program makes the inventory manager which manage the inventory object
and call the inventory object to add its price and return its string in json file

Author: Shruti Zarbade
Date: 28/01/2020
To Do : Adding the data in json file given by the user using inventory manager
"""
import json


class InventoryManager:

    def __init__(self, json_file):  # Taking file to get data from json file
        self.json_file = json_file
        self.inventory = None

    def inventory_factory(self):
        """
        This is the method to get data from inventory file and show value of each item in inventory
        """

        with open(self.json_file, 'r') as file:
            self.inventory = json.load(file)
            # for item in self.inventory["inventory"]:
            #     print("adding data in json file")
            #     print(f"value of {item['weight']}Kg of {item['name']} is \
            #     {item['weight'] * item['price_per_kg']}")

    def add_to_inventory(self):
        """
        Method to add item to inventory and save to json file
        """
        n = int(input("Enter number of items you would like to add to inventory :\n"))
        for i in range(n):
            while True:
                try:  # Getting information about data to add to inventory json file
                    item = input("Item you would want to enter to inventory :\n")
                    weight = int(input("Enter weight of the product you are adding to inventory :\n"))
                    price = int(input("Enter cost per KG of the product "))

                except ValueError:
                    print("Please enter values for weight and price per kg")

                else:
                     break

            with open(self.json_file, 'r+') as f:  # Saving changes to json file
                data = dict()
                data['name'] = item
                data['weight'] = weight
                data['price_per_kg'] = price
                self.inventory["inventory"].append(data)
                json.dump(self.inventory, f, indent=2)


if __name__ == "__main__":
    a = InventoryManager("inventory_mngm.json")
    a.inventory_factory()
    a.add_to_inventory()



