#!/usr/bin/python
#!encoding: UTF-8

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if a != 0:
  x = -b/a
  print 'Solucion: ', x
else: 
  print 'La ecuacion no tiene solucion'
  
  
#Nota: el error estaba en el else; el ej. nos daba dos if, y siempre que hay un if el otro caso debe ser un else.