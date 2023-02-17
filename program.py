#v1 +++
wiek =input("Podaj wiek uzytkownika")
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita")
wiek=int(wiek)
if wiek>=18 and wiek <=40:
    print("Witay w naszym sklepi z alcocholem")
elif wiek >40:
    print("Witaj w naszym sklepue")
    print("Korzystaj z umiarem")
else:
    exit("Za mlody")