import shutil
import os

def escrever_arquivo(texto):
    arquivo = open("texto.txt", "a")
    arquivo.write(texto)
    arquivo.close()

def actualizar_arquivo(texto):
    arquivo = open("texto.txt", "a")
    arquivo.write(f"\n{texto}")
    arquivo.close()

def ler_arquivo(nome_arquivo:str):
    arquivo = open(nome_arquivo, "r")
    arquivo_lido = arquivo.read()
    print(arquivo_lido)
    print(type(arquivo_lido))

def copiar_arquivo(nome_arquivo:str, direcertorio:str):
    if not os.path.exists(direcertorio):
        os.makedirs(direcertorio)

    shutil.copy(nome_arquivo, direcertorio)

def mover_arquivo(nome_arquivo:str, directorio:str):
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    shutil.move(nome_arquivo, directorio)

if __name__ == "__main__":
    # escrever_arquivo("Minha primeira linha")
    # actualizar_arquivo("Minha segunda linha")
    # ler_arquivo("texto.txt")
    # copiar_arquivo("texto.txt", "copia")
    mover_arquivo("notas_alunos.txt", "notas")