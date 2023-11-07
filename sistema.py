from ex115.lib.interface import*
from ex115.lib.arquivo import*
from time import sleep

arq='cursoemvideo.txt'

#if arquivoExiste(arq):
#   print('Arquivo encontrado com sucesso!')
#else:
#    print('Arquivo não encontrado!')
#    criarArquivo(arq)

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta=menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome=str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema . . . Até Logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)