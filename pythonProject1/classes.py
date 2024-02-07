class Animal:   #klasa --> wzorzec dla obiektu, opisuje obiekt  #obiekt --> byt, który tworzymy na bazie klasy

    def __init__(self, name):   #konstruktor --> pozwala na wykonanie fragmentu kodu przy tworzeniu obiektu, możliwość stworzenia klasy, która przyjmuję warunki początkowe
        self.name = name
    def set_a_name(self, new_name):    #tworzenie metody(funkcja wewnątrz klasy) , self --> pozwala korzystać ze zmiennych i metod w innym miejscu klasy
        self.name = new_name

    def print_name(self):
        print(self.name)          # 1 sposób to --> drukowanie

    def get_name(self):
        return self.name           # 2 sposób to --> zwracanie

class Cat(Animal):

    def __init__(self, breed, name):
        super().__init__(name)
        self.breed = breed

    def calculate_food(self, mass):
        return mass * 7

pajton = Cat("dachowiec", "Pajton")
pajton.print_name()
food_needed = pajton.calculate_food(4.5)
print(f"Food needed: {pajton.calculate_food(4.5)}")

# my_animal = Animal("Reksio")       #obiekt na bazie klasy Animal musi być!!!!! () --> powoduję stworzenie nowego obiektu
# my_animal.set_a_name("Azor")            #wstawianie imienia
# my_animal.print_name()
#

# class Person:
#
#     def __init__(self, name, surname, year_of_birth):
#         self.name = name
#         self.surname = surname
#         self.year_of_birth = year_of_birth
#
#     def print_full_name(self):
#        print(f"{self.name} {self.surname}")
#
#     def get_age(self):
#         age = 2023 - self.year_of_birth
#         return age
#     def change_surname(self, new_surname):
#         self.surname = new_surname
#
#
# jan = Person("Jan", "Testowy", 1999 )
# jan.print_full_name()
# jan.change_surname("Nietestowy")
# jan.print_full_name()
# jan.get_age()
# print(jan.get_age())
