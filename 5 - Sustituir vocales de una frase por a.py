# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 5 - Escribe un programa que te pida una frase y una vocal, y pase estos datos como par�metro a una
funci�n que se encargar� de cambiar todas las vocales de la frase por la vocal seleccionada."""
a = raw_input("Escr�beme algo: ")
b = raw_input("Dime la vocal que m�s rabia te d�: ")
def sustituirvocales(a):
    for c in a:
        if c in "aeiou":
            a = a.replace(c,b)
    return a
print sustituirvocales(a)
