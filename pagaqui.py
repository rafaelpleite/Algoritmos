# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome:Anderson Lima dos Santos
    NUSP:########

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
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        Minha colega Maria me explicou que eu devia utilizar a função int() 
        quando fazemos leitura de números inteiros.

        No fórum escreveram para usar a função ...

        A minha solução foi baseada na descrição encontrada na 
        página https://stackoverflow.com/questions/15976333/

    Descrição de ajuda ou indicação de fonte:
'''
import numpy as np

#------------------------------------------------------------
class Paguime:
    ''' Recebe um array com pares (fcoin, quantidade) indicando
        o tipo e quantidade disponíveis de cada fcoin e atende os 
        pagamentos quando possível.
    '''
    def __init__(self, array):
        self.caixa = array
        self.size = array.size
        self.data = array.data   
        self.shape = array.shape
    def __str__(self):
        array = self.caixa
        nlin,ncol = self.shape
        s = ''
        n = 0
        print("O saldo do caixa é: \n")
        while n < nlin:
            s += f'{array[n,1]} fcoins de {array[n,0]} Frogs\n'
            n += 1
        return (s)
    
    def pague(self,valor):
        copia = np.copy(self.caixa)
        copia[:,1] = 0
        if valor == 0:
            return copia
        gasto = pagueR(copia,self.caixa,valor)
        return gasto


def pagueR(copia, caixa, valor):
    nlin, ncol = caixa.shape
    #caso base
    if valor == 0:
        return
    #daqui para baixo o intuito é apenas mudar a cópia-------------------------
    if valor <= copia[0,0]:
        n = 0
        while n < nlin:
            if caixa[n,0] == valor and caixa[n,1] > 0:
                copia[n,1] += 1
                caixa[n,1] -= 1
                return copia
            n += 1
        n = 0
        while n < nlin:
            if caixa[n,0] < valor and caixa[n,1] > 0:
                copia[n,1] += 1
                caixa[n,1] -= 1
                v = valor - copia[n,0]
                pagueR(copia,caixa,v)
                return copia
            n += 1
    if valor > copia[0,0]:
        n = 0 
        while n < nlin:
            if caixa[n,1] > 0:
                copia[n,1] += 1
                caixa[n,1] -= 1
                v = valor - copia[n,0]
                pagueR(copia,caixa,v)
                return copia
            n += 1
    return copia
    