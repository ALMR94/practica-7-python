# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 2 - Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de
caracteres diferentes), los pase como par�metros a una funci�n, y �sta debe unirlos y devolver
una �nica cadena. La cadena final la imprimir� el programa por pantalla."""
a = raw_input("Dime tu nombre: ")
b = raw_input("Dime tu 1� apellido: ")
c = raw_input("Dime tu 2� apellido: ")
def nomcomplet(a,b,c):
    d=a.title()
    e=b.title()
    f=c.title()
    print d,e,f
print "Tu nombre completo es:"
nomcomplet(a,b,c)
