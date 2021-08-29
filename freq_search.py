import sys
import os
from os import chdir, listdir


class Noticia:
    def __init__(self, nomeArquivo, listaTokens=None):
        self.nomeArquivo = nomeArquivo
        self.listaTokens = listaTokens

def extracaoDasNoticias():
    arquivos = [arq for arq in listdir() if os.path.isfile(arq) and arq.lower().endswith(".txt")]
    noticias = []
    for noticia in arquivos:
        noticias.append(Noticia(noticia))
    return noticias

def preProcessamento():
    listaNoticias = extracaoDasNoticias()
    for noticia in listaNoticias:
        with open(noticia.nomeArquivo, 'r') as arquivo:
            texto = arquivo.read()
            texto = texto.lower()
            texto = list(filter(lambda c: c not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~', texto))
            texto = "".join(texto) #convertendo de volta para uma string
            texto = texto.replace("\n", " ")
            noticia.listaTokens = texto.split(" ")
    return listaNoticias

def calculoOverlap(termos, noticiasPreproocessadas):
    listaTermos = termos.split(" ")
    arquivo = " "
    maiorOverlap = -1
    for noticia in noticiasPreproocessadas:
        repeticoes = 0
        for termo in listaTermos:
            repeticoes += noticia.listaTokens.count(termo)
        maiorLista = len(noticia.listaTokens) if len(noticia.listaTokens) > len(listaTermos) else len(listaTermos)
        overlap = repeticoes/maiorLista
        if overlap > maiorOverlap:
            arquivo = noticia.nomeArquivo
            maiorOverlap = overlap
    return arquivo


if __name__ == "__main__":
    caminhoDiretorio = sys.argv[1]
    termos = sys.argv[2]

    if(os.path.exists(caminhoDiretorio)):
        chdir(caminhoDiretorio)
        noticiasPreproocessadas = preProcessamento()
        resultado = calculoOverlap(termos, noticiasPreproocessadas)
        with open(resultado, 'r') as texto:
            print(texto.read())

    else:
        print("Caminho para diretório inválido. Por favor, tente novamente!")
