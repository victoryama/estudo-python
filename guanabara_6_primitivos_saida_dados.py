#converter um número para float e 
#n = float(input('Digite um valor:'))
#m = str(input('Digite um valor:'))
#print(n)
#print(type(n))
#print(m)
#rint(type(m))

#booleano, verdadeiro ou falso
    #vai entender se tiver um valor dentro como verdadeiro
#n = bool(input('Digite um valor:'))
#print(n)

#verifica se a entrada pode ser convertido em um tipo de entrada
#n = input('digite um valor:')
#se é possível para número
#print(n.isnumeric()) 
#se é possível para alfabético
#print(n.isalpha())
#se é possível para alfanumerico
#print(n.isalnum())

#Desafio 3
    #Crie um programa que leia dois números e mostre a soma entre eles
#a = int(input('A = '))
#b = int(input('B = '))
#soma = a + b
#print('A soma é', a + b)
#print('A + B = {}' .format(a + b))
#print('A + B = {}' .format(soma))
#print('{} + {} = {}' .format(a, b, soma))

#DESAFIO 4
    #Faça um programa que leia algo pelo teclado e mostre na tela o seu teipo primitivo e todas as informações pos´siveis sobre ele

primitivo = input('Digite algo e darei o tipo dele: ')
#OBS input retorna sempre como str se não for feito a conversão
print(primitivo)
print(type(primitivo))
print('É um número? ', primitivo.isnumeric())
print('É uma letra? ', primitivo.isalpha())
print('É um alfanumérico? ', primitivo.isalnum())
