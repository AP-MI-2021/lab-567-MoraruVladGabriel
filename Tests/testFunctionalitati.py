from Logic.CRUD import adaugaRezervare, getById
from Domain.rezervare import getClasa, getPret, getId
from Logic.functionalitati import majoClasa, ieftinire, determPretMaximClasa, ordonareDescDupaPret, sumaPretNume


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


def testDetermPretMaximClasa():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 179, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)
    lista = adaugaRezervare("456", "bravofly", "economy", 176, "da", lista)
    lista = adaugaRezervare("458", "bravofly", "economy", 200, "nu", lista)

    rezultat = determPretMaximClasa(lista)

    assert len(rezultat) == 2
    print(rezultat["economy"])
    assert rezultat["economy"] == 200
    assert rezultat['economy plus'] == 150


def testOrdonareDescDupaPret():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)
    lista = adaugaRezervare("456", "bravofly", "economy", 176, "da", lista)
    lista = adaugaRezervare("458", "bravofly", "economy", 177, "nu", lista)

    rezultat = ordonareDescDupaPret(lista)

    assert getId(rezultat[0]) == "121"
    assert getId(rezultat[1]) == "458"
    assert getId(rezultat[2]) == "456"
    assert getId(rezultat[3]) == "111"


def testSumaPretNume():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)
    lista = adaugaRezervare("456", "bravofly", "economy", 100, "da", lista)
    lista = adaugaRezervare("458", "bravofly", "economy", 100, "nu", lista)

    rezultat = sumaPretNume(lista)

    assert len(rezultat) == 2
    assert rezultat["bravofly"] == 400
    assert rezultat["airbus"] == 150