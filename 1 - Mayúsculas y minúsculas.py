# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 1 - Escribe un programa que pida un texto por pantalla, este texto lo pase como par�metro a un
procedimiento, y �ste lo imprima primero todo en min�sculas y luego todo en may�sculas."""
a = raw_input("Escribe una frase: ")
def mayusminus(a):
    b=a.lower()
    c=a.upper()
    print b
    print c
mayusminus(a)
