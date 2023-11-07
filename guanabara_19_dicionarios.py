#Guanabara Python3: 3 aula 19

#? Dicionários - variável composta, indices literais, personalizar os índices, fechados por {}

""" dados=['pedro',25]
print(dados[0])
print(dados[1]) """
#? permite personalizar os indices
""" dados=dict()
#? determina o nomes dos indices
dados={'nome':'Pedro','idade':25} 
print(dados['nome'])
print(dados['idade']) """
#? criar um novo elemento
""" dados['sexo']='M'
print(dados)
#? remover elemtnos
del dados['idade']
print(dados) """

filme = {'título':'Star Wars','ano':1977,'diretor':'George Lucas'}
print(filme)
#? para retornar os valores do dicionário
#print(filme.values())
#? para retornar os indices
print(filme.keys())
lista=list()
lista.append(filme.keys())
print(lista(1))
#? para retornar indices e valores
#print(filme.items())
#? utilizando for
#for indices, valores in filme.items():
    #print(f'O {indices} é {valores}')

""" brasil = []
estado1={'UF':'Rio de Janeiro', 'sigla':'RJ'}
estado2={'UF':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['UF']) """

#? para não relacionar a lista e o dicionário: fazer uma cópia 
    #* não se pode fazer fatiamento
""" estado=dict()
brasil=list()
for c in range(0,3):
    estado['UF']=str(input('UF: '))
    estado['Sigla']=str(input('Sigla: '))
    brasil.append(estado.copy()) #? fazendo cópia
for estado in brasil:
    for indices, valores in estado.items():
        print(f'O {indices} tem valor {valores}')

for estado in brasil:
    for valores in estado.values():
        print(valores, end=' ')
    print() """

#! Desafio 90
    #? Programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela
""" aluno = dict()
aluno['nome'] = input("Nome: ")
aluno['media'] = float(input("Média: "))
if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
elif aluno['media'] <= 7:
    aluno['situacao'] = "Reprovado"

for indice, item in aluno.items():
    print(f'{indice} é de {item}') """

#! Desafio 91
    #? Programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
""" from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1':randint(1,6),'jogador2':randint(1,6), 'jogador3':randint(1,6), 'jogador4':randint(1,6)}
rank = ()
print('Sorteados: ')
for jogador, n in jogo.items():
    print(f'{jogador} tirou {n}.')
    sleep(1)
#* itemgetter pega os itens no indice indicado 
rank = sorted(jogo.items(), key=itemgetter(0), reverse=True)
print(rank)
for lugar, jogador in enumerate(rank):
    print(f'{lugar+1}°lugar: {jogador[0]} com {jogador[1]}')
    sleep(1)
 """
#! Desafio 92
    #? Programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receverá também o ano de contratação e o salaário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

""" from datetime import datetime
dados = {}
dados['nome']=str(input('Nome: '))
nascimento=int(input('Ano de Nascimento: '))
dados['idade']=datetime.now().year - nascimento
dados['cpts']=int(input('Carteira de Trabalho (0 não tem): '))
if dados['cpts']!=0:
    dados['ano de contratação']=int(input('Ano de contratação: '))
    dados['salario']=int(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contratação']+35)-datetime.now().year)
print('-=-'*10)
print(dados)

for indices, valores in dados.items():
    print(f'O {indices} tem valor {valores}.')"""

#! Desafio 93
    #? Programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogado e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No fina, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durant o campeonato.
""" jogador=dict()
jogador['nome']=str(input('Nome do Jogador: '))
#para inserir dados de um dicionário deve ser usado "" não ''
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
jogos=list()
for c in range(0,partidas):
    jogos.append(int(input(f'Quantos gols na {c+1}° partida? ')))
jogador['gols']=jogos[:]
print('-=-'*15)
print(jogador)
print('-=-'*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*15)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas')
total=0
print(f'{jogador["gols"]}')
for k, v in enumerate(jogador['gols']):
    print(f'Na {k+1}° partida, fez {v} gols.')
    total+=v
print(f'Fez um total de {total} gols.') """

""" jogador=dict()
jogador['nome']=str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogos=list()
soma=0
for c in range(0,partidas):
    jogos.append(int(input(f'Quantos gols na {c+1}° partida? ')))
    soma+=jogos[c]
jogador['gols']=jogos[:]
jogador['total']=soma
print('-=-'*20)
print(jogador)
print('-=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-'*20)
for i, g in enumerate(jogador['gols']):
    print(f'Na {i+1}° partida, {jogador["nome"]} fez g gols.')
print(f'Foi um total de {soma} gols.') """

#! Desafio 94
    #? Programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a)quantas pessoas foram cadastradas, b) a média de idade do grupo, c) uma lsita com todas as mulheres, d) uma lista com tds as pessoas com idade acima da média
""" pessoa={}
dados=[]
it=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Erro! Digitar M ou F!')
    pessoa['idade']=float(input('Idade: '))
    dados.append(pessoa.copy())
    it+=pessoa['idade']
    while True:
        cnt=input('Continuar? [S/N] ').upper()[0]
        if cnt in 'SN':
            break
        else:
            print('Erro! Digitar M ou F!')
    if cnt.upper().strip()[0] in 'N':
            break
#print(dados)
print('-=-'*20)
print(f'O grupo tem {len(dados)} pessoas')
media=it/len(dados)
print(f'A média de idade é de {media} anos')
print(f'As mulheres cadastradas foram:',end=' ')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}',end=' ')
print()
print(f'Lista de pessoas que estão acima da média:')
for p in dados:
    if p["idade"]>=media:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<<ENCERRADO>>')
 """

 #! Desafio 95
    #? Aprimore desafio 93, funcione com vários jogadores, com sistema de visualização de detalhes do aproveitamento de cada jogador

""" jogador=dict()
jogos=list()
jogadores=list()
while True:
    jogador.clear()
    jogos.clear()
    jogador['nome']=str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    soma=0

    for c in range(0,partidas):
        jogos.append(int(input(f'Quantos gols na {c+1}° partida? ')))
        soma+=jogos[c]
    jogador['gols']=jogos[:]
    jogador['total']=soma
    print('-=-'*20)
    print('-=-'*20)
    jogadores.append(jogador.copy())
    cnt=str(input('Continuar? [S/N] ')).upper().strip()[0]
    if cnt in 'N':
        break
    else:
        print('---'*15)
print('-=-'*15)
print('COD    nome        gols      total')
print('---'*15)
for k, v in enumerate(jogadores):
    print(f'{k}          {v["nome"]}      {v["gols"]}       {v["total"]}')
print('---'*15)
while True:
    k = int(input('Mostrar dados de qual jogador? '))
    if k==999:
        break
    elif k>=len(jogadores):
        print(f'Erro! Não existe jogador com código {k}!')
    else: #k<=len(jogadores)-1
        print(f'Levantamento do jogador {jogadores[k]["nome"]}:')
        for i, n in enumerate(jogadores[k]["gols"]):
            print(f'No {i+1}° jogo fez {n} gols')
print('>>>ENCERROU...')
#print(jogadores) """
