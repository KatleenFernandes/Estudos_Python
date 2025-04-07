#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s=float(input('Digite o valor do seu sálario: R$ '))
a=s+(s*(15/100))
print('Seu sálario de R${:.2f} reais com 15% de aumento passa a ser R${:.2f} reais.'.format(s,a))
