a = 10     #jeżeli, jeden warunek się nie spełni/spełni to kolejne nie są weryfikowane
b = 0
if a > 0:
    print("Value is positive")
elif a == 0:
    print("Value is zero")
elif a < 0:
    print("Value is negative")
else:
    print("Something went wrong")

if a > 0 and b > 0:
    print("Both values positive")
elif a > 0 or b > 0:
    print("One value is positive")

# if not - negacja

a = True                              #jeśli a jest prawdą
if a:                                 # 0, (), [], {} "", None --> False
    print("This is True")
else:
    print("This is False")


<= za darmo
> 100 



