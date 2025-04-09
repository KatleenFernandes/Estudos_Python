#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a=input('Digite o nome do primeiro aluno: ')
b=input('Digite o nome do segundo aluno: ')
c=input('Digite o nome do terceiro aluno: ')
d=input('Digite o nome do quarto aluno: ')
print('A ordem sorteada foi: {}'.format(random.sample([a,b,c,d],k=4)))
#Ao invés do sample, também é possível utilizar o shuffle.