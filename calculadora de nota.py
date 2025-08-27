#calculadora
aluno = input("qual é seu nome:")
nota1= float(input("digite primeira nota:"))
nota2 =float(input("digite segunda nota:"))
nota3 =float(input("digite terceira nota:"))
nota4 =float(input("digite quarta nota:"))
media = (nota1 + nota2 + nota3)/3
if media >=7:
    print("resultado:aprovado")
else:
    print("resultado:reprovado")   

print(aluno)
print(media) 
