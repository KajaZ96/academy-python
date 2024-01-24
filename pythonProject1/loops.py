for i in range(1, 11):  #iterowanie przedział, wykona się tyle razy ile jest elementów w liście
    print(i)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:     #fruit - zmienna   #iterowanie po elementach z listy
    print(fruit)


a = 0
while a < 10:                      #pętla sprawdza warunek, może być nieskończona
    print(a)
    a += 1

b = 0
while True:                            #wykonuj cały czas, dopiero jak spełni się warunek zatrzymaj
    print(b)
    if b > 10:
        break
    b += 1


for i in range(10, 100, 2):            #początek, koniec i krok
    print(i)

a = 10
while a < 100:
    print(a)
    a += 2

n = 4     #silnia 1*2*3*4
if n == 0:                               #
    result = 1
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
print(f"Factorial from {n} equals {result}")


