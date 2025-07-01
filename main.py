
#------------------------------------------------------------------------------

# HLAVIČKA PROJEKTU
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
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
def vygeneruj_tajne_cislo() -> str:
    """
    Vygeneruje náhodné 4místné číslo s unikátními číslicemi.
    První číslice není nula.
    """
    cislice = list('0123456789')
    prvni_cislice = random.choice(cislice[1:])
    cislice.remove(prvni_cislice)
    tajne_cislo = prvni_cislice

    for _ in range(3):
        dalsi = random.choice(cislice)
        cislice.remove(dalsi)
        tajne_cislo += dalsi

    return tajne_cislo

#tajne_cislo = vygeneruj_tajne_cislo()
#přesun z globálního prostoru do bloku if __name__ == "__main__" na konci kódu

#------------------------------------------------------------------------------

#kontrola správnosti formátu tipu (4 znaky, číslice, nezačína 0, unikátnost)
def spravny_format(tip: str) -> bool:
    """
    Zkontroluje, zda má tip správný formát:
    - 4 číslice
    - nezačíná nulou
    - obsahuje pouze čísla
    - číslice jsou unikátní
    """
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

#pozdrav a pravidla
def pozdrav_a_vysvetli():
    print(f"""
Ahoj, zahrajeme si hru Bulls and Cows!
Pravidla hry:
- hledej 4místné číslo
- bull znamená správná číslice na správné pozici
- cow znamená správná číslice, ale na špatné pozici
""")
    
pozdrav_a_vysvetli()

#------------------------------------------------------------------------------
#TOTO ZAKOMENTOVAT - zobrazení vygenerovaného čísla
#print(oddelovac)
#print("Vygenerované číslo je:", tajne_cislo)
#------------------------------------------------------------------------------

#získání, případně znovuzadání tipu z důvodu nesprávného formátu
def ziskej_tip_od_hrace():
    while True:
        tip = input("Zadej svůj tip (4 různá čísla, nezačínej nulou): ")
        if spravny_format(tip):
            return tip
        else:
            print(oddelovac)
            print("Nesprávný formát! Zkus to znovu.\n" + oddelovac)

print(oddelovac)
#------------------------------------------------------------------------------

#porovnání tajného čísla a tipu od hráče
#bull = správná číslice na správné pozici
#cow = číslice existuje v tajném čísle, ale na jiné pozici

def porovnej_cisla(tajne_cislo, tip):
    bulls = 0
    cows = 0

    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    
    return bulls, cows

while True:
    hracuv_tip = ziskej_tip_od_hrace()
    print(oddelovac)
    print("Zadal jsi:", hracuv_tip)

    bulls, cows = porovnej_cisla(tajne_cislo, hracuv_tip)

    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"

    print(f"{bulls} {bull_text}, {cows} {cow_text}")
    print(oddelovac)

    if bulls == 4:
        print("Juhuu, uhodl jsi!")
        break

