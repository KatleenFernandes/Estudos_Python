#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1=float(input('Digite um valor: '))
c=n1*100
m=n1*(10**3)
print('{:.3f}m em cm vale {:.3f}cm e em mm vale {:.3f}mm'.format(n1,c,m))
#Agora faça para todas as medidas: km,hm,dam e dm.
print('A escala completa de {}m é: '.format(n1))
print('Em Km: {}km;\nEm Hm: {};\nEm dam: {};\nEm m: {};\nEm dm: {};\nEm cm: {};\nEm mm: {}.'.format(n1/(10**3), n1/(10**2),n1/10,n1,n1*10,c,m))
