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
    monitores e colegas). Com exceção de material de MAC0122, caso
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
# MarkovModel(), MarkovModel.laplace(), __str__()
from markov_model import MarkovModel

# math.log()
import math

class TopModel:
    def __init__(self, k, dict_corpora):
        self.k, self.dict_corpora, self.markov = k, dict_corpora, dict()
        for i in dict_corpora: self.markov[i] = MarkovModel(k, dict_corpora[i])
            
    def __str__(self):
        t = f'TopModel possui {len(self.dict_corpora)} modelos: '
        for i in self.dict_corpora: t += str(i)
        for j in self.dict_corpora: t += f'\nModelo {j}:\nalfabeto tem {self.markov[j]}\n'
        return t
    
    def modelo(self, string):
        if string in self.dict_corpora: return self.markov[string]
        print(f"modelo '{string}' não foi definido")
        return None
    
    def verossimilhanca_total(self, string, citacao):
        if string in self.dict_corpora:
            citacao_n, p = citacao + citacao[0:self.k], .0
            for i in range(len(citacao)): p+= math.log(self.markov[string].laplace(citacao_n[i: i+self.k+1]))
            return p
        print(f'modelo {string} não foi definido')
        return None
    
    def media_verossimilhanca(self, string, citacao):
        if type(self.verossimilhanca_total(string, citacao)) == float: return self.verossimilhanca_total(string, citacao) / len(citacao)
        self.verossimilhanca_total(string, citacao)
        
    def top_model(self, citacao):
        d = dict()
        for i in self.dict_corpora: d[i] = self.media_verossimilhanca(i, citacao)
        return max(d, key=d.get), d[max(d, key=d.get)]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

