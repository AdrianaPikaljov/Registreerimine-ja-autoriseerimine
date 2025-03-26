from moduldef1 import *
import random

vastus_list = ["jah", "ei"]
print("Tere tulemast!")

while True:
    vastus = input("Kas olete registreeritud? (jah/ei): ").lower()
    if vastus in vastus_list:
        break
    print("Vastus peab olema ainult 'jah' või 'ei'!")

if kusimus(vastus):  # Kui vastus on "ei", siis registreerime kasutaja
    while True:
        login = input("Sisesta oma kasutajanimi: ")
        if sis(login):
            print("See kasutajanimi on juba hõivatud, sisesta teine!")
        else:
            break
    
    while True:
        vastus1 = input("Genereerida parool? (jah/ei): ").lower()
        if vastus1 in vastus_list:
            break
        print("Vastus peab olema ainult 'jah' või 'ei'!")
        if kusimus(vastus1):
            parool = parooli_muutus()
            print(f"Sinu parool: {parool}")
    else:
        while True:
            parool = input("Sisesta oma parool: ")
            if kontr_parool(parool):
                break
            print("Parool peab olema vähemalt 8 tähemärki pikk ning sisaldama numbreid, väikeseid ja suuri tähti ning erimärke!")
    
    newkasutaja(login, parool)
    print("Sa oled registreeritud!")

while True:
    vastus = input("Kas sa tahad sisse logida? (jah/ei): ").lower()
    if vastus not in vastus_list:
        print("Vastus peab olema ainult 'jah' või 'ei'!")
        continue
    
    if vastus == "ei":
        break
    
    while True:
        login = input("Sisesta oma kasutajanimi: ")
        if sis(login):
            break
        print("Seda kasutajanime ei ole nimekirjas!")
    
    while True:
        parool = input("Sisesta oma parool: ")
        if kontr_pasword(login, parool):
            print("Sa oled süsteemi sisse loginud!")
            break
        print("Parool ei sobi! Proovi uuesti.")
