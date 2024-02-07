my_text = "Ala ma kota\n " #\n nowa linia

stripped_text = my_text.strip()   #zostawi tylko kontend
print(stripped_text)

splitted_text = my_text.split()  #podzieli tekst --> tworzy tablicę
print(splitted_text)

replaced_text = my_text. replace("","")  #podmienia znaki
print(replaced_text)

joined_text = "".join(splitted_text)    #łączenie tekstu
print(joined_text)

upper_tekst = my_text.upper()  #zmiana na duże litery
print(upper_tekst)

full_name = "jan jans"
names = full_name.split()
print(names)
name = names [0].capitalize()
surname = names [1].capitalize()
print(f"{name} {surname}")