from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitati import majoClasa, ieftinire, determPretMaximClasa, ordonareDescDupaPret, sumaPretNume


def printMenu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("4. Trece toate rezervările făcute pe un nume citit la o clasă superioară")
    print("5. Ieftineste toate rezervările la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determina pretul maxim pentru fiecare clasa.")
    print("7. Ordoneaza rezervarile descrescator dupa pret.")
    print("8. Afiseaza sumele prețurilor pentru fiecare nume.")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa(economy/economy plus/business): ")
        pret = float(input("Dati pretul: "))
        checkin = input("Dati checkin-ul(da/nu): ")
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergereRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Dati noul checkin: ")
        return modificaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiMajoClasa(lista):
    try:
        nume = input("Dati numele: ")
        return majoClasa(nume, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiIeftinire(lista):
    try:
        procentaj = float(input("Dati procentajul: "))
        return ieftinire(procentaj, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiDetermPretMaximClasa(lista):
    rezultat = determPretMaximClasa(lista)
    for clasa in rezultat:
        print("Pretul maxim la clasa {} este: {}".format(clasa, rezultat[clasa]))


def uiOrdonareDescDupaPret(lista):
    showAll(ordonareDescDupaPret(lista))


def uiAfisareSumaPretNume(lista):
    rezultat = sumaPretNume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor: {}".format(nume, rezultat[nume]))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergereRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiMajoClasa(lista)
        elif optiune == "5":
            lista = uiIeftinire(lista)
        elif optiune == "6":
            uiDetermPretMaximClasa(lista)
        elif optiune == "7":
            uiOrdonareDescDupaPret(lista)
        elif optiune == "8":
            uiAfisareSumaPretNume(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita!Reincercati.")
