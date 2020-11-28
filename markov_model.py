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
        
    Usei uma função sort nativa do python: https://developers.google.com/edu/python/sorting#:~:text=Custom%20Sorting%20With%20key%3D,-For%20more%20complex&text=For%20example%20with%20a%20list,sorts%20with%20those%20proxy%20values.
    Usei uma função set nativa do python: https://docs.python.org/2/library/sets.html
'''

class MarkovModel:
    def __init__(self, k, frase):
        self.k = k
        self.frase = frase
        self.quantidade = len(set(frase)) #DOCUMENTAÇÃO DO SET: set() -> new empty set object set(iterable) -> new set object
        
        self.palavras = []
        frase_d = frase + frase[0: k+1]
        for n in range(k, k+2):
            for i in range(len(frase)):
                self.palavras.append(frase_d[i: n+i])
        self.palavras_u = sorted(sorted(list(set(self.palavras))), key=len)
        self.cache = [0]*len(self.palavras_u)
        
        for i, ival in enumerate(self.palavras):
            self.cache[self.palavras_u.index(ival)] += 1
                        
    def __str__(self):
        p = f'alfabeto tem {self.quantidade} símbolos\n'
        for i, ival in enumerate(self.palavras_u):
            p += str('"') + str(ival) + str('"') + ' ' + str(self.cache[i]) + '\n'
        return p
    
    def alphabet(self):
        alpha = str()
        for i in sorted(set(self.frase)):
            alpha+= i
        return alpha
    
    def N(self, v):
        if v in self.palavras_u: return int(self.cache[self.palavras_u.index(v)])
        else: return 0
        
    def laplace(self, v):
        if v[:-1] not in self.palavras_u:
            return 1 / self.quantidade
        n = self.cache[self.palavras_u.index(v[:-1])] #toma o index da string que está antes de v[-1]
        strd = self.frase + self.frase[0: len(v)-1]
        m = 0
        for i in range(len(strd) - self.k):
            if strd[i: i + self.k+1] == v:
                m += 1
        return (m + 1/2) / (n + self.quantidade/2)
        
        
        
        
        
        
        
        
        
        
        
        
        
