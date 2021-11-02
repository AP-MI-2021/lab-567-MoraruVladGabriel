def creeazaRezervare(id, nume, clasa, pret, checkin):
    """
    Creaza un dictionar ce reprezinta o rezervare.
    :param id: string.
    :param nume:string.
    :param clasa:string.
    :param pret:float.
    :param checkin:string.
    :return:un dictionar ce contine o rezervare.
    """
    if clasa != "economy" and clasa != "economy plus" and clasa != "business":
        raise ValueError("Clasa nu este una dintre economy/economy plus/business!")
    if checkin != "da" and checkin != "nu":
        raise ValueError("Checkin-ul nu este de forma da/nu!")
    return {
        'id': id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin": checkin
    }

def getId(rezervare):
    """
    da id-ul unei rezervari.
    :param rezervare: dictionar ce contine o rezervare
    :return: id-ul rezervarii
    """
    return rezervare['id']

def getNume(rezervare):
    """
    da numele unei rezervari.
    :param rezervare: dictionar ce contine o rezervare
    :return: numele rezervarii
    """
    return rezervare["nume"]

def getClasa(rezervare):
    """
    da clasa unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: clasa rezervarii
    """
    return rezervare["clasa"]

def getPret(rezervare):
    """
    da pretul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: pretul rezervarii
    """
    return rezervare["pret"]

def getCheckin(rezervare):
    """
    da checkin-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: checkin-ul rezervarii
    """
    return rezervare["checkin"]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )