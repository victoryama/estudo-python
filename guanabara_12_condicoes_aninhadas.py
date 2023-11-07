#Guanabara Python3: 2 aula 12

#? Condições Aninhadas: estruturas condicionais dentro de estruturas condicionais. Pode ser usado quantos elif quiser, else pode não ter mas se tiver apenas 1 else, não se pode usar elif sem if 
    #? if condição:
        #? bloco
    #? elif condição 2:
        #? bloco
    #? else:
        #? bloco

#n = input('Nome: ')
#if n == 'Victor' or n == 'Nathalia':
#    print('Belo nome')
#elif n == 'João' or n == 'Maria' or n == 'Ana':
#    print('Nome popular')
#elif n in 'Claudia Jessica Juliana':
#    print('Belo nome feminino')
#else:
#    print('Diferente')

#! Desafio 36
    #? Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, ela não deverá passar 30% do slário se não será negado.
#valor = float(input('Valor da casa: R$'))
#salario = float(input('Salário: R$'))
#anos = float(input('Em quantos anos: '))
#p = valor/(anos*12)
#if p > (0.3*salario):
#    print('Negado')
#else:
#    print('Aprovado')

#! Desafio 37
    #? Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 = binário, 2 = octanal e 3 = hexadecimal

#! Desafio 38
    #? Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primiero valor é maior, o segundo valor é o maior, não existe valor maior, os dois são iguais
#n1 = int(input('Primeiro: '))
#n2 = int(input('Segundo: '))
#if n1>n2: 
#    print('O primeiro valor é o maior')
#elif n2>n1:
#    print('O segundo o valor é o maior')
#else:
#    print('Os dois são iguais')

#! Desafio 39
    #? Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: se ainda vai se alistar, se é hora de se alistar ou se já pasosu do tempo. Deverá mostrar o tempo q falta ou passou
#ano = int(input('Ano de nascimento: '))
#if 2022-ano==18:
#    print('Está na hora de se alistar')
#elif 2022-ano>18:
#    print('Já passou seu tempo')
#    d = (2022-ano)-18
#    if d==1:
#        print('Passou apenas 1 ano')
#    else:
#        print('Passaram {}anos'.format(d))
#elif 2022-ano<18:
#    print('Você ainda vai se alistar')
#    d = 18 - (2022-ano)
#    if d==1:
#        print('Falta apenas 1 ano')
#    else:
#        print('Faltam {}anos'.format(d))

#! Desafio 40
    #? Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média: abaixo de 5 = reprovado, entre 5 e 6.9 = recuperação, igual ou superior a 7 = aprovado
#n1 = float(input('Primeira nota: '))
#n2 = float(input('Segunda nota: '))
#media = (n1+n2)/2
#if media < 5:
#    print('REPROVADO')
#elif media >= 5 and media <= 6.9:
#?osb poderia ter deixado apenas media >=5
#    print('RECUPERAÇÃO')
#elif media >= 7:
#    print('APROVADO')

#! Desafio 41
    #? A condeferação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria: até 9 = mirim, até 14 = infantil, até 19 = junior, até 20 = senior, acima é master
#ano = int(input('Ano de nascimento: '))
#idade = 2022 - ano
#if idade <= 9:
#    print('MIRIM')
#elif idade >9 and idade <= 14:
#    print('INFANTIL')
#elif idade > 14 and idade <= 19:
#    print('JUNIOR')
#elif idade == 20:
#    print('SENIOR')
#else:
#    print('MASTER')

#! Desafio 42
    #? refaça o 35 mostrando o tipo de triângulo: equilátero, isósceles e escaleno

#! Desafio 43
    #? peso e altura, calcula o IMC e mostre o status; abaixo = abaixo de 18.5, ideal entre 18,5 a 25, sobrepeso 25 até 30, obesidade 30 até 40, obesidade mórbida acima de 40
#peso = float(input('Peso em Kg: '))
#altura = float(input('Altura em m: '))
#imc = peso / (altura**2)
#print(imc)
#if imc < 18.5:
#    print('abaixo do peso')
#elif imc >= 18.5 and imc < 25:
#    print('peso ideal')
#elif imc >= 25 and imc < 30:
#    print('sobrepeso')
#elif imc >= 30 and imc < 40:
#    print('obesidade')
#elif imc >= 40:
#    print('obesidade morbida')

#! Desafio 44
    #? Elabora um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e a condição de pagamento. a vista -10%, cartão a vista -5%, cartão em 2x normal e 3x ou mais no cartão 20% juros
#preco = float(input('VALOR R$'))
#pagamento = input('Condição: ')
#if pagamento == 'a vista':
#    valor = 0.9*preco
#elif pagamento == 'cartão a vista':
#    valor = 0.95*preco
#elif pagamento == 'cartao em 2x':
#   valor = preco
#else:
#    valor = 1.2*preco
#print('O valor normal é de {:.2f} e o valor conforme a forma de pagamento {} é de R${:.2f}'.format(preco,pagamento,valor))

#! Desafio 45
    #? Jokenpô com o computador
from random import randint
jogadas = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
print('Jogadas: 0=pedra, 1=papel e 2=tesoura')
escolha = int(input('Jogada: '))
print('='*20)
print('Computador: {}'.format(jogadas[pc]))
print('Jogador: {}'.format(jogadas[escolha]))
if pc == 0:
    if escolha == 0:
        print('Empate')
    elif escolha == 1:
        print('Jogador ganhou')
    elif escolha == 2:
        print('Jogador perdeu')
elif pc == 1:
    if escolha == 0:
        print('Jogador perdeu')
    elif escolha == 1:
        print('Empate')
    elif escolha == 2:
        print('Jogador ganhou')
elif pc == 2:
    if escolha == 0:
        print('Jogador ganhou')
    elif escolha == 1:
        print('Jogador perdeu')
    elif escolha == 2:
        print('Empate')