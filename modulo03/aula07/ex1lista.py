def rotacionar_lista(lista, k):
    if not lista:
        return []
    k = k % len(lista)
    return lista[-k:] + lista[:-k]

numeros = [1, 2, 3, 4, 5]
resultado = rotacionar_lista(numeros, 2)
print(resultado)
