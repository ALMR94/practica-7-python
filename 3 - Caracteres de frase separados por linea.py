# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 3 - Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento, y éste
debe mostrar la frase con un carácter en cada línea."""
a = raw_input("Escribe una frase: ")
def caracterporlinea(a):
    b=len(a)
    i=1
    for i in range(b):
        print a[i:i+1]
        i+1
caracterporlinea(a)
