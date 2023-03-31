nome = input('Digite seu nome: ').strip().upper()
altura = float(input('Digite sua altura: ')) / 100
peso = float(input('Digite seu peso: '))

imc = peso / (altura ** 2)

print(f'''{nome} tem {altura} de altura,
pesa {peso} quilos e seu IMC é
{imc}
''')
