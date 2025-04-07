#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
n=float(input('Digite o valor em reais que você tem: R$ '))
d=n/3.27
print('Com R$ {:.2f} reais você pode comprar US$ {:.2f} dólares.'.format(n,d))
