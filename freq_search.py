import sys
import os
import glob
from os import chdir, listdir


class Noticia:
    def __init__(self, nomeArquivo, listaTokens=None):
        self.nomeArquivo = nomeArquivo
        self.listaTokens = listaTokens

def extracaoDasNoticias():
    arquivos = [arq for arq in listdir() if os.path.isfile(arq) and arq.lower().endswith(".txt")]
    print(arquivos)
    noticias = []
    for noticia in arquivos:
        noticias = Noticia(noticia)
    return noticias

def preProcessamento():
    listaNoticias = extracaoDasNoticias()
    


if __name__ == "__main__":
    caminhoDiretorio = sys.argv[1]
    termos = sys.argv[2]

    if(os.path.exists(caminhoDiretorio)):
        chdir(caminhoDiretorio)
        preProcessamento()

    else:
        print("Caminho para diretório inválido. Por favor, tente novamente!")
