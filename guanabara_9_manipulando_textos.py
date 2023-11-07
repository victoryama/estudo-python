#Guanabara Python3: 1 aula 9

#? Cadeia de caracteres = uma frase, sempre entr '' ou """
    #? cada letra irá ficar dentro de um espaço na memória
    #? operações com as cadeias
frase = 'Curso Em Video Python' #?20 caracteres

        #? fatiamento de string = relação de uma parte ou um intervalo através dos índices 
            #? ex: frase[9], frase[9:13] OBS: irá pegar um a menos q o final 
            #? frase[9:21:2] intervalo entre 9 e 20 pulando em 2 em 2
            #? frase[:5] quando se omite o primeiro, ele começa do início
            #? frase[15:] quando se omite o final, ele termina no último
            #? frase[9::3] 
            #? frase
        
#print(frase[1:3])
#print(frase[5:9])
#print(frase[:21])
#print(frase[::3])

        #? análise = saber informações de string
            #? len(frase) = comprimento da frase, caracteres da frase = N° caracteres + 1
            #? frase.count('o') = contar quantas vezes aparecem a letra em ''
                #? frase.count('o',0,13) contagem com fatiament
            #? frase.find('deo') = em que momento começou
                #? posição -1 quer dizer q não existe o que se procura
            #? 'curso' in frase = operador in, se existe a palavra True ou Fals

#print(len(frase))
#print(frase.count('o'))
#print(frase.count('o',0,13))
#print(frase.find('deo'))
#print(frase.find('android'))
#print(frase.find('Em'))
#print('curso' in frase)

        #? Transformação, apesar de lista de string ser imutável, pode se realizar alguns métodos
            #? frase.replace('python', 'android')= troca o primeiro pelo segundo
            #? frase.upper() = transformar em maiúculas
            #? frase.lower() = transformar em minúsculas
            #? frase.capitalize() = deixar apenas o primiro em maíusculo e o resto em minúsculo
            #? frase.title() = deixar o primeiro caracter de cada palavra em maísuclo
            #? frase.strip() = remove espaços no início e final
            #? frase.rstrip() ou frase.lstrip() = remover apenas da direita (r) ou esquerda (l)

#linha = frase.replace('python', 'android')
#print(frase.replace('python', 'android'))
#print(linha)
#FRASE = frase.upper()
#print(FRASE)
#print(frase.title())
#string = '   Aprendendo Python  '
#print(string.strip())
#print(string.rstrip())

        #? Divisão de Strings
            #? frase.split() = realizado uma divisão nos espaços da frase/string em lista
        #? Junção
            #? '-'.join(frase) = junção da lista, oq está em '' será oq irá juntar a lista
nova = frase.split()
print(nova)
print('-'.join(nova))
print(' '.join(nova))
teste=''.join(nova)
print(teste)
print(type(teste))

#! Desafio 22
    #? Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todos as letras maiúsculas, o nome com todos minúsculos, quantas letras ao todo (sem considerar os epaços) e quantas letras tem o primeiro nome

#nome_completo = input('Qual seu nome completo? ')
#maior = nome_completo.upper()
#menor = nome_completo.lower()
#sep = nome_completo.split() #lista
#sem = ''.join(sep)
#letras_completo = len(sem)
#teste print(sep)
#nome = sep[0] #? selecionar item da lista
#teste print(nome)
#letras_nome = len(nome)
#print('Seu nome é {}. \nEm maísculo é {} e em minúsculo {}'.format(nome_completo, maior, menor))
#print('O total de letras é {}. '.format(letras_completo), end='')
#print('Seu primeiro nome tem {} letras'.format(letras_nome))

#! Desafio 23
    #? Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados.
#n = int(input('Digite um número entre 0 a 9999: '))
#print(type(n))
#print(n[1])
#u = n // 1 % 10
#d = n // 10 % 10
#c = n // 100 % 10
#m = n // 1000 % 10
#print('O número {} tem: '.format(n))
#print('{} unidades'.format(u))
#print('{} dezenas'.format(d))
#print('{} centas'.format(c))
#print('{} milhares'.format(m))


#! Desafio 24
    #? Faça um programa que leia o nome de uma cidade e dia se ela começa ou não com o nome santo
#nome = input('Digite o nome de uma cidade: ')
#lista = nome.split()
#primeiro = lista[0].upper()
#resposta = 'SANTO' in primeiro
#print(lista)
#print(primeiro)
#print(resposta)
#print('Sua cidade possui o nome "SANTO": {} '.format(resposta))

#! Desafio 25
    #? Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
#nome_completo = input('Seu nome completo: ')
#nome = nome_completo.upper()
#resposta = 'SILVA' in nome
#print('Seu nome {},\npossui o nome "SILVA": {}' .format(nome_completo, resposta))

#! Desafio 26
    #? Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra A, em que posição ela aparece a primeira vez e em qual posição ela aparece a última vez
#entrada = input('Digite uma frase: ')
#frase = entrada.upper()
#print('Aparece {} vezes.'.format(frase.count('A'))) #quantas vezes aparece
#print('Aparece a primeira vez em {}.'.format(frase.find('A'))) #primeirta vez
#print('Aparece a última vez em {}.'.format(frase.rfind('A'))) #última vez

#! Desafio 27
    #? Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro eo últumo nome separadamente
#nome_completo = input('Digite seu nome completo: ')
#nome = nome_completo.split()
#n = len(nome)
#print('Seu primeiro nome é {} \ne seu último nome é {}'.format(nome[0],nome[n-1]))