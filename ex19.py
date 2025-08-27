numero = int(input('Digite um número inteiro: '))

for i in range(4):
    maior = int(input('Digite outro número inteiro: '))

    if maior > numero:
        numero = maior

print(f'O maior número digitado foi o {numero}')
