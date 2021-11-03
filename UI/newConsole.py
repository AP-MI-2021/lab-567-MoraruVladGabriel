from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from UI.console import showAll

def printMenu():
    print("Comanda help: Cere ajutor.")
    print("Comanda add: Adauga rezervare: id, nume, clasa(economy/economy plus/business), pret, checkin(da/nu)")
    print("Comanda delete: Stergere rezervare: id")
    print("Comanda update: Modifica o rezervare: id ")
    print("Comanda showall: Afiseaza toate rezervarile.")
    print("Comanda stop: Oprire program.")



def printHelp():
    print(
        "In aceste meniu comenzile se dau separate prin ; si datele vor fi separate prin , ."
        "Un exemplu de comanda ar putea fi: add,1,andrei,business,100,da;showall"
    )
def runMenu(lista):

    while True:
        printMenu()
        comenzi = input("Introduceti comenzile separate prin ';', iar detaliitle pentru fiecare comanda prin ',': ")
        if comenzi == "stop":
            break

        comenzi = comenzi.split(";")

        for comanda in comenzi:
            comanda = comanda.split(",")
            lista_comanda = []
            for detalii in comanda:
                lista_comanda.append(detalii)
            if lista_comanda[0] == "add":
                try:
                    pret = float(lista_comanda[4])
                    lista = adaugaRezervare(lista_comanda[1], lista_comanda[2], lista_comanda[3], pret, lista_comanda[5], lista)
                except ValueError as ve:
                    print("Erpare: {}".format(ve))
            elif lista_comanda[0] == "delete":
                try:
                    lista = stergeRezervare(lista_comanda[1], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif lista_comanda[0] == "update":
                try:
                    lista = modificaRezervare(lista_comanda[1], lista_comanda[2], lista_comanda[3], lista_comanda[4], lista_comanda[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif lista_comanda[0] == "showall":
                showAll(lista)
            elif lista_comanda[0] == "help":
                printHelp()
            elif lista_comanda[0] == "stop":
                break
            else:
                print("Comanda nu este recunoscuta!")
