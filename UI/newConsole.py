from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from UI.console import showAll
from Logic.functionalitati import undocmd, redocmd


def printMenu():
    print("Comanda help: Cere ajutor.")
    print("Comanda add: Adauga rezervare: id, nume, clasa(economy/economy plus/business), pret, checkin(da/nu)")
    print("Comanda delete: Stergere rezervare: id")
    print("Comanda update: Modifica o rezervare: id, nume, clasa(economy/economy plus/business), pret, checkin(da/nu) ")
    print("Comanda showall: Afiseaza toate rezervarile.")
    print("Comanda undo.")
    print("Comanda redo")
    print("Comanda stop: Oprire program.")


def printHelp():
    print(
        "In acest meniu comenzile se dau separate prin ; si datele vor fi separate prin , ."
        "Un exemplu de comanda ar putea fi: add,1,andrei,business,100,da;showall"
    )


def runMenu(lista):
    undoLista = []
    redoLista = []
    printMenu()
    while True:
        comenzi = input("Introduceti comenzile separate prin ';', iar detaliile pentru fiecare comanda prin ',': ")
        if comenzi == "stop":
            break

        comenzi = comenzi.split(";")

        for comanda in comenzi:
            comanda = comanda.split(",")
            lst_cmd = []
            for detalii in comanda:
                lst_cmd.append(detalii)
            if lst_cmd[0] == "add":
                try:
                    pret = float(lst_cmd[4])
                    undoLista.append(lista)
                    redoLista.clear()
                    lista = adaugaRezervare(lst_cmd[1], lst_cmd[2], lst_cmd[3], pret, lst_cmd[5], lista)
                except ValueError as ve:
                    print("Erpare: {}".format(ve))
            elif lst_cmd[0] == "delete":
                try:
                    undoLista.append(lista)
                    redoLista.clear()
                    lista = stergeRezervare(lst_cmd[1], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif lst_cmd[0] == "update":
                try:
                    undoLista.append(lista)
                    redoLista.clear()
                    lista = modificaRezervare(lst_cmd[1], lst_cmd[2], lst_cmd[3], lst_cmd[4], lst_cmd[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif lst_cmd[0] == "showall":
                showAll(lista)
            elif lst_cmd[0] == "undo":
                if len(undoLista) == 0:
                    print('Nu se poate face undo!')
                lista = undocmd(lista, undoLista, redoLista)
            elif lst_cmd[0] == "redo":
                if len(redoLista) == 0:
                    print('Nu se poate face redo!')
                lista = redocmd(lista, undoLista, redoLista)
            elif lst_cmd[0] == "help":
                printHelp()
            elif lst_cmd[0] == "stop":
                break
            else:
                print("Comanda nu este recunoscuta!")
