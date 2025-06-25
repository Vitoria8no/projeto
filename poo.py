   
class celular:
    marca ='Nokia'
    modelo = 'tijolão'
    cor = 'azul'
    tem_camera = False
    bateria = 'infinita'
    def fazer_ligações(self):

        print('fazendo ligação...')

    def jogar_cobrinha(self):
        print('jogando cobrinha...')

    def despertador(self):
        print('despertando...')
    def calcular(self,v1,v2):
        return v1 + v2

celular =celular()

calculado = celular.calcular(2,4)
print(calculado)




