#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta, pinta uma área de 2m**2
l=float(input('Digite a largura da sua parede em m: '))
a=float(input('Digite a altura da sua parede em m: '))
A=l*a
t=A/2
print('A área da sua parede é {}m², portanto é preciso de {}L de tinta para pintar a sua parede.'.format(A,t))
