from Domain.rezervare import getNume, getClasa, getId, getPret, getCheckin, creeazaRezervare


def majoClasa(nume, lista):
    """
    Trece toate rezervările făcute pe un nume citit la o clasă superioară.
    :param nume:numele citit
    :param lista:lista de rezervari
    :return:lista modificata
    """

    ok = 0
    for rezervare in lista:
        if getNume(rezervare) == nume:
            ok = 1
            break
    if ok == 0:
        raise ValueError("Nu exista nici o rezervare pe numele dat.")

    listaNoua = []
    for rezervare in lista:
        if getNume(rezervare) == nume:
            if getClasa(rezervare) == "economy":
                clasaNoua = "economy plus"
            elif getClasa(rezervare) == "economy plus":
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
    if procentaj > 100 or procentaj < 0:
        raise ValueError("Procentajul trebuie sa fie cuprins intre 0 si 100.")
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

def determPretMaximClasa(lista):
    """
    Determina pretul maxim pentru fiecare clasa.
    :param lista: lista de rezervari.
    :return: un dictionar
    """
    rezultat = {}
    for rezervare in lista:
        clasa = getClasa(rezervare)
        pret = getPret(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat


def ordonareDescDupaPret(lista):
    '''
    Ordoneaza rezervarile descrescator dupa pret.
    :param lista:lista de rezervari.
    :return:lista ordonata descrescator dupa pret.
    '''
    return sorted(lista, key=lambda rezervare: getPret(rezervare), reverse=True)


def sumaPretNume(lista):
    """
    Determina suma preturilor pentru fiecare nume.
    :param lista: lista rezeervarilor
    :return: un dictionar
    """
    rezultat = {}
    for rezervare in lista:
        pret = getPret(rezervare)
        nume = getNume(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat