#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
d=int(input('Quantos dias alugados? '))
k=float(input('Quantos Km rodados? '))
t=60*d+0.15*k
print('O total a pagar é de R$ {:.2f} reais.'.format(t))
