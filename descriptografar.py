from cryptography.fernet import Fernet
import os

#1. Carregar o arquivo chave.key
def carregar_chave():
    return open("chave.key", "rb").read()

#2. Descriptografar arquivo
def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

#3. Encontrar os arquivos dentro da pasta test_files
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswitch(".key"):
                lista.append(caminho)
    return lista

#4. Função principal
def main():
        chave = carregar_chave()
        arquivos = encontrar_arquivos("test_file")
        for arquivo in arquivos:
            descriptografar_arquivo(arquivo, chave)
        print("Arquivo restaurados com sucesso")

if __name__ == "__main__":
    main()
