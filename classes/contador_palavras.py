def contador_letras(lista_palavras:list):
    letras_contadas = []
    for palavra in lista_palavras:
        numero = len(palavra)
        letras_contadas.append(numero)

    return  letras_contadas

if __name__ == "__main__":
    lista = ["Morango", "Banana", "Batata", "Pêssigo"]
    contagem = contador_letras(lista)
    print(contagem)


