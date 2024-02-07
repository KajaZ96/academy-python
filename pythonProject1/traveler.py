from basics.classes import Student             #importowanie klas/metod/funkcji/zmiennych, dpstęp do klasy z innego pliku


andrzej = Student("Andrzej", "Nietestowy", 1999)

assert andrzej.get_age() == 25, f"Andrzej has {andrzej.get_age()} years, not 25." #można zmienić komunikat błędu


fruits = ["apple", "orange"]

assert "apple" in fruits, ""


