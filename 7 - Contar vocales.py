# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1� DAW - Pr�ctica 7 - Ejercicio 7 - Escribe un programa que lea una frase, y la pase como par�metro a un procedimiento. El
procedimiento contar� el n�mero de vocales (de cada una) que aparecen, y lo imprimir� por pantalla."""
def vocales(frase):
	vocales = {"a":"�", "e":"�", "i":"�", "o":"�", "u":"�"}
	minusculas = frase.lower()
	res = 0
	for v,a in vocales.items():
		cant = minusculas.count(v)+minusculas.count(a)
		res += cant
		print "%s -> %s" % (v.upper(),cant)
	print "TOTAL -> %s" % res
frase = raw_input('Escribe una frase: ')
vocales(frase)
