#Guanabara Python3: 3 aula 22

#* Modularização: construir módulos
    #? resolver problemas de programas grande
        #! dividir programas grandes
        #! aumentar a legibilidade
        #! Facilitar a manutenção
        #! Vantagens:
            #? organizaçãod e código
            #? facilidade na manutenção      
            #? ocultação de código detalhado
            #* reutilização em outros projetos- precisa colocar o arquivo na mesma pasta do projeto

#! Exemplo
#? Arquivo de módulo a parte, com as funções
#import modulos
#? para pegar as funções, esse formato não é recomendável, pois pode ter outras bibliotecas com o mesmo nome, será utlizado a última importada
#?pode fazer no formato: from modulo import fatorial
""" num=int(input("Inteiro: "))
fat=modulos.fatorial(num) #? para referenciar as funções 
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {modulos.dobro(num)}")
print(f"O triplo de {num} é {modulos.triplo(num)}") """


#* Pacotes: junção de módulos, separados por assuntos
    #? solução para quando os módulos também não conseguem satisfazer - MUITAS FUNÇÕES EM UM MÓDULO

    #? para criar pacotes: para códigos muito maiores
        #? todo arquivo .py pode ser um módulo
        #* toda pasta é considerado um pacote: criar uma pasta como pacote, podendo conter outras pastas que são pacotes
        #! Sintaxe para nomes de arquivos dentro de pacotes, arquivo especial:
            #?__init__.py

#from pacotes import operacoes
""" num=int(input("Inteiro: "))
fat=operacoes.fatorial(num) #? para referenciar as funções 
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {operacoes.dobro(num)}")
print(f"O triplo de {num} é {operacoes.triplo(num)}") """

#! Desafio 107
#? módulo moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um program que importe esse módulo e use algumas dessas funções

#from ex107 import moeda

""" p = float(input('Preço: R$'))
print(f'Metade de {p} é {moeda.metade(p)}')
print(f'Dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {p}, temos  {moeda.aumentar(p)}')
print(f'Reduzindo 13% de {p}, temos {moeda.diminuir(p)}') """

#! Desafio 108
#? Adaptar desafio 107, criando uma fuinção adicional chamada moeda() que consifa mostrar os valroes como um valor monetário formatado
#from ex108 import moeda

""" p = float(input('Preço: R$'))
print(f'Metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'Dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos  {moeda.moeda(moeda.aumentar(p))}')
print(f'Reduzindo 13% de {moeda.moeda(p)}, temos {moeda.moeda(moeda.diminuir(p))}') """

#! Desafio 109
#? Modifique funções no desafio 107m para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatada pela função moeda(), do desafio 108

#from ex109 import moeda

""" p = float(input('Preço: R$'))
print(f'Metade de {moeda.moeda(p, True)} é {moeda.metade(p)}')
print(f'Dobro de {moeda.moeda(p, True)} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13% de {moeda.moeda(p)}, temos {moeda.diminuir(p, 13, True)}') """

#! Desafio 110
#? Adicione ao módulo moeda.py uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui
""" from ex110 import moeda
p=float(input('Preço: R$'))
moeda.resumo(p, 80, 35) """

