#Guanabara Python3: 2 aula 15

#? Laços de repetição: interrompendo a repetição While
    #? comando stop/iterrompa desvia da repetição
        #? while true:
            #? if algo:
                #? comando
            #? if algo:
                #? break
#? while true: faz repetir o laço para sempre
    #? break quebra o ciclo

""" c=1
while True:
    print(c,'->', end='')
    c += 1
    if c > 100:
        break
print('Terminou') """

""" n = c = s = 0
while True:
    n = int(input('Número: '))
    if n == 999:
        break
    s+=n
    c+=1
print(c)
print(f'soma = {s}')
print('soma = {}'.format(s)) """

#? nova formatação
""" nome = 'jose'
idade = 33
salario = 1000
print(f'O {nome} tem {idade} anos e ganhar {salario}reais') """

#! Desafio 66
    #? leia vários números inteiros. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos númeors foram difitados e qual foi a soma entre eles. Desconsiderando o flag

""" n = quant = 0
while True:
    numero = int(input('Número: '))
    print('Parada = 999')
    if numero != 999:
        n += numero
        quant += 1
    elif numero == 999:
        break
print(f'Soma dos {quant} números é de {n}!') """

#! Desafio 67
    #? mostre a tabuada de vários números, um de cafa vez, para cada valor figitado pelo usuário. O programa será interrompido quando o número solicitado foi negativo

""" while True:
    n = int(input('Qual tabuada?'))
    if n>0:
        for c in range(1,11):
            print(f'{n} X {c} = {n*c}')
    elif n<0:
        break
print('Encerrado') """

#! Desafio 68
    #? Par ou ímpar com o PC, só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas 
""" from random import randint
print('PAR ou IMPAR')
print('=-= '*10)
vitorias = 0
while True:
    jogada = int(input('Valor: '))
    pi = str(input('Par ou ÍMPAR? [P/I] '))
    print('=-= '*10)
    pc = randint(0,10)
    if pi == 'P': #jogador escolher PAR
        if (jogada+pc)%2==0:
            vitorias += 1
            print(f'Venceu! Computador jogou {pc} e você {jogada}')
        elif (jogada+pc)%2!=0:
            print(f'Perdeu! Computador jogou {pc} e você {jogada}')
            break
    elif pi == 'I': #jogador escolher ÍMPAR
        if (jogada+pc)%2!=0:
            vitorias += 1
            print(f'Venceu Computador jogou {pc} e você {jogada}')
        elif (jogada+pc)%2==0:
            print(f'Pereu! computador jogou {pc} e você {jogada}')
            break
print('PERDEU!')
print('=-= '*10)
print(f'Você venceu {vitorias} vezes!') """

#! Desafio 69
    #? Leia idade e sexo de várias pessoas. Para cada pessoa, perguntar se vai ou não continuar, no final mostrar: quantas pessoas tem mais de 18 anos, quantos homens cadastrados e quantas mulheres tem mais de 20 anos

""" dezoito=h=m=0
while True:
    idade = int(input('idade: '))
    if idade >=18:
        dezoito+=1
    while True:
        s = str(input('Sexo: [M/F]')).upper().strip()
        if s in 'MmFf':
            break
    if s in 'Ff':
        if idade>20:
            m+=1
    elif s in 'Mn':
        h+=1
    while True:
        continuar = str(input('Continuar? [S/N]')).upper().strip()[0]
        if continuar in 'SsNn':
            break
    if continuar in 'Nn':
        break
print(f'Tem {dezoito} pessoas com mais de 18 anos, {h} homens cadastrados e {m} mulheres com mais de 20 anos') """

#! Desafio 70
    #? Programe que leia o nome e preço de vários produtos. O programa deverá pergutar se o usuário vai continuar. No final mostre: total gasto, quantos produtos custam mais de R$1000.00, nome do produto mais barato
""" c=total=caro=mil=barato=0
while True:
    nome = str(input('Produto: '))    
    preco = float(input('Preço: R$'))
    c+=1
    total+=preco
    if preco>1000:
        mil+=1
    if c==1:
        barato=preco
        caro=preco
        maisbarato=nome
        maiscaro=nome
    elif c>1:
        if preco<barato:
            barato=preco
            maisbarato=nome
        elif preco>caro:
            caro=preco 
            maiscaro=nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N]')).upper().strip()[0]
    if continuar=='N':
        break
print(f'Total: R${total}')
print(f'Tem {mil} produtos custando mais de R$1000.00!')
print(f'O mais barato é o/a {maisbarato} e custa R${barato}!')
print(f'O mais caro é o/a {maiscaro} e custa R${caro}!') """

#! Desafio 71
    #? Simlador de caixa eletrônico. Perguntar o valor a ser sacado (inteiro) e o programa vai informar quantas células de cada valor serão entregues. COnsidere cédulas de 50,20,10 e 1
""" cinquenta=vinte=dez=um=0
sacar=int(input('Valor a sacar: R$'))
while True:
    if sacar>=50:
        cinquenta=sacar//50
        resto=sacar%50
        sacar=resto
    elif sacar>=20:
        vinte=sacar//20
        resto=sacar%20
        sacar=resto
    elif sacar>=10:
        dez=sacar//10
        resto=sacar%10
        sacar=resto
    elif sacar>=1:
        um=sacar//1
        resto=sacar%1
        sacar=resto
    elif resto==0:
        break
print(f'{cinquenta} cédulas de RS50.\n{vinte} cédulas de R$20.\n{dez} cédulas de R$10.\n{um} cédulas de R$1 ')
 """

""" valor = int(input('valor a sacar: R$'))
total = valor
cedula=50
n=0
while True:
    if total>=cedula:
        total-=cedula
        n+=1
    elif total<cedula:
        if n>0:
            print(f'{n} cédulas de R${cedula}')
        if cedula==50:
            cedula=20   
        elif cedula==20:
            cedula=10
        elif cedula==10:
            cedula=1
        n=0
        if total==0:
            break """