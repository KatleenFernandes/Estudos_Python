#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para Fahrenheit.
c=float(input('Digite a temperatura em °C: '))
f=c*1.8+32
#Formúla da conversão: c/5 = (f-32)/9
print('A temperatura {}°C equivale a {}ºF.'.format(c,f))