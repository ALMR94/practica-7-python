# -*- coding: cp1252 -*-
"""Antonio Li Manzaneque- 1º DAW - Práctica 7 - Ejercicio 9 - Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si
riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman."""
palabra1=raw_input("Escríbeme una palabra: ")
palabra2=raw_input("Escríbeme otra palabra: ")
a=len(palabra1)
b=len(palabra2)
def rima(palabra1,palabra2):
        if palabra1[a-3:a] == palabra2[(b-3):b]:
                print "Las palabras",palabra1,"y",palabra2,"riman lo suyo."
        elif palabra1[a-2:a] == palabra2[b-2:b]:
                print "Las palabras",palabra1,"y",palabra2,"riman un pelín."
        else:
                print "Las palabras",palabra1,"y",palabra2,"no riman nada de nada."
rima(palabra1,palabra2)
