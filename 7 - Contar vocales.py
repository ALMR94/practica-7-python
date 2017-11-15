# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 7 - Escribe un programa que lea una frase, y la pase como parámetro a un procedimiento. El
procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla."""
def vocales(frase):
	vocales = {"a":"á", "e":"é", "i":"í", "o":"ó", "u":"ú"}
	minusculas = frase.lower()
	res = 0
	for v,a in vocales.items():
		cant = minusculas.count(v)+minusculas.count(a)
		res += cant
		print "%s -> %s" % (v.upper(),cant)
	print "TOTAL -> %s" % res
frase = raw_input('Escribe una frase: ')
vocales(frase)
