import random
x = 0
i = 0
while i < 3:
    a = random.randrange(1, 10, 1)
    b = random.randrange(1, 10, 1)
    с = int(input(f"{a} + {b} = "))
    if с == a + b:
        print("pravilno!")
        x = x + 1
    else:
        print("otvet ne verniy")
        i = i + 1
print(f"igra okonchena, pravilnih otvetov: {x}")


