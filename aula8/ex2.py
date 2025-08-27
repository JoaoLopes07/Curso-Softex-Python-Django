palavra = input('Digite uma palavra: ').lower()

nova_palavra = palavra.replace('a', '1').replace('e', '2').replace('i', '3').replace('o', '4').replace('u', '5')

print(nova_palavra)
print(palavra)