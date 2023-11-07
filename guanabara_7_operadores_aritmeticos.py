#Guanabara Python3: 1 aula 7

#OBS cores em comentários
    #
    #!   
    #*
    #?
    #//

#? operadores aritméticos 
    #? operando binário
    #? serve em strings
#?  + adição
#?  - subtração
#?  * multiplicação
#?  / divisão
#?  ** potência
#?  // divisão inteira
#?  % resto de divisão (módulo) 
#?  == se é igual
#?  **(1/2) raiz quadrada
#?  **(1/n) raiz a n    

#? ordem de precedência
#? 1° ()
#? 2° **
#? 3° * / // % fazer quem aparece primeiro
#? 4° + -

#? função de potência pow(a,b) quebra a ordem de precedência
#potencia = int(pow(3,3))
#print(3**3)
#print(potencia)
#rint(pow(3,3))

#? operadores em print
#nome = input('seu nome: ')
#print('prazer {}!'.format(nome))
#print('prazer {:10}!'.format(nome))
#print('prazer {:>10}!'.format(nome))
#print('prazer {:<10}!'.format(nome))
#print('prazer {:=^10}!'.format(nome))

#* usar uma variável a mais quando precisar utilizar usa-la depois, se não utilizar diretamente com operador

#n1 = int(input('digite um número: '))
#n2 = int(input('digite outro número: '))
#s = n1 + n2
#m = n1*n2
#d = n1/n2
#di = n1//n2
#exp = n1**n2
#print('n1 mais n2 = {}, n1 vezes n2 = {}, n1 dividido por n2 = {:.3f}'.format(s,m,d))
#? em end='' para não quebrar a linha
#? em {:.3f} é definido a quantidade de casas decimais
#print('divisão inteira de n1 por n2 = {}, exponencial de n1 por n2 = {}'.format(di,exp))
#? em end='' para não quebrar a linha, para quebrar a linhausar \n
#print('n1 mais n2 = {}, n1 vezes n2 = {}, n1 dividido por n2 = {:.3f}. '.format(s,m,d), end='')
#print('Divisão inteira de n1 por n2 = {}, exponencial de n1 por n2 = {}'.format(di,exp))
#print('n1 + n2 = {} \n n1*n2 = {}'.format(s,m))

#! Desafio 5
    #? Faça um programa que leia um número inteiro e mostra na sua tela o seu sucessor e seu antecessor
#inteiro = int(input('Digite um inteiro: '))
#antecessor = inteiro - 1
#sucessor = inteiro + 1
#print('O número é {},'.format(inteiro), end='') 
#print(' seu antecessor é {}'.format(antecessor), end='')
#print(' e seu sucessor é {}.'.format(sucessor))

#! Desafio 6
    #? Crie um algorítmo que leia um númro e  mostre o seu dobro, triplo e raiz quadrada.\
#numero = float(input('Escolha um número: '))
#dobro = 2*numero
#triplo = 3*numero
#raiz = numero**(1/2)
#print('O dobro de {} é {},'.format(numero,dobro), end='')
#print(' seu triplo é {}'.format(triplo), end='')
#print(' e sua raiz quadrada é {:.2f}.'.format(raiz))

#! Desafio 7
    #? Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
#nota_1 = float(input('Digite uma de suas notas: '))
#nota_2 = float(input('Digite a sua outra nota: '))
#print('A média de suas notas é {:.2f}.' .format((nota_1 + nota_2)/2))

#! Desafio 8
    #? Escreva um programa que leia um valor em metros e o exiba convertdo em centímetros e milímetros
#medida = float(input('Qual sua medida em metros? '))
#print('A sua medid é {:.2f}m \n em centímetro é {:.2f}cm \n e em #milímetros {:.2f}mm'.format((medida),(medida*100),(medida*1000)))

#! Desafio 9
    #? Faça um programa que leia um número inteiro qualuqer e mostre na tela a sua tabuada
#inteiro = int(input('Digite um inteiro: '))
#print('A tabuada de {} é \n{}X1 = {}'.format(inteiro,inteiro,inteiro*1))
#print('{}X2 = {}'.format(inteiro,inteiro*2))
#print('{}X3 = {}'.format(inteiro,inteiro*3))
#print('{}X4 = {}'.format(inteiro,inteiro*4))
#print('{}X5 = {}'.format(inteiro,inteiro*5))
#print('{}X6 = {}'.format(inteiro,inteiro*6))
#print('{}X7 = {}'.format(inteiro,inteiro*7))
#print('{}X8 = {}'.format(inteiro,inteiro*8))
#print('{}X9 = {}'.format(inteiro,inteiro*9))
#print('{}X10 = {}'.format(inteiro,inteiro*10))

#! Desafio 11
#L = float(input('Largura da parede: '))
#A = float(input('Altura da parede: '))
#area = L*A => tinta = (L*A)/2
#para cada 2m^2 necessita de 1L de tinta
#print('Sua parede tem a dimensão de {}mx{}m e sua área é de {:.2f}m². \nPara pinta essa parede, você precisará de {:.2f}L de tinta.'.format(L, A, L*A, L*A/2))

#! Desafio 12
    #? Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
#p = float(input('Preço? R$'))
#d = p*0.95
#print('Preço final é de R${:.2f}'.format(d))

#! Desafio 13
    #? Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
#s = float(input('Qual o seu salário? '))
#print('Como amento de 15%, seu salário de R${:.2f} passa a ser R${:.2f}.'.format(s, s*1.15))

#! Desafio 15
    #? Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule e preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado
#dia = int(input('Quantos dias de aluguel? '))
#dist = float(input('Quantos Kmo rodados? '))
#p = dia*60.00 + dist*0.15
#print('Para {}dias e {}Km, o preço a ser pago é de R${}'.format(dia, dist, p))
