# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 8 - Escribe un programa que pida una frase, y pase la frase como par�metro a una funci�n que debe
eliminar los espacios en blanco (compactar la frase). El programa principal imprimir� por pantalla el resultado final."""
frase=raw_input("Escr�beme algo: ")
def frasesinespacios(frase):
	frase2=frase.replace(' ', '')
	return frase2
print "Aqu� lo tienes sin espacios:",frasesinespacios(frase)
