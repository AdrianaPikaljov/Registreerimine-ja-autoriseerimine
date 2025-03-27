# list.append(x) Добавляет элемент в конец списка
# list.extend(L) Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x) Вставляет на i-ый элемент значение x
# list.remove(x) Удаляет первый элемент в списке, имеющий значение x
# list.pop(i) Удаляет i-ый элемент и возвращает его. Если индекс не указан,
# удаляется последний элемент
# list.index(x, [start [, end]]) Возвращает положение первого элемента от start до end со значением x
# list.count(x) Возвращает количество элементов со значением x
# list.sort([key = функция]) Сортирует список на основе функции
# list.reverse() Разворачивает список
# list.copy() Копия списка
# list.clear() Очищает список

users_list = ["adri"]  # Kasutajate nimekiri, kus hoiame kõiki registreeritud kasutajate sisselogimisi
parool_list = ["ADRIIIlol228,."]  # Paroolide nimekiri, kus hoiame kõigi kasutajate paroole

import random

def kusimus(vastus: str) -> bool:
    """Vastus jah või ei.
    Kui kasutaja sisestab "jah", tagastab funktsioon False.
    Kui kasutaja sisestab "ei", tagastab funktsioon True.
    
    :param str vastus: Sisend, milleks kasutaja sisestab kas "jah" või "ei".
    :rtype: bool: Tagastab kas True või False vastavalt kasutaja sisestusele
    """
    if vastus == "ei":  # Kui vastus on "ei", tagastame True
        vastus = True
    else:  # Kõik muud vastused (nt "jah") tagastavad False
        vastus = False
    return vastus

def sis(sisse: str) -> bool:
    """Kontrollib, kas kasutaja sisselogimise nimi on juba süsteemis.
    
    :param str sisse: Kasutaja sisestatud sisselogimine
    :rtype: bool: Tagastab True, kui kasutaja on olemas, vastasel juhul False
    """
    if sisse in users_list:
        vas = True  # Kasutaja on süsteemis olemas
    else:
        vas = False  # Kasutaja pole süsteemis
    return vas

def pasword(parool: str) -> bool:
    """Kontrollib, kas parool on olemas süsteemis.
    
    :param str parool: Kasutaja sisestatud parool
    :rtype: bool: Tagastab True, kui parool on süsteemis, vastasel juhul False
    """
    if parool in parool_list:
        vaspar = True  # Parool on olemas
    else:
        vaspar = False  # Parool ei ole süsteemis
    return vaspar

def kontr_pasword(login: str, parool: str) -> bool:
    """Kontrollib, kas kasutajanimi ja parool vastavad süsteemis olevatele andmetele.
    
    :param str login: Kasutaja sisestatud sisselogimine
    :param str parool: Kasutaja sisestatud parool
    :rtype: bool: Tagastab True, kui nii kasutajanimi kui parool on õiged
    """
    if login in users_list:  # Kui kasutajanimi on olemas süsteemis
        lol = users_list.index(login)  # Leiame selle kasutajanime asukoha
        vaslog = parool_list[lol] == parool  # Kontrollime, kas parool vastab
    else:
        vaslog = False  # Kui kasutajat pole, siis ei saa parool ka õige olla
    return vaslog

def kusimusparo(zabyl: str) -> bool:
    """Küsimus "kas unustasid parooli?".
    Kui kasutaja sisestab "jah", tagastab funktsioon True.
    Kui kasutaja sisestab "ei", tagastab funktsioon False.
    
    :param str zabyl: Kasutaja sisestatud vastus ("jah" või "ei")
    :rtype: bool: Tagastab True või False vastavalt kasutaja vastusele
    """
    if zabyl == "jah":
        vaszabyl = True  # Kui vastus on "jah", tagastame True
    else:
        vaszabyl = False  # Kõik muud vastused (nt "ei") tagastavad False
    return vaszabyl

def parooli_muutus(login: str, parool: str) -> bool:
    """Muudab kasutaja parooli.
    Kui kasutaja sisestab õiged andmed, siis uuendatakse tema parool süsteemis.
    
    :param str login: Kasutaja sisestatud sisselogimine
    :param str parool: Kasutaja uus parool
    :rtype: bool: Tagastab True, kui parool edukalt muudeti, vastasel juhul False
    """
    if login in users_list:  # Kui kasutaja on olemas süsteemis
        lol = users_list.index(login)  # Leiame selle kasutaja asukoha
        parool_list[lol] = parool  # Uuendame parooli
        vasparmuut = True  # Parool muudeti edukalt
    else:
        vasparmuut = False  # Kui kasutaja pole olemas, ei saa parooli muuta
    return vasparmuut

def kontr_parool(parool) -> bool:
    """Kontrollib, kas parool vastab nõuetele: vähemalt 8 tähemärki,
    mis sisaldavad suuri tähti, numbreid või erimärke.
    
    :param str parool: Sisestatud parool, mida kontrollitakse
    :return: True, kui parool vastab kõigile nõuetele, vastasel juhul False
    """
    str_list = list(".,:;!_*-+()/#¤%&")  # Erimärkide nimekiri
    
    password_ = []  # Muutuja, kuhu salvestame kõik kehtivad märgid (suur täht, number, erimärk)
    
    # Läbime kõik parooli tähemärgid ja kontrollime, kas need vastavad nõuetele
    for i in parool:
        if i.isupper() or i.isdigit() or i in str_list:
            password_ += i  # Lisame kehtivad märgid
            
    # Kontrollime, kas parool sisaldab vähemalt 8 tähemärki, mis vastavad nõuetele
    if len(password_) >= 8:
        return True  # Kui parool vastab nõuetele, tagastame True
    else:
        return False  # Kui parool on liiga lühike või ei vasta nõuetele, tagastame False

def newkasutaja(login: str, parool: str) -> bool:
    """Registreerib uue kasutaja süsteemi.
    Kui kasutajanimi pole veel olemas, lisatakse see süsteemi koos parooliga.
    
    :param str login: Kasutaja sisestatud sisselogimine
    :param str parool: Kasutaja sisestatud parool
    :rtype: bool: Tagastab True, kui uus kasutaja edukalt registreeriti, vastasel juhul False
    """
    if login in users_list:  # Kui kasutajanimi on juba olemas
        vasreg = False  # Ei saa registreerida, kuna nimi on juba kasutusel
    else:
        users_list.append(login)  # Lisame uue kasutajanime
        parool_list.append(parool)  # Lisame parooli vastavale kasutajale
        vasreg = True  # Kasutaja on edukalt registreeritud
    return vasreg
