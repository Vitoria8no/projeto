#funções do python:
#conjunto ou bloco de comando que executa alguma tarefa ou ação.
#geralmente essa função recebe parametros,executa uma ação  e devolve algum resultado.
#que pode ser chamado de retorno.

#print("ola mundo")função
#len()função
#input() função
#def()função do python

#def nome funcão(parametro):
#instruçoes
#instruçoes
#instruçoes
#return valor(opcional)
def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor *0.1
    elif valor >2000:
        imposto = valor *0.13
    else:
        imposto =valor *0.2
    return imposto


preco_produto1 = 2500
preco_produto2 = 3500
imposto_produto1 =calcular_imposto(preco_produto1)
imposto_produto2 =calcular_imposto(preco_produto2)
print(imposto_produto1)
print(imposto_produto2)

