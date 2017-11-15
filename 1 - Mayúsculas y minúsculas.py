# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 1 - Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un
procedimiento, y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas."""
a = raw_input("Escribe una frase: ")
def mayusminus(a):
    b=a.lower()
    c=a.upper()
    print b
    print c
mayusminus(a)
