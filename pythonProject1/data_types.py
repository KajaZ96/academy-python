a_int = 1  # no max/min value
a_float = 1.1 # no limit
int(a_float)

a_str = "[id='login']"
a_str2 = '[id="login"]'
print(a_str[0])

a_list = [0, 1, 2, "test", [1, 2]] # ordered, mutable, not uniqe
print(a_list[3])
print(a_list[-1])
a_list[0] = 100
print(a_list)
a_list.append(10)
print(a_list)

a_tuple = (0, 1, 2, 0, "test") # ordered, immutable, value not uniqua
print(a_tuple[-1])

a_dict = { # unordered - nieuporządkowane, mutable, unique keys (klucz: wartosc)
    "name" : "Klaudia",
    "city" : "Zyrardow",
    "weight": 47,
    "0": "admin",
    1: "moderator"
}

print(a_dict["city"])
print(a_dict["0"])
print(a_dict)
a_dict["city"] = "Warszawa"
a_dict["job"] = "QA"
print(a_dict)

a_set = {3, 2, 0, 0} # unordered, mutable, unique values
b_set = [0, 5, 10]
print(a_set)
a_set.add(10)
print(a_set)
print(a_set.intersection(b_set))

a_bool = True

a_none = None  #null, nil

pajton = {
    "type": "cat",
    "age": 4,
    "weight": 4.5,
    "sleeping_places": ["bed", "box", "heather", "everywhere"],
    "colors": ("white", "grey", "brown"),
    "is_alive": True
}

hobby = "food"
lenght = 20
str_to_print = "I like " + hobby + " a lot. I practice it for " + str(lenght) + " years."  #mapowanie str
print(str_to_print)

str_to_print = "I like {} a lot. I practice it for {} years.".format(hobby, lenght) #interpulacja, nadpisywanie wartości
print(str_to_print)

str_to_print = f"I like {hobby} a lot. I practice it for {lenght} years."  #wstrzykiwanie zmiennych, tylko zdefiniowane
print(str_to_print)


str_to_print1 = "My " + pajton["type"] + " has " + str(pajton["age"]) + " years. "
print(str_to_print1)

str_to_print1 = "My {} has {} years.".format(pajton["type"], pajton["age"])
print(str_to_print1)

str_to_print1 = f"My {pajton['type']} has {pajton['age']} years."
print(str_to_print1)

