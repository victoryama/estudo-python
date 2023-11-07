#Guanabara Python3: 3 aula 18

#? Listas 2 - continuação de variáveis compostas
    #? adicionar uma lista em outra lista

""" teste=list()
teste.append('gustavo')
teste.append(40)
galera=list()
galera.append(teste[:]) #? add lista teste em galera
#? para não gerar uma ligação entre listas utilizar [:] para copiar
teste[0]='maria'
teste[1]=22
galera.append(teste[:])
print(galera) """

""" galera=[['João',19],['ana',33],['joaquim',13],['maria',45]]
print(galera)
print(galera[0]) #? selecionou a lista em [0]
print(galera[0][0]) #? selecionou a lista em [0] e o item em [0]
print(galera[1][0])
for p in galera:
    print(p)
    print(p[0])
    print(f'{p[0]} tem {p[1]} anos') """

""" galera=list()
dado=list()
for c in range(0,3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
maior=menor=0
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade')
        maior+=1
    else:
        print(f'{p[0]} é menor de idade')
        menor+=1
print(galera)
print(f'tem {maior} pessoas com mais de 21 anos')
print(f'tem {menor} pessoas com menos de 21 anos') """

#! Desafio 84
    #? Programa que leia nome e peso de várias pessoas, guardadno tudo em uma lista. No final, mostre: a) quantas pessoas foram cadastradas b) uma listagem com as pessoas mais pesadas c) listagem com as pessoas mais leves
""" pessoa = list()
infos = list()
maior=menor=0

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(int(input('Peso: ')))
    if len(infos)==0:
        maior=menor=pessoa[1]
    elif len(infos)>0:
        if pessoa[1]>maior:
            maior=pessoa[1]
        elif pessoa[1]<menor:
            menor=pessoa[1]
    cnt=input('Continuar? [S/N]')
    infos.append(pessoa[:])
    pessoa.clear()
    if cnt.upper().strip()[0] in 'N':
        break
#print(pessoa)
#print(infos)
print(f'cadastrado {len(infos)} pessoas.')
pesado = list()
leve = list()
print(f'Peso maior foi de {maior}Kg. Peso de',end=' ')
for p in infos:
    if p[1]==maior:
        print(f'{p[0]}',end=' ')
print(f'\nPeso menor foi de {menor}Kg. Peso de',end=' ')
for p in infos:
    if p[1]==menor:
        print(f'{p[0]}',end=' ')
 """
#! Desafio 85
    #? Programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores apres e ímpares em ordem crescente.

""" numero=list()
par=list()
impar=list()
numero.append(par)
numero.append(impar)

for c in range (0,7):
    n=int(input(f'O {c+1}° Valor: '))
    if n%2==0:
        par.append(n)
    elif n%2>0:
        impar.append(n)
par.sort()
impar.sort()
print(f'Valores pares: {par}')
print(f'Valores impares: {impar}') """

#! Desafio 86
    #? Programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz com a formatação correta
""" l1=list()
l2=list()
l3=list()
matriz=list()
matriz.append(l1)
matriz.append(l2)
matriz.append(l3)
for linha in range(0,3):
    for coluna in range(0,3):
        if linha==0:
            l1.insert(coluna,input(f'Digite um valor em [{linha}, {coluna}]: '))
        elif linha==1:
            l2.insert(coluna,input(f'Digite um valor em [{linha},  {coluna}]: '))
        elif linha==2:
            l3.insert(coluna, input(f'Digite um valor em [{linha} , {coluna}]: '))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print('\n') """

""" matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna]=int(input(f'Digite um valor para[{linha}][{coluna}]: '))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]} ]', end=' ')
    print() """

#! Desafio 87
    #? Aprimore o desafio anterior, mostrando no final: a soma de todos os valores pare, soma dos valores da terceira coluna, o maior valor da segunda linha.

""" m=[[0,0,0],[0,0,0],[0,0,0]]
somapares=somacoluna=0
for linha in range(0,3):
    for coluna in range(0,3):
        m[linha][coluna]=int(input(f'Valor para [{linha}][{coluna}]: '))
        if m[linha][coluna]%2==0:
            somapares+=m[linha][coluna]
        if coluna==2:
            somacoluna+=m[linha][coluna]
        if linha==1:
            if coluna==0:
                maior=m[linha][coluna]
            elif coluna>0:
                if m[linha][coluna]>maior:
                    maior=m[linha][coluna]

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[  {m[linha][coluna]}  ]', end='')
    print()
print(f'Soma dos pares: {somapares}')
print(f'Soma da terceira coluna: {somacoluna}')
print(f'Mario valor da segunda linha {maior}') """

#! Desafio 88
    #? Programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta.
""" from random import randint
#print(randint(1,11))
lista=list()
jogo=list()
n=int(input('Quantos jogos? '))
for jogos in range(0,n):
    tentativa=0
    while True:
        sorteio = randint(1,60)
        if sorteio not in jogo:
            jogo.append(sorteio)
            tentativa += 1
        if tentativa >= 6:
            break
    lista.append(jogo[:]) #copia sem ligação
    jogo.clear()
print(f' Sorteando {n} jogos')
for jogo in range(0,n):
    print(f'Jogo {jogo+1}: {lista[jogo]}')
print('Boa sorte') """

#! Desafio 89
    #? Program que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média e cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente
#*posições
""" p=0 #posicao aluno em dados
dados=list()
alunos=list()
while True:
    alunos.insert(0,input('Nome: '))
    alunos.insert(1,float(input('Nota 1: ')))
    alunos.insert(2,float(input('Nota 2: ')))
    dados.append(alunos[:])
    continuar=str(input('Continuar? ')).upper().strip()
    alunos.clear()
    if continuar in 'N':
        break
print('No.   Nome       Média')
print('-=-'*10)
for posicao, aluno in enumerate(dados):
    print(f'{posicao:<4}   {aluno[0]:<10}       {((aluno[1]+aluno[2])/2):>8.1f}')

while True:
    al=int(input('Mostrar notas de qual aluno? '))
    if al>(len(dados)-1):
        print('FIM')
        break
    elif al<=(len(dados)-1):
        print(f'Notas de {dados[al][0]} são [[{dados[al][1]}][{dados[al][2]}]]')
 """