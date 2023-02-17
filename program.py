#v1 +++
wiek =input("Podaj wiek uzytkownika\n")
plec = int(input("Podaj plec\n"))
if wiek >=30 and plec =="kobieta":
    print("Pierwszy aperol spiritz gratis")
else:
    exit("Niestety nie przysługują ci gratisy")
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita")
wiek=int(wiek)
if wiek>=18 and wiek <=120:
    print("Witamy!")
elif wiek >120:
    exit("Alkohol szkodzi zdrowiu")
    print("Korzystaj z umiarem")
else:
    exit("Za mlody")
