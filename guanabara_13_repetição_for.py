#Guanabara Python3: 2 aula 13

#? for: laço de repetição ou interação
    #?  precisa de um limite
    #?  contador 
    #? laço com variável de controle
    #? estrutura de repetição com variável de controle 

#? for variavel range(0,3):
    #?if moeda:
        #?pega
    #?passo
    #?pula
#?comando 

for c in range(0,6):
    print(c)
    print('sou um merda')
print('culpa minha como sempre')

#* o última é ignorado
#for c in range(0,6):
#    print(c)
#print('terminou')
#* para uma contagem regressiva
#* terceira casa no range determina a forma da contagem
#for c in range(6,0,-1):
#    print(c)
#print('terminou') 

#n = int(input('Número: '))
#for c in range(0,n+1):
#    print(c)
#print('terminou')

#i = int(input('Início: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range(i,f+1,p):
#    print(c)
#print('terminou')

#s = 0
#for c in range(0,4):
#    n = int(input('Valor: '))
#    s = s + n # ou s += n
#print('fim')
#print(s)

#! Desafio 46
    #? mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo até 10 até 0, com uma pausa de 1 s entre eles
#from time import sleep
#s = 10
#print('10s para os fogos')
#? contagem
#for c in range (s, -1, -1):
#    sleep(1)
#    print(c)
#    if c == 0:
#        print('bru boom pah')

#! Desafio 47
    #? mostre na teal todos os números pares que estão no intervalo entre 1 a 50
""" for c in range (50, -1, -2):
    print(c, end=' ')
print('Terminou')

for c in range (2, 51, 2):
    print(c, end=' ')
print('terminou')
 """

#! Desafio 48
    #? calcule a soma entre todos os número impares que são múltiplos de três e que se encopntram no internvalo de 1 até 500
#s = 0
#for c in range (1, 501, 2):
#    if c%3==0:
#        s=s+c
#print(s)

#! Desafio 49
    #? desafio 9, mostrando a tabuada de um número número com o laço for

#! Desafio 50
    #? leia 6 números inteiros e mestre a soma apenas daqueles que forem pares. Se o valor for impar, desconsidereo 
#s = 0
#for c in range (1, 7):
#    n = int(input('Digite um número: '))
#    if n%2==0:
#        s = s + n
#print(s)

#! Desafio 51
    #? Leia o primeiro termo e a razão de um PA, no final mostre os 10 termos dessa PA
#primeiro = int(input('Primeiro termo: '))
#razao = int(input('Razão: '))
#n = primeiro
#for c in range (1,11,1):
#    n = n + razao
#    print(n) 
#print('terminou')

#! Desafio 52
    #? Leia um número inteira e diga se é ou não um número primo
""" n = int(input('Digite um inteiro: '))
t = 0
for c in range (1, n+1):
    if n%c==0:
        t = t + 1
if t == 2:
    print('Número PRIMO')
else:
    print('Número NÃO PRIMO') """

#! Desafio 53
    #? Leia frases qualquer e diga se ela é um palindromo, desconsiderando os espaços

#! Desafio 54
    #? leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
""" menor = 0
maior = 0
for c in range (1, 8):
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        maior += 1
    elif idade <18:
        menor += 1
print('{} pessoas já atingiram a maioridade e {} pessoas ainda não atingiram.' .format(maior,menor)) """
""" from datetime import date
hoje = date.today().year
maior = 0
menor = 1
for c in range (1, 8):
    data = int(input('Ano de nascimento: '))
    idade = hoje - data
    if idade>=18:
        maior += 1
    elif idade<18:
        menor += 1
print('{} pessoas já atingiram a maioridade e {} pessoas ainda não atingiram.' .format(maior,menor))   """     

#! Desafio 55
    #? Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
""" for c in range (1, 6):
    pesinho = float(input('Peso em Kg: '))
    if c==1:
        maior = pesinho
        menor = pesinho
    elif c >1:
        if pesinho >= maior:
            maior = pesinho
        elif pesinho <= menor:
            menor = pesinho
print('O maior foi {}Kg e o menor {}Kg'.format(maior,menor)) """

