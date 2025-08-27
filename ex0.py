'''nome = 'João'
print(nome)

nome = input('Digite seu nome: ')
print(nome)
nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite seu Sexo(M/F): '))
idade = int(input('Digite sua Idade: '))
print(f'Seu nome é {nome}\nSeu sexo é {sexo}\nSua Idade é {idade}')
if idade > 17:
    print('Você é de Maior')
else:
    print('Você é de Menor')

numero = int(input('Digite seu número: '))
print(f'Seu número é {numero}')

subtracao = numero - 2
print(f'{numero} - 2 = {subtracao}')

multiplicaao = numero * 2
print(f'{numero} * 2 = {multiplicaao}')

divisao = numero / 2
print(f'{numero} / 2 = {divisao}')

divisao_inteira = numero // 2
print(f'{numero} // 2 = {divisao_inteira}')

resto_divisao = numero % 2
print(f'{numero} % 2 = {resto_divisao}')

potencia = numero ** 2
print(f'{numero} ** 2 = {potencia}')'''

email = str(input('Digite o seu Email: '))
senha = str(input('Digite a sua Senha: '))
senha_confirme = str(input('Confirme a sua Senha: '))

if senha == senha_confirme:
    True
else:
    print('Senha Incorreta')
