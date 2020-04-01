# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:44:40 2019

@author: b20a
"""
import math

print("Vamos resolver uma equação de 2 grau? y= ax2 + bx + c")
a=int(input( "Qual o valor de a?"))
b = int(input("Qual o valor de b?"))
c = int(input( "Qual o valor de c?"))

delta = (b**2)-(4*a*c)

if delta = 0:
    x = -b/(2a)
    print(" Sua função só tem uma raiz", x)

if delta <0:
    print (" Sua função é complexa... se fudeu")
    
if delta >0:
    raizDelta = math.sqrt(delta)
    x1 = ((-b)+(raizDelta))/(2a)
    x2 = ((-b)-(raizDelta))/(2a)
    print ( " Suas raizes são reais e são:", x1 "," X2)