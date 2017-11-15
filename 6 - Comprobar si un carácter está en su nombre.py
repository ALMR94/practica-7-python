# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 6 - Escribe un programa que lea el nombre de una persona y un carácter, le pase estos datos a una
función que comprobará si dicho carácter está en su nombre. El resultado de dicha función lo
imprimirá el programa principal por pantalla."""
a = raw_input("Escríbe un nombre: ")
b = raw_input("Dime que carácter quieres que verifique: ")
def tienecaracter(b):
    c=a.count(b)
    if c>0:
        print "Sí, y además, el carácter",b,"está",c,"veces."
    else:
        print "No, ese carácter no está en el nombre."
tienecaracter(b)
