#Guanabara Python3: 3 aula 20

#* Funções: funções vinculados a rotina, coisas feitas constantemente
""" #? def nomefuncao():
#?      comando
#? 
#? precisa de duas linhas vazias
#?para chamar a função: nomefuncao() 
"""

#* Comando personalizado que adapte as necessides utilizando Parâmetros
#?def titulo(mensagem): nome genérico para parâmetro dentro do () da função
    #?comando com parâmetro "mensagem" sendo utilizado
#?titualo(parametro) utilizar parametro dentro do ()

#* Empacotamento: parâmetros serão "jogados" dentro, não se sabe a quantidade q será enviado/jogado
#? def contador(*num): #deve se utilizar o *

#? exemplos
""" def soma(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(4, 5)
soma(a=4, b=5)
soma(b=4, a=5) #? mudar a ordem, desde que seja especificado
soma(8, 9)
soma(2, 1) """

""" def contador(*num):
    for valor in num:
        print(f'{valor}',end=' ')
    print('fim') """


""" def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} número')


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2) """

""" def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1
    print(lst)


valores=[7,2,5,0,4]
dobra(valores) """

#? Desempacotamento
""" def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'somando os valores {valores} temos {s}')


soma(5,2)
soma(2,9,4) """

#! Desafio 96
    #? Programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno
#* primeiro definir a função

""" def area(l,c):
    print(f'A área de um terreno de {l}x{c} é de {l*c}')


#* definir as entradas
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c) """

#! Desafio 97
    #? Programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

#* definir a função
""" def escreva(msg):
    size=len(msg)
    print('~'*(size + 4))
    print(f'  {msg}')
    print('~'*(size + 4))


#* entradas
while True:
    msg = str(input())
    escreva(msg)
    cnt = input('Continuar ? [S/N] ')
    if cnt.upper().strip()[0] in 'N':
        break  """

#! Desafio 98
    #? Programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim, e passo e realiza a contagem. Três contagens: a) 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2 c) contagem personalizada
#* definir função
""" from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p==0:
        p = 1
    valor = i
    print('-=-'*15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print(valor, end=' ')
    sleep(0.5)
    #looping de contagem
    while True:
        if i<f:
            valor += p
            if valor > f:
                print('FIM!')
                break
            else:
                print(valor, end=' ')
                sleep(1)
        elif i>f:
            valor -= p
            if valor < f:
                print('FIM!')
                break
            else:
                print(valor, end=' ')
                sleep(0.5)

contador(1, 10, 1)
contador(10, 0, 2)
print('-=-'*15)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo) """

#! Desafio 99
    #? Programa que tenha uma função chamada maior(), que receva vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior
""" from time import sleep
def maior(*num): #* vai receber vários parâmetros, desempacotar
    cnt = maior = 0
    print('-=-'*15)
    print('Analisando...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        cnt+=1
        if cnt == 0:
            maior = valor
        elif cnt > 0:
            if valor>maior:
                maior = valor

    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')



# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior() """

#! Desafio 100
    #? programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somapar(). A primeira função vai sortear 5 números e vai colocálos dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior
""" from random import randint
list=[]
#funcao sorteio
def sorteio():
    cnt=0
    #list=[]
    print(f'Sorteando 5 valores da lista:', end=' ')
    while True: #contage
        n=randint(1,10)
        list.append(n)
        print(n, end=' ')
        cnt+=1
        if cnt==5:
            print('PRONTO!')
            break


#funcao somapar
def somapar():
    soma=0
    for n in list:
        if n%2==0:
            soma+=n
    print(f'Somando os valores pares de {list} temso {soma}')


sorteio()
somapar() """

""" from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for cnt in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True) #para mostrar a contagem
        sleep(0.3)
    print('PRONTO!')

def somapar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


num = list()
sorteio(num)
somapar(num) """