from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)

    assert len(lista) == 1
    assert getId(getById("121", lista)) == "121"
    assert getNume(getById("121", lista)) == "bravofly"
    assert getClasa(getById("121", lista)) == "economy"
    assert getPret(getById("121", lista)) == 200
    assert getCheckin(getById("121", lista)) == "da"

def testStergeRezervare():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)

    lista = stergeRezervare("121", lista)

    assert len(lista) == 1
    assert getById("121", lista) is None
    assert getById("111", lista) is not None

def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("121", "bravofly", "economy", 200, "da", lista)
    lista = adaugaRezervare("111", "airbus", "economy plus", 150, "da", lista)

    lista = modificaRezervare("121", "airbus", "economy plus", 250, "da", lista)

    rezervareUpdatata = getById("121", lista)

    assert getId(rezervareUpdatata) == "121"
    assert getNume(rezervareUpdatata) == "airbus"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 250
    assert getCheckin(rezervareUpdatata) == "da"

    rezervareNeupdatata = getById("111", lista)

    assert getId(rezervareNeupdatata) == "111"
    assert getNume(rezervareNeupdatata) == "airbus"
    assert getClasa(rezervareNeupdatata) == "economy plus"
    assert getPret(rezervareNeupdatata) == 150
    assert getCheckin(rezervareNeupdatata) == "da"