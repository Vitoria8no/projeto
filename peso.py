peso = float(input('qual é seu peso? (kg)'))
altura = float(input('qual é sua altura? (m)'))
imc =peso/(altura**2)
print(' o imc dessa pessoa é de {:.1f}' .format(imc))
if imc < 18.5:
    print('voce esta abaixo do peso')
elif 18.5 <= imc< 25:
    print('esta na faixa de peso normal')
elif 25 <= imc < 30:
    print('voce esta em sobrepeso')