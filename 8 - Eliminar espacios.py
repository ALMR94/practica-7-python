# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 8 - Escribe un programa que pida una frase, y pase la frase como parámetro a una función que debe
eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá por pantalla el resultado final."""
frase=raw_input("Escríbeme algo: ")
def frasesinespacios(frase):
	frase2=frase.replace(' ', '')
	return frase2
print "Aquí lo tienes sin espacios:",frasesinespacios(frase)
