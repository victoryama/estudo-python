#Guanabara Python3: 1 aula 11

#? Cores do terminal: Padrão ANSI padrão de normalização internacional
    #?escape sequece
    #?cores: \033[codigom
    #? \033[estilo;cor de texto ;cor de fundo m
        #? para estilo: 0(sem estilo) 1(negrito) 4(underline) 7(inverte letra e fundo)
        #? para texto: 30(branco), 31(vermelho), 32(verde), 33(amarelo), 34(azul), 35(violeta), 36 (ciano) e 37(cinza é padrão)
        #? para fundo: mesmas ordem de cores que o texto mas equivale a 40, 41, 42, 43, 44, 45, 46 e 47
#\033[0;30;41m
#\033[4;33;44m
#\033[m
#\033[7;30m
#print('\033[4;30;45mHello world!\033[m')
#print('\033[1;31;43mHello World!')
#print('Hello World!\033[m')
#print('\033[4;32;44mHello World!\033[m')
#print('\033[0;32;40mHello World!\033[m')
#* vc deve abrir e fechar no format, por isso se tem o {} 3 vezes
#? criando lista de cores
i = 'mimimi'
print('mimimi {}{}{}' .format('\033[4;34m',i,'\033[m')) 
cores = {'limpa': '\033[m', 'azul': '\033[34m',
         'amarelo': '033[33m', 'pretobranco': '\033[7;30m'}
print('mimimi {}{}{}' .format(cores['azul'],i,cores['limpa']))