# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 3 - Escribe un programa que lea una frase, y la pase como par�metro a un procedimiento, y �ste
debe mostrar la frase con un car�cter en cada l�nea."""
a = raw_input("Escribe una frase: ")
def caracterporlinea(a):
    b=len(a)
    i=1
    for i in range(b):
        print a[i:i+1]
        i+1
caracterporlinea(a)
