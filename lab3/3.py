a = input("vvedite slovo")
if len(a) > 0 and a.isalpha():
    if "f" in a:
        print("eto redkoye slovo!")
    else:
        print("eto ne redkote slovo...")
else:
    print("nekorrektnoye znachenie")
