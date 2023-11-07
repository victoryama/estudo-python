#Guanabara Python3: 3 aula 21

#? Funções: 
    #? interective help, docstring, argumentos opcionais, escopo de variáveis, retorno de resultados

#* Interactive Help
    #? função: help()
        #?Manul completo Pode digitar qualquer comando, função e biblioteca e receberá o manual
        #? para sair usar: quit
       
#help(print)#? digitar no promp ou no script
#print(input.__doc__)

#* Docstrings
    #? Uma string de documentação, manual a ser exibido durante uma ajuda interativa
    #? Para que possa usar o manual de uma função criada, usar o docstrings, logo depois do comando def
    #? para começar """ manual """

 #! exemplo   
""" def contador(i, f, p): #? Contador, parâmetros formais i=inicio, f=fim e p=passo """
    #"""-> Faz uma contagem e mostra na tela.
    #:param i: início da contagem
    #:param f: fim da contagem
    #:param p: passo da contagem
    #:return: sem retorno
    #"""
    #""" c=i
    #while c<=f:
    #    print(f'{c}',end='..')
    #    c+=p
    #print('FIM!')


#contador(2,10,2) #?Parâmetro real é copiado para os parâmetros formais
#help(contador)

#* Parâmetros opcionais
    #? caso um parâmetro não receba um valor
#! Exemplo
#def somar(a=0,b=0,c=0):
    #"""
    #-> Faz a soma dos três valores e mostra o #resultado na tela.
    #: para a: pimeiro valor
    #: para b: segundo valor
    #: para c: terceito valor
    #"""    
    #s=a+b+c
    #print(f'A soma vale {s}')


""" somar(3,2,5)
somar(8,4)
somar()
somar(b=4, c=2)
somar(c=3, a=2)
help(somar)  """


#* Escopo de Variáveis
#!Exemplo
""" def teste(b):
    a=8 #uma outra variável a, local
    global a #para usar a variável global e não criar outra
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}') """
#dentro da função tem as variáveis locais b e c


#fora da função tem a variável global a
""" a=5
teste(a)
print(f'A fora vale {a}') """
#caso se usasse uma variável local fora da função, teria um erro

""" def funcao():
    n1=4
    print(f'N1 dentro vale {n1}')


n1=2
funcao()
print(f'N1 fora vale {n1}') """


#* Retorno de valores
    #? para personalizar resultados, para poder ter um retorno do resultado, sem escrever de qualquer forma 
    #! return s

#!Exemplo
""" def somar(a=0,b=0,c=0):
    s=a+b+c
    return s


r1=somar(3,2,5)
r2=somar(1,7)
r3=somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}') """

#! Exercícios
#?fatorial
""" def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f*=c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

#? Par ou ímpar
def parouimpar(n=0):
    if n%2==0:
        return 'Par'
    else:
        return 'Ímpar'


print(parouimpar(int(input('Digite um número:')))) """

#! Desafio 101
    #?Programa que tenha uma função chamada voto() que receba o ano de nasicmento de uma pessa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
""" from datetime import date
#função
def voto(ano):
    idade = date.today().year - ano
    print(f'Com {idade} anos:',end=' ')
    if idade<16:
        print('NEGADO')
    elif 16<=idade<18 or idade>65:
        print('OPCIONAL')
    else:
        print('OBRIGATÓRIO')


#retorno
voto(int(input('Em que ano você nasceu? '))) """

#! Desafio 102
    #? Programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
#função fatorial
#def fatorial(n=1, show=False):
    #"""-> Calcula o fatorial de um número.
    #:param n: o número a ser calculado.
    #:param show: (opcional) mostrar ou não a conta.
    #:return: valor do fatorial de um número n"""
    #i=1
    #for c in range (n,0,-1):
    #    if n<0:
    #        print('Não é possível calcular fatorial de número negativo!')
    #    elif show:
    #        print(c, end='')
    #        if c>1:
    #            print(' x ', end='')
    #        else:
    #            print(' = ', end='')
    #    i*=c
    #return i


