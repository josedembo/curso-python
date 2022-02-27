
def calcula_media():
    arquivo = open("notas_alunos.txt", "r")
    arquivo_lido = arquivo.read()
    lista_notas  = []
    dados_alunos = arquivo_lido.split("\n")
    for dado_aluno in dados_alunos:
        dados_notas = {}
        notas_aluno = dado_aluno.split(",")
        nome_aluno = notas_aluno.pop(0)
        media_aluno = lambda notas: sum([int(nota) for nota in notas])/len(notas)
        dados_notas["nome"] = nome_aluno
        dados_notas["media"] = media_aluno(notas_aluno)
        lista_notas.append(dados_notas)
    print(lista_notas)
    return  lista_notas

if __name__ == "__main__":
    calcula_media()