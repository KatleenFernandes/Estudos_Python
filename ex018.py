#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
a=int(input('Digite o ângulo: '))
r=radians(a)
print('O seno de {}º é {:.2f}º.\nO cosseno de {}º é {:.2f}º.\nA tangente de {}º é {:.2f}º.'.format(a,sin(r),a,cos(r),a,tan(r)))

