a = ""
while True:
    c = str(input("vvedite slovo"))
    if c == "stop":
        break
    else:
        a = a + c + " "

print(a)