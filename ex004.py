#Exercicio 04: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n=input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços? ',n.isspace())
print('É um número? ',n.isnumeric())
print('É alfabético? ',n.isalpha())
print('É alfanúmerico? ',n.isalnum())
print('Está em maiúsculas? ',n.isupper())
print('Está em minúsculas? ',n.islower())
print('Está capitalizada? ',n.istitle())
#Exercicio 04-Bônus: Faça a mesma coisa do exercício anterior utilizando o .format.
a=input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaços em {}? {}'.format(a,a.isspace()))
print('{} é um número? {}'.format(a,a.isnumeric()))
print('{} é alfanúmerico? {}'.format(a,a.isalnum()))
print('{} está somente em letras maiúsculas? {}'.format(a,a.isupper()))
print('{} está somente em letras minúsculas? {}'.format(a,a.islower()))
print('{} está capitalizada? {}'.format(a,a.istitle()))
