nome = input('Digite o nome: ').strip().upper()
sobrenome = input('Digite o sobrenome: ').strip().upper()
idade = int(input('Digite a idade: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
maior_de_idade = ' '
if idade >= 18:
    maior_de_idade = 'SIM'
else:
    maior_de_idade = 'NÃO'
altura_metros = float(input('Digite a altura: ')) / 100

print('Nome', nome)
print('Sobrenome', sobrenome)
print('Idade', idade)
print('Ano de nascimento', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros', altura_metros)
