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

        A monitora me explicou que eu devia utilizar a função 
        split(), strip(), map() e filter() para leitura dos dados
        no arquivo.

    Descrição de ajuda ou indicação de fonte:

'''

class Cliente:
    '''
        Siga as especificações do enunciado para 
        construir a classe Cliente.

        Coloque o seu código a seguir.
    '''
    
    def __init__(self, nome): #str --> None
        self.nome = nome
        
    def get_nome(self): #None --> str
        return self.nome
    
    def put_classificacao(self, filmes): #list --> None
        self.filmes = filmes
        
    def get_classificacao(self): #None --> list
        return self.filmes[:]
    
    def __str__(self): #None --> str
        string = str(self.nome) + '\n'
        for i, j in enumerate(self.filmes):
            string += str(i) + ': ' + str(j) + '\n'
        return string
    
    def distancia(self, other): #Cliente --> int
        cliente1, cliente2 = [], []
        for i, j in enumerate(self.filmes):
            if j in other.filmes:
                cliente1.append(j)
        for i, j in enumerate(other.filmes):
            if j in self.filmes:
                cliente2.append(j)
        numcliente1, numcliente2 = [], [0]*len(cliente2)
        for i, j in enumerate(cliente1):
            numcliente1.append(i)
            for u, v in enumerate(cliente2):
                if j == v:
                    numcliente2[u] = i
        if len(numcliente1) <= 2:
            return None
        return sort(numcliente2)
        
    
def sort(numcliente2): #str --> int
    interacao = 0
    for i in range(len(numcliente2) - 1):
        for j in range(len(numcliente2)-1, i, -1):
            if numcliente2[j] < numcliente2[j-1]:
                interacao += 1
                numcliente2[j], numcliente2[j-1] = numcliente2[j-1], numcliente2[j]
    return interacao
    
    
    
    
    
    
    
    
    
    
    
    
    
    

