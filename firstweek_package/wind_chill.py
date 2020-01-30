from utility import Utility

t = int(input("Temperature in t: "))
v = int(input("Wind Speed v: "))

print(Utility.wind_chill(t, v))