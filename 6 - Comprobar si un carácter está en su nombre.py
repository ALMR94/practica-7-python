# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 6 - Escribe un programa que lea el nombre de una persona y un car�cter, le pase estos datos a una
funci�n que comprobar� si dicho car�cter est� en su nombre. El resultado de dicha funci�n lo
imprimir� el programa principal por pantalla."""
a = raw_input("Escr�be un nombre: ")
b = raw_input("Dime que car�cter quieres que verifique: ")
def tienecaracter(b):
    c=a.count(b)
    if c>0:
        print "S�, y adem�s, el car�cter",b,"est�",c,"veces."
    else:
        print "No, ese car�cter no est� en el nombre."
tienecaracter(b)
