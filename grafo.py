# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
# NÃO INCLUA NENHUM OUTRO import ...
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

#-----------------------------------------------------------------
class Grafo:
    '''
        Siga as especificações do enunciado para construir a classe Grafo.

        Coloque o seu código a seguir.
    '''
    def __init__(self, text='', sep=' '):
        self.dict = dict()
        if text != '' and text != None:
            with open(text, encoding="utf8", errors='ignore') as f:
                lines = f.readlines()
                for i in lines:
                    i = i.split(sep)
                    i[len(i)-1] = i[len(i)-1].strip('\n')
                    self.dict[i[0]] = i[1:]
                    for j in i[1:]:
                        self.insira_aresta(i[0], j)
        for p in self.dict:
            self.dict[p].sort()
        
    def __str__(self):
        s = ''
        for i in sorted(self.dict):
            self.dict[i].sort()
            s += i + ' | '
            for j, jval in enumerate(self.dict[i]):
                if j != len(self.dict[i]) - 1: s += jval + ', '
                else: s += jval 
            s += '\n'
        return s
    
    def insira_aresta(self, v, w):
        if v == '' or w == '': return None
        v, w = v.strip(), w.strip()
        if v not in self.dict: self.dict[v] = [w]
        else: self.dict[v] = list(set(self.dict[v] + [w]))
        if w not in self.dict: self.dict[w] = [v]
        else: self.dict[w] = list(set(self.dict[w] + [v]))
        self.dict[v].sort
        self.dict[w].sort
            
    def tem_vertice(self, v):
        return v in self.dict
        
    def V(self):
        return len(self.dict)
    
    def A(self):
        l = []
        for i in sorted(self.dict):
            for j in self.dict[i]:
                if sorted([i, j]) not in l:
                    l.append(sorted([i,j]))
        return len(l)
        
    def vertices(self):
        return sorted(list(self.dict.keys()))
    
    def adjacentes(self, v):
        return self.dict[v]
    
    def grau(self, v):
        return None
    
    def tem_aresta(self, u, v):
        if v not in self.dict: return False
        return u in self.dict[v]
