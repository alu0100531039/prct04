#!/usr/bin/python
#!encoding: UTF-8

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

x=-b/a

print 'solucion: ', x


#Nota: una corrección del ejercicio, para exigir a distinto de 0 sería la siguiente
#   if (a != 0):
#       x = -b/a
#       print 'Solucion: ', x
#   else:
#       print 'Error, el valor de a debe ser distinto de 0'