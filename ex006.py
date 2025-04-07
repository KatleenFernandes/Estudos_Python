#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1=float(input('Digite um número: '))
d=n1*2
t=n1*3
r=n1**(1/2)
print('Considerando o número {:.0f}, seu dobro é {:.0f}, seu triplo é {:.0f} e sua raiz quadrada é {:.0f}'.format(n1,d,t,r))
#Ele vai considerar o arrendondamento de números quebrados como usualmente consideramos. O 7.5 é 8 e o 7.3 é 7;