""" num=int(input('Calcular Fatorial de: '))
print(fatorial(num, show=True))
help(fatorial) """

#! Desafio 103
    #? Programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

""" def ficha(a,b):
    if a=='':
        a='<desconhecido>'
    if b=='':
        b='0'
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


nome=input('Nome do Jogador: ')
gols=input('Número de Gols: ')
ficha(nome,gols) """

""" def ficha(a='<desconhecido>',b=0):
        print(f'O jogador {a} fez {b} gol(s)no campeonato.')


#principal
nome=str(input('Nome do jogador: '))
gols=str(input('Número de Gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()=='':
    ficha(b=gols)
else:
    ficha(nome,gols) """

#! Desafio 104
    #? Programa que tenha função leiaint(), que vai funcionar de forma semelhante â função input() do python, só que fazendo a validação para aceitar apenas um valor numérico.
""" #função
def leiaint(n):
    if n.isnumeric():
        print(f'Você acabou de digitar o número {n}')
    else:
        print('ERRO! Digite um número inteiro válido.')


#programa principal
while True:
    numero=input('Digite um número: ')
    if numero.isnumeric():
            leiaint(numero)
            break
    else:
        print('ERRO! Digite um número inteiro válido.') """


""" def leiaint(msg):
    ok = False
    valor = 0
    while True:
        numero= str(input(msg))
        if numero.isnumeric():
            s=int(numero)
            ok = True
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return s


n=leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}') """

""" def leiaint(entrada):
    #looping
    while True:
        n=input(entrada)
        if n.isnumeric():
            numero=n
            break
        else:
            print('ERRO! Digite um número inteiro válido!')
    return numero


#pricipal 
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}') """

#! Desafio 105
    #? Programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: quantidade de notas, maior nota, menor nota, média da turma, situação (opcional). Add as docstrings da função

#função
#def notas(*n, sit=False):
    #"""
    #-> Função para analisar notas e situações de vários alunos.
    #:param n: uma ou mais notas dos alunos (aceita várias)
    #:param sit: valor opcional, indicando se deve ou não adicionar a situação
    #:return: dicionário com várias informações sobre a situação da turma
    #"""
    #r={}
    #r['total']=len(n)
    #r['maior']=max(n)
    #r['menor']=min(n)
    #r['média']=sum(n)/len(n)
    #if sit is True:
    #    if r['média']>=7:
    #        r['situação']='BOA'
    #    elif r['média']>=5:
    #        r['situação']='Razoável'
    #    else:
    #        r['situação']='RUIM'
    #return r


#programa principal
#oletim=notas(5.5,2.5,1.5, sit=True)
#print(boletim)
#help(notas)

#! Desafio 106
    #? Mini-sistema que utilize o intrective Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "fim", o programa se encerrará. OBS: use cores
from time import sleep
""" c=('\033[m',        # 0 - sem cor
'\033[0;30;41m',    # 1 - vermelho
'\033[0;30;42m',    # 2 - verde
'\033[0;30;43m',    # 3 - amarelo
'\033[0;30;44m',    # 4 - azul
'\033[0;30;45m',    # 5 - roxo
'\033[7;30,'        # 6 - branco
); """

#def ajuda(comando):
#    titulo(f'Acessando o manual do comando \'{comando}\'',4)
#    print(c[6], end='')
#    help(comando)
#    print(c[0], end='')
#    sleep(2)


#def titulo(mensagem, cor=0):
#    tam=len(mensagem)+4
#    print(c[cor], end='')
#    print('~'*tam)
#    print(f'  {mensagem}')
#    print('~'*tam)
#    print(c[0], end='')
#    sleep(2)



#principal
#cmd=''
#while True:
#    titulo('SISTEMA de AJUDA PyHELP', 2)
#    cmd=input('Função ou biblioteca> ')
#    if cmd.upper()=='FIM':
#        break
#    else:
#        ajuda(cmd)
#titulo('ATÉ LOGO!', 1)
