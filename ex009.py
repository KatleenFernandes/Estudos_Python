#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.
n=int(input('Digite um número: '))
n1=n*1
n2=n*2
n3=n*3
n4=n*4
n5=n*5
n6=n*6
n7=n*7
n8=n*8
n9=n*9
n10=n*10
print('A tabuada do número {} é: \n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}'.format(n,n,n1,n,n2,n,n3,n,n4,n,n5,n,n6,n,n7,n,n8,n,n9,n,n10))
#Resolução mais bonita:
print('-'*12)
print('{} x {:2} = {}'.format(n,1,n*1))
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print('{} x {:2} = {}'.format(n,4,n*4))
print('{} x {:2} = {}'.format(n,5,n*5))
print('{} x {:2} = {}'.format(n,6,n*6))
print('{} x {:2} = {}'.format(n,7,n*7))
print('{} x {:2} = {}'.format(n,8,n*8))
print('{} x {:2} = {}'.format(n,9,n*9))
print('{} x {:2} = {}'.format(n,10,n*10))
print('-'*12)