
#------------------------------------------------------------------------------

# HLAVIČKA PROJEKTU
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Patricie Hermanová
email: patriciehermanova@gmail.com
"""
#------------------------------------------------------------------------------

# ZADÁNÍ PROJEKTU

# A/ program pozdraví užitele a vypíše úvodní text
# B/ program vytvoří tajné 4místné číslo 
    # (číslice musí být unikátní a nesmí začínat 0)
# C/ hráč hádá číslo. Program jej upozorní, 
    # pokud zadá číslo kratší nebo delší než 4 čísla, 
    # obsahovat duplicity, 
    # začínat nulou, 
    # obsahovat nečíselné znaky
# D/ program vyhodnotí tip uživatele
# E/ program dále vypíše počet 
    # bull/bulls (pokud uživatel uhodne jak číslo, tak jeho umístění)
    # cows/cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění)
    # Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. 
    # Tedy 1 bull a 2 bulls (stejně pro cow/cows)
#F/ zápis organizovaný do krátkých a přehledných funkcí.

#------------------------------------------------------------------------------

# Oddělovač
oddelovac = "-" * 50

###################################### KÓD ####################################

#importování knihovny random
import random

#------------------------------------------------------------------------------

#vytvoření tajného čísla (první čislice nesmí být nula, vždy unikátní)
def vygeneruj_tajne_cislo():
    cislice = list('0123456789')
    prvni_cislice = random.choice(cislice[1:])
    cislice.remove(prvni_cislice)
    tajne_cislo = prvni_cislice

    for _ in range(3):
        dalsi = random.choice(cislice)
        cislice.remove(dalsi)
        tajne_cislo += dalsi

    return tajne_cislo

#test funkce, pak zakomentovat
#tajne_cislo = vygeneruj_tajne_cislo()
#print("Tajné číslo:", tajne_cislo)

print(oddelovac)
#------------------------------------------------------------------------------

#kontrola správnosti formátu tipu (4 znaky, číslice, nezačína 0, unikátnost)
def spravny_format(tip):
    if len(tip) != 4:
        return False
    
    if not tip.isdigit():
        return False
    
    if tip[0] == "0":
        return False
    
    if len(set(tip)) != 4:
        return False
    
    return True

print(oddelovac)
#------------------------------------------------------------------------------

#znovuzadání tipu z důvodu nesprávného formátu
def ziskej_tip_od_hrace():
    while True:
        tip = input("Zadej svůj tip (4 různá čísla, nezačínej nulou): ")
        if spravny_format(tip):
            return tip
        else:
            print("Nesprávný formát! Zkus to znovu.")


#pozdrav a úvod
print("Ahoj, zahrajeme si hru bulls and cows!")
print("Hledej 4místné číslo, kombinace jsou unikátní a nezačínají nulou")

print(oddelovac)
#------------------------------------------------------------------------------

#tip od hráče
hracuv_tip = ziskej_tip_od_hrace()
print("Zadal jsi:", hracuv_tip)

print(oddelovac)
#------------------------------------------------------------------------------
