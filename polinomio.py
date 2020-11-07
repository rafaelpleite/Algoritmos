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
    monitores e colegas). Com exceção de material de MAC0110 e MAC0122, 
    caso você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na 
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

'''
class Polinomio:
    def __init__(self, coefs):
        C = coefs[:]
        for i in range(len(C) -1, 0, -1): #tira os maiores graus == 0
            if C[i] != 0:
                break
            else:
                C.pop(i)           
        self.coefs = C
        
    def coeficientes(self):
        return self.coefs[:]
    
    def __str__(self):
        C = self.coefs
        if C == [0]: #se for p(x) = 0
            return str(0)
        else:
            p = str()
            for i in range(len(C) - 1, 0, -1): #Percorre a lista do fim até o começo (Inverso)
                if C[i] > 0:
                    p += '+ ' + str(C[i]) + '*x^' + str(i) + ' '
                if C[i] < 0:
                    p += '- ' + str(-1 * C[i]) + '*x^' + str(i) + ' '
            if C[0] != 0:
                p += '+ ' + str(C[0])
            return p
    
    def grau(self):
        C = self.coefs
        for i in range(len(C) -1, 0, -1):
            if C[i] != 0:
                return i
        return 0
    
    def derive(self):
        C = self.coefs[1:]
        for i in range(len(C)):
            C[i] = C[i] * (1 + i)
        return Polinomio(C)
        
    def __call__(self, num):
        n = num
        C = self.coefs
        valor = C[0]
        for i in range(1, len(C)):
            valor += C[i] * (n ** i)
        return valor
    
    def __add__(self, other):
        C = self.coefs
        
        if type(other) == float or type(other) == int: #é número
            num = other
            E = C[:]
            E[0] = E[0] + num
            return Polinomio(E)
            
        else: #não é numero
            D = other.coefs
            if len(C) >= len(D):
                E = [0]*len(C)
                for i in range(len(D)):
                    E[i] = C[i] + D[i]
                for j in range(len(D), len(C)):
                    E[j] = C[j]
                return Polinomio(E)
            else: #len(D) > len(C)
                E = [0]*len(D)
                for i in range(len(C)):
                    E[i] = C[i] + D[i]
                for j in range(len(C), len(D)):
                    E[j] = D[j]
                return Polinomio(E)
            
    def __radd__(self, other):
        C = self.coefs
        if type(other) == float or type(other) == int: #é número
            num = other
            E = C[:]
            E[0] = E[0] + num
            return Polinomio(E)
            
        else: #não é numero
            D = other.coefs
            if len(C) >= len(D):
                E = [0]*len(C)
                for i in range(len(D)):
                    E[i] = C[i] + D[i]
                for j in range(len(D), len(C)):
                    E[j] = C[j]
                return Polinomio(E)
            else: #len(D) > len(C)
                E = [0]*len(D)
                for i in range(len(C)):
                    E[i] = C[i] + D[i]
                for j in range(len(C), len(D)):
                    E[j] = D[j]
                return Polinomio(E)
            
            
            
            
    def __sub__(self, other):
        C = self.coefs
        D = other.coefs
        if len(C) >= len(D):
            E = [0]*len(C)
            for i in range(len(C) - len(D)):
                print('val i ', i)
                print('valor', C[i])
                E[i] = C[i]
            #for j in range(len(C) - len(D), len(C)):
                #print('val j ', j)
                #E[j] = C[j]
            print(E)
            return Polinomio(E)
            
            
        else: #len(D) > len(C)
            E = [0]*len(D)
            for i in range(len(C)):
                E[i] = C[i] - D[i]
                for j in range(len(C), len(D)):
                    E[j] = - D[j]
                return Polinomio(E)
            
    def __mul__(self, other):
        C = self.coefs
        
        if type(other) == float or type(other) == int: #é número
            num = other
            E = C[:]
            for i in range(len(E)):
                E[i] = E[i] * num
            return Polinomio(E)
            
        else: #não é numero
            D = other.coefs
            E = [0]*(len(C) + len(D) - 1)
            for i in range(len(C)):
                for j in range(len(D)):
                    E[i + j] += C[i] * D[j]
            return Polinomio(E)
        
    def __rmul__(self, other):
        C = self.coefs
        
        if type(other) == float or type(other) == int: #é número
            num = other
            E = C[:]
            for i in range(len(E)):
                E[i] = E[i] * num
            return Polinomio(E)
            
        else: #não é numero
            D = other.coefs
            E = [0]*(len(C) + len(D) - 1)
            for i in range(len(C)):
                for j in range(len(D)):
                    E[i + j] += C[i] * D[j]
            return Polinomio(E)