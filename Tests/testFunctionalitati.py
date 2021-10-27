from Logic.CRUD import adaugaRezervare, getById
from Domain.rezervare import getClasa, getPret
from Logic.functionalitati import majoClasa, ieftinire

def testaMajoClasa():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)
    lista = adaugaRezervare("456", "bravofly", "economy", 176, "da", lista)

    lista = majoClasa("bravofly", lista)

    assert getClasa(getById("121", lista)) == "economy plus"
    assert getClasa(getById("111", lista)) == "economy plus"
    assert getClasa(getById("456", lista)) == "economy plus"

def testIeftinire():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)
    lista = adaugaRezervare("456", "bravofly", "economy", 176, "da", lista)
    lista = adaugaRezervare("458", "bravofly", "economy", 176, "nu", lista)


    lista = ieftinire(25, lista)

    assert getPret(getById("121", lista)) == 150
    assert getPret(getById("111", lista)) == 112.5
    assert getPret(getById("456", lista)) == 132
    assert getPret(getById("458", lista)) == 176