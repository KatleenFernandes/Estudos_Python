#Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dele e escrevendo o nome escolhido.
import random
a=input('Digite o nome do primeiro aluno: ')
b=input('Digite o nome do segundo aluno: ')
c=input('Digite o nome do terceiro aluno: ')
d=input('Digite o nome do quarto aluno: ')
s=random.choice([a,b,c,d])
print('O aluno sorteado foi {}.'.format(s))
#Também pode ser feito da forma abaixo:
'''from random import choice
n1=input('Primeiro aluno: ')
n2=input('Segundo aluno: ')
n3=input('Terceiro aluno: ')
n4=input('Quarto aluno: ')
lista=[n1,n2,n3,n4]
escolhido=choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))'''
