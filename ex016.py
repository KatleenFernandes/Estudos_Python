#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
'''from math import trunc
n=float(input('Digite um número: '))
t=trunc(n)
print('O número {} tem a parte inteira {}.'.format(n,t))'''
num=float(input('Digite um número: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num,int(num)))
