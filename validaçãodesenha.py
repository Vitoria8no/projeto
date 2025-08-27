senha_correta ="1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha = input("digite sua senha:")
    if senha == senha_correta:
        print("acesso permitido")
        break
    else:
        tentativas +=1
    print("senha incorreta.tentativas restantes:",max_tentativas-tentativas)
if tentativas == max_tentativas:
    print("acesso bloqueado")
