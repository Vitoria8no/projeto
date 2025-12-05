print('{:=^40}'.format('lojas guanabara'))
preco = float(input('preco das compras: R$'))
print(''' FORMAS DE PAGAMENTOS
      [1] à vista dinheiro/pix
      [2] à vista cartão
      [3] à 2x no cartão
      [4] à 3x ou mais no cartão''')

opção = int(input('qual vai ser a forma de pagamento?'))
if opção == 1:
    total = preco - (preco * 10/100)
elif opção == 2:
    total = preco - (preco * 5/100)
elif opção == 3:   
    total = preco 
    parcela = total/2
    print('sua compra sera parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:    
    total = preco + (preco * 20/100)
    totparc  = int(input('quantas parcelas?'))
    parcela = total/ totparc
    print('sua compra sera parcelada em {}x de R${:.2f}'.format(totparc, parcela))
print('sua compra de R${:.2f} vai custar R${:.2f} mo final.'.format(preco, total))