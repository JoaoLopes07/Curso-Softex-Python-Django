"""Crie um programa que recebe uma frase do usuário e faz uma análise completa sobre ela,
mostrando:
● A quantidade de palavras na frase.
● A quantidade de vogais (a, e, i, o, u).
● A quantidade de consoantes.
● Se a frase é um palíndromo (ou seja, se ela pode ser lida da mesma forma de trás para
frente, ignorando espaços e letras maiúsculas).
"""


def limpa_frase(frase: str) -> str:
    return frase.replace(" ", "").lower()


def contar_palavra(frase: str) -> int:
    return len(frase.split())


def contar_vogais_consoantes(frase: str) -> tuple[int, int]:
    vogais = "aeiou"
    cont_vogais = 0
    cont_consoantes = 0

    for letra in frase:
        if letra in vogais:
            cont_vogais += 1
        elif letra.isalpha():
            cont_consoantes += 1
    return cont_vogais, cont_consoantes


def eh_palindromo(frase: str) -> bool:
    palindromo = limpa_frase(frase)
    return palindromo == palindromo[::-1]


def analise():
    frase = input("Digite uma frase: ").lower()

    palavras = contar_palavra(frase)

    vogais, consoantes = contar_vogais_consoantes(frase)

    print(
        f"A frase tem:\n{palavras} Palavras.\n{vogais} Vogais.\n{consoantes} Consoantes.\n"
    )

    if eh_palindromo(frase):
        print("A frase é um palíndromo")
    else:
        print("A frase não é um palíndromo")


analise()
