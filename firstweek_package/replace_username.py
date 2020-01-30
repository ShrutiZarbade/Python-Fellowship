from utility import Utility

# Getting input from user
string = input("Enter Username: ")
string= string.strip()  

# Calling method from utility
a = Utility.replace_string(string)
print(a)