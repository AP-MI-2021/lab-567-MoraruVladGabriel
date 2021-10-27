from Domain.rezervare import getNume, getClasa, getId, getPret, getCheckin, creeazaRezervare

def majoClasa(nume, lista):
    """
    Trece toate rezervările făcute pe un nume citit la o clasă superioară.
    :param nume:numele citit
    :param lista:lista de rezervari
    :return:lista modificata
    """
    listaNoua = []
    for rezervare in lista:
        if getNume(rezervare) == nume:
            if getClasa(rezervare) == "economy":
                clasaNoua = "economy plus"
            elif  getClasa(rezervare) == "economy plus":
                clasaNoua = "business"
            else:
                clasaNoua = "business"
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                clasaNoua,
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def ieftinire(procentaj, lista):
    """
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    :param procentaj:procentajul citit, float
    :param lista:lista de rezervari
    :return:noua lista modificata.
    """
    listaNoua = []
    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare ) - getPret(rezervare) * procentaj / 100,
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua