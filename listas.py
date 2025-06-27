#listas
#carros =['uno','jeep','renault']
#print(carros)
#carros.append('corsel')
#print(carros)
#carros[0]
#print(carros[0])


vendas =[100,50,14,20,30,700]

#soma dos elementos
total_vendas=sum(vendas)
print(total_vendas)
#tamanho da listas
quantidades_vendas =len(vendas)
print(quantidades_vendas)

#maximo e minimo
print(max(vendas))
print(min(vendas))

#pegar posição
print(vendas[0])
print(vendas[3])

listas_produtos =['iphone','airpod','ipad','macbook']
#adicionar um item na lista
listas_produtos.append("apple watch")
print(listas_produtos)

#remover um item na lista
listas_produtos.remove("apple watch")
print(listas_produtos)
listas_produtos.pop(0)
print(listas_produtos)
#editar um item
precos =[1000,1500,3500]
print(precos)



#contar quantas vezes um item aparece na lista

listas_produtos =['iphone','airpod','ipad','macbook','iphone','ipad','iphone']
print(listas_produtos.count("iphone"))


#ordenar uma listas
listas_produtos.sort()
print(listas_produtos)