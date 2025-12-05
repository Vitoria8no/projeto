t1 = float(input('primeiro segmento'))
t2 = float(input('segundo segmento'))
t3 = float(input('terceiro segmento'))

if t1< t2 + t3 and t2< t1 +t3 and t3< t2 + t1:
    print('os segmento acima podem formar um triangulo!')
if t1 == t2 == t3:
        print('Equilatero!')
if t1 != t2 != t3:
      print('Escaleno!')
else:
    print('Isosceles')  
