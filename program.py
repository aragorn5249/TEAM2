#v1 +++
wiek =input("Podaj wiek uzytkownika")
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita")
wiek=int(wiek)
if wiek>=18 and wiek <=120:
    print("Witamy!")
elif wiek >120:
    exit("Alkohol szkodzi zdrowiu")
    print("Korzystaj z umiarem")
else:
    exit("Jestes za mlody")