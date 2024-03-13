a = ""
while True:
    c = str(input("vvedite slovo"))
    a = a + c + " "
    x = input("vvedite 1 esli prodoljaem, drugoe znachenie esli stop")
    if x != "1":
        break


print(a)

