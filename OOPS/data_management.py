"""
This is the data_management file in which the data from json file is
load and dump into json file

Author: Shruti Zarbade
Date: 28/01/2020

"""
import json


class Inventory:

    """
    This is the class inventory in which various method like data management
    inventory management is done
    """
    def __init__(self):
        pass

    @staticmethod
    def inventory():
        """
        In this we have done load a file into a json file and dump it into a
        variable.On which various task is perform.
        :return: it return the content with adding various element with price and weight

        """
        try:
            file = open("/home/admin1/PycharmProjects/firstproject/Files/inventory.json", 'r')
            data = json.load(file)
            a = json.dump(data, open('inventory.json', 'w'), indent=4)

            for key in data:
                for value in data[key]:
                    print(key)
                    weight = 0
                    price = 0
                    price += int(value["Price"])
                    weight += int(value["Weight"])
                    print("Name:", value["Name"])
                    print("Price:", value["Price"])
                    print("Weight:", value["Weight"])
                    print("Total price:", price * weight)
                    print()
            return data
        except FileNotFoundError:
            print("File Not found")
        except Exception:
            print("Error")


if __name__ == "__main__":
    Inventory.inventory()






