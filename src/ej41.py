#!/usr/bin/python
#!encoding: UTF-8


def es_perfecto(n):
  for i in range(1,n):
    sumatorio = 0
    if n % i == 0:
      sumatorio +=i
  return sumatorio == n
  
#Nota: está mal el sumatorio puesto dentro del for y además si no "llamamos" a la función ni pedimos un número la terminal no va a hacer nada