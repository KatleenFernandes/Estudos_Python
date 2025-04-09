#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
x=float(input('Digite o comprimento do cateto oposto: '))
y=float(input('Digite o comprimento do cateto adjacente: '))
h=hypot(x,y)
print('O comprimento da hipotenusa é {}.'.format(h))