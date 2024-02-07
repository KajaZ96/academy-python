my_text = "Ala ma kota"
#text_lower = my_text.lower()
vowels = ["a", "e", "i", "o", "y", "u"]

counter = 0
for letter in my_text.lower():             #jeśli litera jest w tekście
    if letter in vowels:
       counter += 1
print(counter)