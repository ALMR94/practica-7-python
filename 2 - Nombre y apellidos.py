# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 2 - Escribe un programa que lea el nombre y los dos apellidos de una persona (en tres cadenas de
caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos y devolver
una única cadena. La cadena final la imprimirá el programa por pantalla."""
a = raw_input("Dime tu nombre: ")
b = raw_input("Dime tu 1º apellido: ")
c = raw_input("Dime tu 2º apellido: ")
def nomcomplet(a,b,c):
    d=a.title()
    e=b.title()
    f=c.title()
    print d,e,f
print "Tu nombre completo es:"
nomcomplet(a,b,c)
