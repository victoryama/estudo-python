#Guanabara Python3: 3 aula 23

#? Tratamentos de erros e exceções
#? Toda exceção é uma exception - erro que não ocorre sempre

    #? Comando try e except e else: tente alguma coisa (try) se não acontece uma exceção (except) caso dê certo (else) dando certo ou não (finally)

""" try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
#? pode ter vários erros para cada tipo de exceção
#except:
#    print('Infelizmente tivemos um problema: ')
except (ValueError, TypeError):
    print('Tivemos um problema com os dipos de dados que vc digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('Usuario preferiu não informar os dados')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!') """

#! Desafio 113
    #? Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

""" def leiaint(entrada):
    #looping
    while True:
        try:
            n=int(input(entrada))
        except(ValueError, TypeError):
            print('Erro: digite um inteiro válido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompido pelo usuário.')
            return 0
        else:
            return n


#pricipal 
num = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {num}')  """

#! Desafio 114
    #?Crie um código em Python que testa se o site Pudim está acessível pelo computador usado
""" import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Tudo OK')
    print(site.read()) """ #mostra o código inteiro do site
