import math


def add_one(value):
    result = value + 1
    return  result


def calculate_fuel(mass):

    if type(mass) not in [int, float]: # fuel = math.floor(mass / 3) - 2  #korzystanie zbibliotek wbudowanych, zaokrąglenie
        return None

    if mass <=0:
        return None  #return --> wychodzi z funkcji i kończy działanie

    fuel = mass // 3 - 2   #zaokrąglenie - liczba całkowita bez miejsc po przecinku

    if fuel <= 0:
        return 1

    return fuel

# print(calculate_fuel(14))

print("xxxxxxxxxxxxxxx")

if __name__ == '__main__':    #--> wykonuje się tylko w tym pliku
    print("yyyyyyyyyyyyyyyyyy")


