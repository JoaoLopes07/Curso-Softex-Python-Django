while True:
    numero = input('Digite seu número com 11 dígitos: ')

    if numero.isdigit() and len(numero) == 11:
        repeticao = False
        for i in numero:
            repeticoes = 0
            for j in numero:
                if i == j:
                    repeticoes +=1
                if repeticoes >=3:
                    repeticao = True
                    break
        if repeticao:
            print('Número Inválido. 3+ digitos iguais')
        else:
            ddd = numero[:2]
            parte1 = numero[2:7]
            parte2 = numero[7:12]
            print(f'({ddd}) {parte1}-{parte2}')
            break
    else:
        print('Numero Inválido. Precisa ter 11 dígitos')