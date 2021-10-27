from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin

def testRezervare():
    rezervare = creeazaRezervare("121", "bravofly", "economy", 200, "da")

    assert getId(rezervare) == "121"
    assert getNume(rezervare) == "bravofly"
    assert getClasa(rezervare) == "economy"
    assert getPret(rezervare) == 200
    assert getCheckin(rezervare) == "da"