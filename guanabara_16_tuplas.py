#Guanabara Python3: 3 aula 1

#? Tuplas: É uma das Variáveis compostas: PODEM TER MAIS DE UMA ATRIBUIÇÃO POR VARIÁVEL
    #? toda variável simples: é um espaço na memória, UMA ÚNICA ATRIBUIÇÃO POR VARIÁVEL 
        #? não dá para colocar 2 atribuições em uma mesma variável simples
    
    #? acessar elementos de uma tupla através de índices 0,1,...
    #* TUPLAS SÃO IMUTÁVEIS, uma vez definidas não podem ser mudadas
    #? tuplas podem estar ou não entre parenteses ()
    
""" lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
lanchinho = 'hamburguer', 'suco', 'pizza', 'pudim' #tupla não precisa estar entre parenteses
print(lanche)
print(lanche[3]) 
print(lanche[-2]) #começa em -1 de trás apra frente
print(lanchinho)
print(lanchinho[1])
#? no fatiamento o último elemento é ignorado
print(lanche[1:3])
print(lanche[1:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-4:])
print(lanche)
print(len(lanche))
for c in range(0, len(lanche)):
    print(lanche[c])
for comida in lanche:
    print(f'vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'vou comer {comida} na posição {pos}')
print(sorted(lanche)) #coloca em ordem em coloca em ´[] tranforma em lista
print(lanche)  """

#? ao juntar Tuplas, a ordem da junção/soma tem diferença
""" a = (2,5,4)
b = (5,8,1,2)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5)) #contar quantas vezes aparece o número 5
print(c.index(2)) #em que posição está o 2, na primeira ocorrência
print(d.index(2,4)) #a partir da posição 4, deslocamento
print(d.index(5,1)) """

#? tuplas podem ter dados de tipos diferentes
""" pessoa = ('gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa) # apaga da melhora
print(pessoa) """
#? Tuplas são imutáveis, mas podem ser deletáveis

#! Desafio 72
    #? programa tenha tupla com contagem por extenso de 0 até 20. Ler um número de entrada de 0 a 20 e mostrar por extenso
""" n = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    entrada = int(input('Número: '))
    if 0<=entrada<=20:
        break
print(f'O número é {n[entrada]}') """

#! Desafio 73
    #? tupla preenchida com os 20 primeiros colocados da tabela do campeotnato brasileiro de Fut, na ordem de colocação, depois mostrar: a) 5 primeiros b) últimos 4, c) uma lista com ordem alfabética e d) posição da tabela do time de chapeco
""" times = 'corinthians', 'palmeiras', 'santos', 'gremio', 'cruzeiro', 'flamengo', 'vasco', 'chapeco', 'atletico', 'botafogo', 'atletico-PR', 'bahia', 'são paulo', 'fluminense', 'sport recife', 'ec vitoria', 'coritiba', 'avaí', 'ponte preta', 'atletico-GO'

print(f'5 primeiros: {times[:5]}')
print(f'4 últimos: {times[16:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'Posição do chapeco {times.index("chapeco")+1}')  """

#! Desafio 74
    #? Programa que gera cinco números aleatórios e coloca em uma tupla. Mostr a listagem de número gerados e também indique o menor e o maior valor q estão na tupla
""" from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for c in numeros:
    print(f'{c}', end=' ')
print(f'Maior: {max(numeros)}') """

#! Desafio 75
    #? Leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre: a)quantas vezes aparecem o valor 9, b) posição do primeiro 3, c)quais números foram pares

""" n = (int(input('Número: ')), int(input('Número: ')), int(input('Número: ')), int(input('Número: ')))
print(n.index(3)) 
if 9 in n:
    print(f'O valor 9 aparece {n.count(9)} vezes')
else:
    print('Não há números 9')
if 3 in n:
    print(f'Posiçao do primeiro 3 é {n.index(3)+1}')
else:
    print('Não há números 3')
print('Números pares: ',end='')
for c in range (0,4):
    if n[c]%2==0:
        print(f'{n[c]}', end=' ') """

#! Desafio 76
    #? Programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. Mostra uma listagem de preços organizando os dados de forma tabular
""" itens = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'tranferidor', 4.20)
print('Lista de preços:')
print('-=-'*20)
for c in range (0,10):
    if c%2==0:
        print(f'{itens[c]}-----------',end='')
    elif c%2!=0:
        print(f'R$ {itens[c]}')
print('-=-'*20)

# com 30 caracteres :30
# alinhado a esquerda com pontos :.<30
# alinhado a direita com espaços :>7.2f

for c in range (0,10):
    if c%2==0:
        print(f'{itens[c]:.<30}', end='')
    elif c%2!=0:
        print(f'R${itens[c]:>7.2f}') """

#! Desafio 77
    #? programa que tenha uma tupla com várias palavras, não usar acento. Depois mostrar, para cada palavra quais são as suas vogais
""" tupla = 'aprender', 'procrastinar', 'linguagens', 'python', 'curso', 'gratis', 'estudar', 'praticas', 'trabalhar', 'mercado', 'programador', 'futuro'

for palavra in tupla:
    print(f'\nPalavra: {palavra.upper()} tem-se as seguintes vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ') """

""" for c in palavras:
    print(f'\nPalavras {c.upper()} tem-se as seguintes vogais: ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ') """

#! Revisão 

""" n = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
for numero in n:
    print(numero) """

""" p = 'Nathalia', 'Victor', 'Giovana', 'Leticia', 'Miyahira', 'Claudia', 'Thor'
for nome in p:
    print(f'{nome}')
    for letra in nome:
        print(letra, end=' ')
    print('Vogais: ',end='')
    for letra in nome:   
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n')
     """