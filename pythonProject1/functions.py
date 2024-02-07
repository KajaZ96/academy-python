import math


def add_one(value):
    result = value + 1
    return  result


def calculate_fuel(mass):
     # fuel = math.floor(mass / 3) - 2  #korzystanie zbibliotek wbudowanych, zaokrąglenie
    fuel = int(mass / 3) - 2   #zaokrąglenie - liczba całkowita bez miejsc po przecinku 
    return fuel

print(calculate_fuel(14))