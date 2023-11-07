#Guanabara Python3: 1 aula 8

#! Bibliotecas/Módulos
#? Fazer importações de bibliotecas para importar comandos/funcionalidades
    #? Generalista: import nome do módulo/biblioteca para importar tudo o que tem na biblioteca
#?  ESPECÍFICO: from módulo/biblioteca import oq se quer para importar apenas o que se quer ou uma parte, economiza memória

#?Exemplo de biblioteca:
    #? biblioteca matemática: math
           #? necessita definir math.sqrt()
        #? ceil = arredondamento para cima
        #? floor = arredondamenteo para baixo
        #? trunc = truncamento, dos número depois da vírgula
        #? pow = potência
        #? sqrt = raiz quadrada
        #? factorial = calcular fatorial
    #? import math importa tds as funções
    #? from math import srqt para apenas essa funções
           #? necessita definir sqrt()
#? from math import srqt, ceil para mais funções

#import math
#num = int(input('numero:'))
#raiz = math.sqrt(num)
#print(raiz)
#print('{}'.format(raiz))
#print('raiz de {} é {}'.format(num, math.floor(raiz)))
#from math import sqrt, floor
#num = int(input('numero: '))
#print('raiz de {} é {}'.format(num, floor(raiz)))

#* para ver bibliotecas acessar python.org em library reference
#* digitar import espaço e depois ctrl+espace aparece lista de biblioteca
#* Pypi package index, lista de bibliotecas da comunidade

#import random
#num = random.random() #? dar um número aleatório
#num = random.randint(1, 10) #? dar um número aleatório no intervalo
#print(num)

import emoji

print(emoji.emojize("olá :sunglasses:"))

#! Desafio 16
    #? Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção interna.
#from math import floor
#n = float(input('Digita um número real: '))
#print('A porção inteira de {} é {}'.format(n, floor(n)))

#! Desafio 17
    #? Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipontenusa
#from cmath import sqrt
#import math
#print('Informe os catetos de um triângulo retânculo')
#co = float(input('Cateto Oposto [Cm]: '))
#ca = float(input('Cateto Adjacente [Cm]: '))
#hp = math.sqrt( math.pow(co, 2) + math.pow(ca,2))
#print('A hipotenusa do triângulo retângulo de cateto oposto {}Cm e cateto adjacente {}Cm \né de {:.2f}Cm'.format(co, ca, hp))

#! Desafio 18
    #? Faça um programa que leia um ângulo qualuqer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#import math
#a = float(input('Digite um ângulo '))
#* os comandos são em radianos, deve se converter usando o comando abaixo
#rad = math.radians(a)
#print('Para o ângulo {}°,\n tem-se o valor seno de {:.2f},\n cosseno de {:.2f} \ne tangente de {:.2f}'.format(a, math.sin(rad), math.cos(rad), math.tan(rad)))

#! Desafio 19
    #? Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
#import random
#N1 = input('Aluno 1: ')
#N2 = input('Aluno 2: ')
#N3 = input('Aluno 3: ')
#N4 = input('Aluno 4: ')
#alunos = [N1, N2, N3, N4]
#escolhido = random.choices(alunos)
#print('O aluno que deverá apagar a lousa é o {}.'.format(random.choice(alunos)))

#! Desafio 20
    #? O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos aluno. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
#import random

#a = input('Aluno 1: ')
#b = input('Aluno 2: ')
#c = input('Aluno 3: ')
#d = input('Aluno 4: ')
#lista = [a, b, c, d]
#random.shuffle(lista)
#print(lista)

#! Desafio 21
    #? Faça um programa em python que abra e reproduza o áudio de um arquivo MP3