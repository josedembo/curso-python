contador_letras = lambda  lista: [ len(x) for x in lista]
media = lambda notas: [int(nota) for nota in notas]

calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a,b: a * b,
    "divisao": lambda a, b: a /b
}


if __name__ == "__main__":
    print(contador_letras(["Morango", "Laranja"]))
    soma = calculadora["soma"]
    print(soma(20, 30))