# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Anderson Lima dos Santos
    NUSP: 11224341

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

class NumPymagema:
    
    def __init__(self, nlin, ncol, val=0):
        self.type = type(val)
        
        if self.type in [list]:
            array  = np.array(val)
            self.array = array
            self.shape = array.shape
            self.data = array.data
            self.size = array.size
            self.tipo = type(self.size)
            
        if self.type in [int, float]:
            array = np.full((nlin,ncol), val)
            self.array = array
            self.shape = array.shape
            self.size = array.size
            self.data = array.data
            self.tipo = type(self.size)

        if self.type not in [list,int,float]:
            self.array = val
            self.shape = val.shape   # dimensão da matriza
            self.data = val.data     #lista com os elementos
            self.size = val.size    #valor inteiro
            self.tipo = type(self.size)
        print(self.tipo)
#--------------------------------------------------------------------------------
    #o programa de impreção funciona com shapes dado o numero, mas não com shape de array
    def __str__(self):
        data = self.data
        nlin, ncol = self.shape
        s =''
        lin = 0
        while lin < nlin:
            col = 0
            while col < ncol:
                s += f'{data[lin,col]} '
                col += 1
            s += '\n'
            lin += 1
        return s
    
    
#--------------------------------------------------------------------------------    
    def __getitem__(self, chave):
        nlin, ncol = self.shape
        lin, col = chave
        valor = self.array[lin,col]
        
        return valor

#--------------------------------------------------------------------------------    
    def __setitem__(self, chave, valor):
        nlin, ncol = self.shape
        lin, col = chave
        if self.tipo in [int]:
            self.array[lin,col] = int(valor)
            
        if self.tipo in [float]:
            self.array[lin,col] = float(valor)
            
    
    
#--------------------------------------------------------------------------------
    def __add__(self, other):
        if type(other) in [int,float]:
            array = self.array + other
        else:
            array = self.array + other.array
        
        return NumPymagem(0,0,array)
    
    def __radd__(self,other):
        return self + other

#--------------------------------------------------------------------------------
    def __mul__(self, other):
        if type(other) in [int, float]:
            array = self.array * other
        else:
            array = self.array * other.array
        
        return NumPymagem(0,0,array)
        
    def __rmul__ (self, other):
        return self * other
    
#--------------------------------------------------------------------------------

    def crop (self,left = 0,top = 0,right = 0 ,bottom = 0):
        '(left,top,right,bottom) -> nova numpyimagem'
        esquerda, topo, direita, baixo = (left, top, right, bottom)
        
        if  (esquerda, topo, direita, baixo) == (0, 0, 0, 0):
            esquerda = 0
            topo = 0
            direita = (self.shape[1])
            baixo = (self.shape[0])
            
        novo_elemento = []
        linha = topo
        while linha < baixo:
            coluna = esquerda
            l = []
            while  coluna < direita:
                elemento = self.data[linha,coluna]
                l.append(elemento)
                coluna += 1
            novo_elemento.append(l)
            linha += 1
        return NumPymagem(0, 0, novo_elemento)


#--------------------------------------------------------------------------------
    def paste (self,img, tlin, tcol):
        shape_1 = self.shape
        shape_2 = img.shape
        i, c = (0,0)
        if tlin < 0:
            linha = tlin
            while linha < 0:
                linha = linha + i
                i += 1
            i = i - 1
        else:
            linha =tlin
        
        if tcol < 0:
            coluna = tcol
            while coluna < 0:
                coluna= coluna+ c
                c += 1
            c = c - 1
        else:
            coluna = tcol
        
        coluna_salva = coluna
        c_salva = c
        while linha < shape_1[0] and i < shape_2[0]:
            coluna, c = (coluna_salva, c_salva)                   
            while coluna< shape_1[1] and c < shape_2[1]:
                if self.tipo in [int]:
                    self.array[linha,coluna] =int(img.array[i,c])
                if self.tipo in [float]:
                    self.array[linha,coluna] =float(img.array[i,c])
                
                c += 1
                coluna += 1
            i += 1
            linha+= 1
            
#--------------------------------------------------------------------------------
    def pinte_disco(self, val, raio, clin, ccol):
        lin, col = self.shape
        Area = 3.1415*(raio**2)
        l = 0
        while l < lin:
            c = 0
            while c < col:
                r = ((l-clin)**2 + (c-ccol)**2)**(1/2)
                Area_compara = 3.1415*(r**2)
                if Area_compara < Area:
                    self.array[l, c] = val
                c += 1
            l += 1
    
#--------------------------------------------------------------------------------
    def pinte_retangulo(self,val, left = 0,top = 0,right = 0 ,bottom = 0):
        '(left,top,right,bottom) -> nova numpyimagem'
        
        esquerda, topo, direita, baixo = (left, top, right, bottom)
        lin , col = self.shape
        
        if esquerda < 0:
            while esquerda < 0:
                esquerda += 1
        if topo < 0:
            while topo < 0:
                topo += 1
        if direita > col:
            direita = col
        
        if baixo > lin:
            baixo = lin
        linha = topo
        coluna = esquerda
        self.array[linha:baixo,coluna:direita] = val
