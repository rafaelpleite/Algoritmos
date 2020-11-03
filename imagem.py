# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Rafael Prudêncio Leite
    NUSP: 11224852

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não 
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte: Usei as funções o último EP

'''

#-------------------------------------------------------------------------- 

class Imagem:
    '''
    Implementação da classe Imagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Imagem
    def __init__(self,nlins, ncols, valor=0):
        self.nlins = nlins
        self.ncols = ncols
        self.valor = valor
        self.matriz = imagem_nova(nlins, ncols, valor)
    
    def __str__(self):
        matriz = self.matriz
        s = f'{cria_imagem(matriz)}'
        return s
    
    def size(self):
        nlins = self.nlins
        ncols = self.ncols
        return (nlins,ncols)
    
    def get(self, lin, col):
        matriz = self.matriz
        return matriz[lin][col]
    
    def put(self, lin, col, valor):
        matriz = self.matriz
        matriz[lin][col] = valor
        self.matriz = matriz
    
    def crop(self, left=0, top=0, right=0, bottom=0):
        matriz = self.matriz
        s = imagem_regiao(matriz, left, top, right, bottom)
        return Imagem(len(s), len(s[0]), s[0][0]) 
    

    
    
def imagem_nova(nlin, ncol, valor):
    l = []
    for i in range(nlin):
        m = []
        for j in range(ncol):
            m.append(valor)
        l.append(m)
    return l


def cria_imagem(matriz):
    imagem = str()
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):
            imagem += str(matriz[i][j])
            if j < len(matriz[i])-1:
                imagem += ', '
        imagem += '\n'
    return imagem

def imagem_regiao(imagem, left, top, right, bottom):
    if bottom == 0:
        bottom = len(imagem)
    if right == 0:
        right = len(imagem[0])
    matriz_regiao = []
    for i in range(top, bottom): #3 - 0 acessando linhas
        complemento = []
        for j in range(left, right): #4 - 1 acessando colunas
            complemento.append(imagem[i][j])
        matriz_regiao.append(complemento)
    return(matriz_regiao)
    
    
    
    
    
    
    
