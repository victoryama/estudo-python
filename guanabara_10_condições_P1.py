#Guanabara Python3: 1 aula 10

#? Condições Simples: para 2 situações/simples
 
    #? if alguma coisa:
        #? comando
    #? else:
        #? outro comando

#* >= é diferente de >

#tempo = int(input('Idade do carro: '))
#if tempo > 4:
    #print('Velho')
#else:
    #print('Novo')
#print('É isso')

#? Simplificando
#print('Novo' if tempo<5 else 'Velho')

#? se a condição não for respeitada, não acontece nada
    #? quando se tem o Else é uma estrutura composta
    #? quando não se tem o Else é uma estrutura condicional simples
#nome = input('Qual seu nome? ')
#if nome == 'Victor':
    #print('Que nome lindo você tem!')
#print('Bom dia, {}' .format(nome))

#n1 = float(input('Primeira nota: '))
#n2 = float(input('Segunda nota: '))
#m = (n1 + n2)/2
#print('Média final: {:.2f}' .format(m))
#if m>=6:
#    print('Você está aprovado')
#else:
#    print('Você foi reprovado')

#! Desafio 28
    #? Escreca um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhdio pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
#import random
#pensamento = random.randrange(0,5,1)
#print(pensamento)
#n = int(input('Número de 1 a 5: '))
#if n == pensamento:
#    print('Venceu')
#else:
#    print('Perdeu')

#! Desafio 29
    #? Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais/Km acima do limite.
#v = float(input('velocidade em Km/h: '))
#if v > 80:
#    m = v - 80
#    c = m*7
#    print('Levou multa!\nNo valor de R${:.2f}' .format(c))
#else:
#    print('Não levou multa, sua velocidade foi de {:.2f}Km/h' .format(v))

#! Desafio 30
    #? Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
#n = int(input('Diga um número: '))
#resto = n % 2
#if resto == 0:
#    print('O Número {} é PAR'.format(n))
#else:
#    print('O Número {} é Impar'.format(n))

#! Desafio 31
    #? Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km e R$0,45 para viagens mais longas
#d = float(input('Distância em Km: '))
#if d <= 200:
#    p = d*0.5
#    print('Sua viagem foi abaixo de 200Km.',end=' ')
#else:
#    p = d*0.45
#    print('Sua viagem foi acima de 200km.',end=' ')
#    #print('O custo foi de R${:.2f}' .format(c))

#print('O custo foi de R${:.2f}' .format(p))
#print('O custo foi de',end=' ')
#p = d*0.5 if d <= 200 else d*0.45 
#print('R${:.2f}'.format(p))
#print('Novo' if tempo<5 else 'Velho')

#! Desafio 32
    #? Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#! Desafio 33
    #? Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#n1 = int(input('Primeiro: '))
#n2 = int(input('Segundo: '))
#n3 = int(input('Terceiro: '))
#maior = n3
#if n1>n2 and n1>n3:
#    maior = n1
#if n2>n1 and n2>n3:
#    maior = n2
#menor = n3
#if n1<n2 and n1<n3:
#    menor = n1
#if n2>n1 and n2>n3:
#    menor = n2
#print('Maior = {} e Menor = {}'.format(maior,menor))

#! Desafio 34
    #? Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250 calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%.
#s = float(input('Seu salário em reais: '))
#aumento = s*0.1 if s>1250 else s*0.15
#print('Seu aumento é de R${:.2f}' .format(aumento))

#! Desafio 35
    #? Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#l1 = float(input('L1: '))
#l2 = float(input('L2: '))
#l3 = float(input('L3: '))
#if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
#    print('Pode formar um triângulo')
#else:
#    print('Não pode formar um triângulo')