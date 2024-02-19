# class Animal:   #klasa --> wzorzec dla obiektu, opisuje obiekt  #obiekt --> byt, który tworzymy na bazie klasy
#
#     def __init__(self, name):   #konstruktor --> pozwala na wykonanie fragmentu kodu przy tworzeniu obiektu, możliwość stworzenia klasy, która przyjmuję warunki początkowe
#         self._name = name
#      @property                      #dekorator --> tworzenie chronionej zmiennej, przy pobieraniu wartości
#     def name(self):
#         return self._name           # 2 sposób to --> zwracanie
#
#     @name.setter                 #dekorator
#     def name(self, new_name):    #tworzenie metody(funkcja wewnątrz klasy) , self --> pozwala korzystać ze zmiennych i metod w innym miejscu klasy
#         self.name = new_name
#
#     def print_name(self):
#         print(self.name)          # 1 sposób to --> drukowanie
#
#
# class Cat(Animal):
#
#     def __init__(self, breed, name):
#         super().__init__(name)
#         self.breed = breed
#
#     def calculate_food(self, mass):
#         return mass * 7
#
# pajton = Animal("pajton")
#
#
#
# pajton = Cat("dachowiec", "Pajton")
# pajton.print_name()
# food_needed = pajton.calculate_food(4.5)
# print(f"Food needed: {pajton.calculate_food(4.5)}")
#
# my_animal = Animal("Reksio")       #obiekt na bazie klasy Animal musi być!!!!! () --> powoduję stworzenie nowego obiektu
# my_animal.set_a_name("Azor")            #wstawianie imienia
# my_animal.print_name()


class Person:

    def __init__(self, name, surname, year_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth

    def print_full_name(self):
       print(f"{self.name} {self.surname}")

    def get_age(self):
        age = 2023 - self.year_of_birth
        return age
    def change_surname(self, new_surname):
        self.surname = new_surname


class Student(Person):
    grades = []

    def __init__(self, name, surname, year_of_birth, grades=[]):  #podawanie argumentów opcjonalnych w metodach(domyślnie, pusty)
        super().__init__(name, surname, year_of_birth)
        self.grades = grades
    def add_grade(self, grade):
        self.grades.append(grade)   #metoda jest zdefiniowana, nic nie robi --> pass, append --> dodaje element na końcu listy

    def calculate_average(self):                         #liczenie średniej, round --> zaokrąglenie
        return round(sum(self.grades) / len(self.grades))



# andrzej = Student("Andrzej", "Testowy", 1999, [1, 1])
# andrzej.add_grade(5)
# andrzej.add_grade(4)
# print(andrzej.calculate_average())

# print(andrzej.name)
# print(andrzej._surname)                                   # _protect __private
# # andrzej.__year_of_birth
# print(andrzej._Person__year_of_birth)


# jan = Person("Jan", "Testowy", 1999 )
# jan.print_full_name()
# jan.change_surname("Nietestowy")
# jan.print_full_name()
# jan.get_age()
# print(jan.get_age())


