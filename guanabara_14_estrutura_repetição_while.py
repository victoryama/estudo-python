#Guanabara Python3: 2 aula 14

#? Estrutura de repetição While
    #? condição - enquanto não algo: repetir o laço
    #? não se tem um limite
        #? com limite ou não pode se usar o while
    #? estrutura de repetição com teste lógico

#while algo:
    #comando
#comando

""" c = 1
while c<10:
    print(c)
    c += 1
print('terminou') """

""" r = 'S'
while r == 'S' or r == 's':
    v = int(input('Valor: '))
    r = str(input('Continurar? [S/N]'))
print('terminou') """

""" n = 1
par = impar = 0
while n != 0:
    n = int(input('Valor: '))
    if n != 0:
        if n%2==0:
            par += 1
        else:
            impar += 1
print('{} números pares e {} números ímpares'.format(par,impar)) """

#! Desafio 57
    #? leia o sexo de uma pessoa, mas só aceite M ou F, caso o contrário peça novamente até ter um valor correto
""" SEXO = str(input('SEXO: '))
while SEXO not in 'MmFf':
    SEXO = str(input('SEXO: ')) 
SEXO = SEXO.strip().upper()
if SEXO == 'M' or SEXO == 'm':
    saida = 'Masculino'
elif SEXO =='F' or SEXO =='f':
    saida = 'Feminino'
print('Seu sexo: {}'.format(saida)) """

#! Desafio 58
    #? desafio 28, computador vai pensar em um número entre 0 a 10, no entanto o jogador vai tentar advinhar até acertar, mostrando quantas tentativas foram necessárias
""" from random import randint 
n = randint(1,10)
print(n)
tentativa = 0
advinhar = int(input('Número: '))
while advinhar != n:
    advinhar = int(input('Número: '))
    tentativa += 1
print('Foram necessárias {} tentativas para advinhar o número {}'.format(tentativa, n)) """

""" from random import randint 
n = randint(0,10)
print(n)
tentativa = 0
acertou = False
while not acertou:
    jogada = int(input('Número: '))
    tentativa += 1
    if jogada == n:
        acertou = True
    elif jogada != n:
        if jogada>n:
            print('menos')
        elif jogada<n:
            print('mais') 
print('foram necessárias {} tentativas para advinhar o número'.format(tentativa)) """

#! Desafio 59
    #? leia dois valores e mostre um meno na tela: 1=soma, 2=multiplicar, 3=maior, 4=novos, 5=sair. realizar a operação em cada fase
""" n1 = float(input('Primeiro: '))
n2 = float(input('Segundo: '))
comando = 0
while comando != 5:
    print('-=-'*20)
    print('Comandos: \n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa')
    comando = int(input('Comando: '))
    if comando == 1:
        s=n1+n2
        print('{} + {} = {}'.format(n1,n2,s))
    elif comando == 2:
        m=n1*n2
        print('{} x {} = {}'.format(n1,n2,m))
    elif comando == 3:
        if n1>n2:
            print('{} > {}'.format(n1,n2))
        elif n1<n2:
            print('{} < {}'.format(n1,n2))
        else:
            print('{} = {}'.format(n1,n2))
    elif comando == 4:
        n1 = float(input('Primeiro: '))
        n2 = float(input('Segundo: '))
    elif comando == 5:
        print('-fim-'*20)
    else:
        print('recomeçando')
print('FIM') """

#! Desafio 60
    #? leia um número qualquer e mostre seu fatorial
""" n = float(input('Número: '))
fat = n
while n != 1:
    print('n é', n)
    #fat = n*(n-1)
    n = n - 1
    #print('agora n é', n)
    fat = fat*n
print('fim')
print(fat) """
""" n = int(input('número> '))
c = n
f = 1
print('Fatorial de : {}!='.format(n),end='')
while c>0:
    print('{}'.format(c),end='')
    if c>1:
        print('X',end='')
    else:
        print('=',end='')
    f = f*c
    c -= 1
print('{}'.format(f)) """

#! Desafio 61
    #? Desafio 51, de forma a mostrar a PA usando while
primeiro = float(input('Primeiro termo: '))
razao = float(input('Razão: '))
n = 0
while n < 10:
    primeiro = primeiro + razao
    n += 1
    print(primeiro)
print('fim')

#! Desafio 62
    #? Melhore o desafio 61, perguntando se ele quer mostrar mais alguns termos, e encerrar quando mostrar 0 termos
""" primeiro = float(input('Primeiro termo: '))
razao = float(input('Razão: '))
n = 0
while n < 10:
    print(primeiro, end=', ')
    primeiro = primeiro + razao
    n += 1
mais = int(input('Quantos a mais?'))
if mais>=1:
    c = 0
    while c < mais:
        print(primeiro, end=', ')
        primeiro = primeiro + razao
        c += 1
elif mais==0:
    print('Finalizado')
 """
#! Desafio 63
    #? leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência fibonacci

#! Desafio 64
    #? leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos números foram digitrados e qual foi a soma entre eles. (desconsiderando o flag)
""" n = 0
c = 0
soma = 0
while n != 999:
    n = int(input('Número: '))
    if n != 999:
        c += 1
        soma += n
   
print('{}números digitados, soma é de {}'.format(c,soma)) """

""" n = 0
c = 0
soma = 0
n = int(input('Número: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Número: '))

print('{}números digitados, soma é de {}'.format(c, soma)) """


#! Desafio 65
    #? leia vários números inteiros pelo teclado, No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
""" n = int(input('Digite um número: '))
d = 1
maior = n
menor = n
soma = n
continuar = ''
while continuar != 'N':
    continuar = str(input('Continuar? [S/N]'))
    if continuar == 'S':
        d += 1
        n = int(input('Número: '))
        soma += n
        if n >= maior:
            maior = n
        elif n <= n:
            menor = n
m = soma/d
print('A média foi de {}, e o maior foi {} e o menor foi {}'.format(m, maior, menor)) """

""" continuar = 'S'
soma=menor=maior=q=0
while continuar in 'Ss':
    n = int(input('Número: '))
    soma += n
    q += 1
    if q==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        elif n<menor:
            menor=n
    continuar=str(input('Continuar? [S/N] ')).upper().strip()[0] #para considerar apenas a primeira letra
m = soma/q
print('digitados {} número, a média é de {}. \nO maior número foi {} e o menor {}'.format(q,m,maior,menor)) """