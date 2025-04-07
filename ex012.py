#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p=float(input('Digite o preço do produto: R$ '))
d=p-(p*(5/100))
print('O produto que custa R${:.2f} reais, fica por R${:.2f} reais quando recebe um desconto de 5%.'.format(p,d))
