# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM import ...
#------------------------------------------------------------------

'''

    Nome: Rafael Prudêncio Leite
    NUSP: ******

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
    
    def __init__(self, arr):
        self.saldo = arr
        
    def __str__(self):
        saldo = str('O saldo a máquina é:\n')
        for i in self.saldo:
            saldo += str(i[1]) + ' fcoins de '+ str(i[0]) + ' Frogs\n'
        return saldo
    
    def pague(self,valor):
        copia = np.copy(self.saldo)
        copia[:,1] = 0
        if valor == 0:
            return copia
        if np.sum(self.saldo[:,0]*self.saldo[:,1]) < valor:
            return None
        gasto = recursiva(copia, self.saldo, valor)
        return gasto
    
    
    
def recursiva(copia, caixa, valor):
    if valor <= copia[0,0]:
        for i, val in enumerate(caixa[:,0]):
            if val == valor and caixa[i,1] > 0:
                copia[i,1] += 1 
                caixa[i,1] -= 1 
                return copia
            
        for i, val in enumerate(caixa[:,0]):
            if val < valor and caixa[i,1] > 0:
                copia[i,1] += 1 
                caixa[i,1] -= 1 
                v = valor - val
                recursiva(copia, caixa, v)
                return copia
    if valor > copia[0,0]:
        for i, val in enumerate(caixa[:,0]):
            if val > 0:
                copia[i,1] += 1
                caixa[i,1] -= 1 
                v = valor - val
                recursiva(copia, caixa, v)
                return copia
    return copia
    

        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
