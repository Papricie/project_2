
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
    # pokud bude obsahovat duplicity, začínat nulou, 
    # příp. obsahovat nečíselné znaky
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