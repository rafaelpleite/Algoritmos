# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Rafael Prudêncio Leite
    NUSP: ********

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

    Descrição de ajuda ou indicação de fonte:

'''
import numpy as np

#-------------------------------------------------------------------------- 

class NumPymagem:
    '''
    Implementação da classe NumPymagem que tem o mesmo comportamento descrito 
    no enunciado.
    '''

    # escreva aqui os métodos da classe Pymagem
    def __init__(self,nlins, ncols, valor=0):
        if not type(valor) == np.ndarray:
            self.nlins = nlins
            self.ncols = ncols
            self.data = np.full((nlins, ncols), valor)
            self.tipo = type(valor)
        else:
            self.nlins = nlins
            self.ncols = ncols
            self.data = np.copy(valor)
            self.tipo = type(valor.tolist()[0][0])
    
    def shape(self):
        return (self.data.shape)
    
    
    def __str__(self):
        data = self.data
        s = f'{cria_imagem(data)}'
        return s
    
    def __getitem__(self, key):
        data = self.data
        return data[key]
    
    def __setitem__(self, key, valor):
        data = self.data
        data[key] = valor
        self.data = data
    
    def crop(self, left=0, top=0, right='SEMVALOR', bottom='SEMVALOR'):
        if right == 'SEMVALOR':
            right = self.ncols
        if bottom == 'SEMVALOR':
            bottom = self.nlins
        data = self.data
        s = data[top: bottom, left: right]
        return NumPymagem(0, 0, s) 
    
    def paste(self, other, tlin, tcol):
        shape_self = self.shape()
        shape_other = other.shape()
        l, c = (0,0)
        linha = tlin
        if tlin < 0:
            while linha < 0:
                linha += l
                l += 1
            l -= 1
        coluna = tcol
        if tcol < 0:
            while coluna < 0:
                coluna += c
                c += 1
            c -= 1
        
        coluna_s = coluna
        c_s = c
        while linha < shape_self[0] and l < shape_other[0]:
            coluna, c = (coluna_s, c_s)
            while coluna< shape_self[1] and c < shape_other[1]:
                if self.tipo == int:
                    self.data[linha, coluna] = int(other.data[l,c])
                elif self.tipo == float:
                    self.data[linha, coluna] = float(other.data[l, c])
                c += 1
                coluna += 1
            l += 1
            linha += 1
            
    
    
    def __add__(self, other):
        return NumPymagem(0, 0, self.data + other.data)
    
    def __mul__(self, num):
        return NumPymagem(0, 0, self.data * num)
    
    
    def pinte_retangulo(self, val, left, top, right , bottom):
        if left <0:
            left = 0
        if top <0:
            top = 0
        if right >self.data.shape[1]:
            right = self.data.shape[1]
        if bottom >self.data.shape[0]:
            bottom = self.data.shape[0]
        self.data[top: bottom, left: right] = val
        
    def pinte_disco(self, val, raio, clin, ccol):
        lin, col = self.shape()
        area = 3.1415*raio**2
        l = 0
        while l < lin:
            c = 0
            while c < col:
                area_c = 3.1415*((l-clin)**2 + (c-ccol)**2)
                if area_c < area:
                    self.data[l, c] = val
                c += 1
            l += 1
    
    
    
    
    
    
def imagem_nova(nlin, ncol, valor):
    l = []
    for i in range(nlin):
        m = []
        for j in range(ncol):
            m.append(valor)
        l.append(m)
    return l


def cria_imagem(data):
    imagem = str()
    for i in range(0,data.shape[0]):
        for j in range(0, data.shape[1]):
            imagem += str(data[i, j]) + ', '
        imagem += '\n'
    return imagem

def imagem_regiao(imagem, left, top, right, bottom):
    if bottom == 0:
        bottom = len(imagem)
    if right == 0:
        right = len(imagem[0])
    data = []
    for i in range(top, bottom): #3 - 0 acessando linhas
        complemento = []
        for j in range(left, right): #4 - 1 acessando colunas
            complemento.append(imagem[i][j])
        data_regiao.append(complemento)
    return(data_regiao)