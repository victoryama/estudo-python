#Guanabara Python3: 3 aula 17

#? Listas: em colchetes []
    #? semelhantes as tuplas, são variáveis compostas mas as listas permitem a alteração de valor, ou seja, são mutáveis
    #? manipulação de listas:
    #? para alterar nomelista[posição]='item'
    #? para adicionar nomelista.append('item')
        #? em um local nomelista.insert(posição,'item')
    #? para deletar: ambos deletam o especificado e refazem os índices
        #? del nomelista[posição] 
        #? normalmente para deletar o último elemento: para nomelista.pop(posição) elimina na posição  para nomelista.pop() elimina o último
        #? indicando o valor a ser removido: nomelista.remove('item')
            #? se tentar remover o item que não existe, tem-se um erro:
                #?if 'item' in nomelista:
                    #?nomelista.remove('item')
        #? Listas através de range:
            #?nomelista=list(range(4,11))
            #?print(nomelista)
        #? para ordenar as listas: nomelista.sort()
        #? para ordem inversa: nomelista.sort(reverse=True)
        #? para o tamanho: len(nomelista)

n = [2,5,9,1]
print(n[3])
n[2]=3
print(n[2])
n.append(7)
print(n)
n.sort()
print(n)
n.sort(reverse=True)
""" print(n)
print(n)
n[2]=3
n.append(7)
n.insert(2,2)
n.pop(2)
print(n)
print(n)
n[2]=3
n.append(7)
n.sort(reverse=True)
n.insert(2,2)
if 5 in n:
    n.remove(5)
print(n)
print(f'tamanho da lista é de {len(n)}') """

""" valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for n in valores:
    print(f'{n}...',end='')
for c, v in enumerate(valores): #posição c, indice v
    print(f'\nposição {c} tem o valor {v}') """

""" valores = list()
for c in range (0,5):
    valores.append(int(input('Valor:')))
for c, v in enumerate(valores):
    print(f'\nposição {c} tem o valor {v}')
print(valores) """

#! ao igualar uma lista na outra, é gerado uma relação entre elas
""" a = [2,3,4,7]
b=a
print(a, end='   ...   ')
print(b)
b[2]=8
print(a, end='   ...   ')
print(b)
#! para fazer uma cópia
c=a[:]
print(a, end='   ...   ')
print(c)
c[2]=0
print(a, end='   ...   ')
print(c) """

#! Desafio 78
    #? Programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valore digitado e as suas respectivas posições na lista
""" valores = list()
pmaior = list()
pmenor = list()
for c in range(0,5):
    valores.append(int(input('Valor: ')))
print(valores)
for posicao, valor in enumerate(valores):
    print(valor)
    if posicao==0:
        menor=maior=valores[posicao] #ou valor
    elif posicao>0:
        if valor>maior:
            maior=valor
        elif valor<=menor:
            menor=valor
for posicao, valor in enumerate(valores):
    if valor==maior:
        pmaior.append(posicao)
    elif valor==menor:
        pmenor.append(posicao)

print(f'Maior valor:{maior} posição: {pmaior}')
print(f'Menor valor:{menor} posição: {pmenor}') """

""" valores = list()
for c in range(0,5):
    valores.append(int(input('Valores: ')))
    if c==0:
        maior=menor=valores[c]
    elif c>0:
        if valores[c]>maior:
            maior=valores[c]
        elif valores[c]<menor:
            menor=valores[c]
print(f'Maior: {maior} e posição:', end=' ')
for posicao, indice in enumerate(valores):
    if indice==maior:
        print(f'{posicao}   ', end='')
print('\n') 
print(f'Menor: {menor} e posicão:', end=' ')     
for posicao, indice in enumerate(valores):
    if indice==menor:
        print(f'{posicao}   ', end='') """

""" print(valores)
print(pmaior)
print(pmenor) """

#! Desafio 79
    #? Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
""" lista = list()
while True:
    valor = int(input('Valor: '))
    if valor not in lista:
        lista.append(valor)
    elif valor in lista:
        print('Duplicado')
    while True:
        continuar = str(input('Continuar? ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break
lista.sort()
print(f'Foi digitado: {lista}') """

#! Desafio 80
    #?Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção, sem usar o sort(). No final mostre a lista ordenada na tela.
""" lista = list()
for c in range (0,5):
    if c==0:
        lista.append(int(input('Valor: ')))
        print('Adicionado no final da lista.')
    elif c>0:
        n = int(input('Valor: '))
        posicao = 0
        while posicao < len(lista):
            if n<=lista[posicao]:
                lista.insert(posicao,n)
                print(f'Adicionado em [{posicao}]')
                break
            elif n>lista[-1]:
                lista.insert(5,n)
                print('Adicionado no final da lista')
                break
            posicao += 1
print(lista)  """

""" lista=list()
for c in range (0,5):
    n=int(input('Valor: '))
    if c==0 or n>lista[-1] :
        lista.append(n)
        print('Adicionado no final: ')
    elif c>0:
        posicao=0
        while posicao<len(lista):
            if n<=lista[posicao]:
                lista.insert(posicao,n)
                print(f'Adicionado em [{posicao}]')
                break
            posicao+=1
print(lista) """

#! Desafio 81
    #? Programa que vai ler vários números e colocar em uma lista. Mostrar: a) quantos números foram digitados b) lista de valores, ordenado de forma descrescente c) se o valor 5 foi digitado e está ou não na lista
""" lista = list()
while True:
    lista.append(int(input('Valor: ')))
    while True:
        cnt = str(input('Continuar? [S/N] ')).upper().strip()[0]
        if cnt in 'SN':
            break
    if cnt in 'N':
        break
    if 5 in lista:
        parte = 'Faz Parte'
    elif 5 not in lista:
        parte = 'Não Faz Parte'
print(f'Foram digitados {len(lista)} elementos')
lista.sort(reverse=True)
print(lista)
print(f'O valor 5 {parte} da lista!')
 """
#! Desafio 82
    #? Programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores apres e os valores ímprares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas
""" lista=list()
while True:
    lista.append(int(input('Valores: ')))
    while True:
        cnt = str(input('Continuar? [S/N] ')).upper().strip()[0]
        if cnt in 'SN':
            break
    if cnt in 'N':
        break
listapar=list()
listaimpar=list() """

""" posicao=0
tamanho = len(lista)
while posicao!=tamanho:
    if lista[posicao]%2==0:
        listapar.append(lista[posicao])
    elif lista[posicao]%2>=1:
        listaimpar.append(lista[posicao])
    posicao+=1 """
    
""" for posicao, item in enumerate(lista):
    if item %2==0:
        listapar.append(item)
    elif item%2>=1:
        listaimpar.append(item)

print(lista)
print(listapar)
print(listaimpar) """

#! Desaio 83
    #? Programa onde o usuário digite uma expressão qualquer que use parênseses. Seu aplicativo deverá analisar se a expressão passada está com os parênses abertos e fechados na ordem correta

""" expressao = input('Expressão: ')
lista=list()
for item in expressao:
    if item == '(':
        lista.append('(')
    elif item == ')':
        if len(lista)>0:
            lista.pop()
        elif len(lista)==0:
            lista.append('0')
            break
if len(lista)==0:
    print('Expressão Válida')
elif len(lista)>0:
    print('Expressão Inválida') """
