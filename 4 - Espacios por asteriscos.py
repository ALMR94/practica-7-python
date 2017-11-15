# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 4 - Escribe un programa que pida una frase, y le pase como parámetro a una función dicha frase. La
función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el
resultado para que el programa principal la imprima por pantalla."""
a = raw_input("Escribe una frase: ")
def espaciosporasteriscos(a):
    alista=a.split()
    fraseast="*".join(alista)
    return fraseast
print espaciosporasteriscos(a)
