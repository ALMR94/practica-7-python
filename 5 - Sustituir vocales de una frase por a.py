# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 5 - Escribe un programa que te pida una frase y una vocal, y pase estos datos como parámetro a una
función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada."""
a = raw_input("Escríbeme algo: ")
b = raw_input("Dime la vocal que más rabia te dé: ")
def sustituirvocales(a):
    for c in a:
        if c in "aeiou":
            a = a.replace(c,b)
    return a
print sustituirvocales(a)
