from Domain.rezervare import creeazaRezervare, getId, getPret

def adaugaRezervare(id, nume, clasa, pret, checkin, lista, undoLista = None, redoLista = None):
    """
    adauga o rezervare intr-o lista
    :param id:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :return:lista ce contine rezervarile vechi plus noua rezervare
    """
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if undoLista is not None and redoLista is not None:
        undoLista.append(lista)
        redoLista.clear()
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    if getPret(rezervare) < 0:
        raise ValueError("Pretul este negativ!")
    return lista + [rezervare]

def getById(id, lista):
    '''
    da rezervarea cu id-ul dat dintr-o lista
    :param id: string
    :param lista:lista
    :return: rezervarea cu id-ul dat
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None

def stergeRezervare(id, lista, undoLista = None, redoLista = None):
    """
    Sterge o rezervare din lista.
    :param id:string
    :param lista:lista de rezervari
    :return:lista fara rezervarea stearsa
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista nici o rezervare cu id-ul dat.")
    if undoLista is not None and redoLista is not None:
        undoLista.append(lista)
        redoLista.clear()
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def modificaRezervare(id, nume, clasa, pret, checkin, lista, undoLista = None, redoLista = None):
    """
    modifica o rezervare dupa id
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: lista cu rezervarea cu id-ul dat , modificata
    """
    if getById(id, lista) is None:
        raise ValueError("Nu exista nici o rezervare cu id-ul dat.")
    if undoLista is not None and redoLista is not None:
        undoLista.append(lista)
        redoLista.clear()
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua