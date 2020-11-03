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
import numpy as np

#-------------------------------------------------------------------------- 
# constantes
BLOCKED = 0  # sítio bloqueado
OPEN    = 1  # sítio aberto
FULL    = 2  # sítio cheio

class Fila:
    def __init__(self):
        self.itens = []
        
    def vazia(self):
        return self.itens == []
        
    def insere(self, item):
        self.itens.append(item)
        
    def remove(self):
        self.itens.pop[0]

class Percolation:
    '''
    Representa uma grade com todos os sítios inicialmente bloqueados.
    '''
    def __init__(self, entrada):
        self.perco = np.full((entrada, entrada), BLOCKED) if type(entrada) == int else np.full(entrada, BLOCKED)
        self.shape = self.perco.shape
        
    '''  
    def shape(self):
        return self.perco.shape
    '''
    
    def __str__(self):
        n_open = int(0)
        fig = str('\n') + str('+---')*self.perco.shape[1] + '+\n/ '
        for i in range(len(self.perco)):
            for j in range(len(self.perco[0])):
                if self.perco[i, j] == BLOCKED:
                    fig += '  / '
                elif self.perco[i, j] == OPEN:
                    fig += 'o / '
                    n_open += 1
                else:
                    fig += 'x / '
                    n_open += 1
            fig += str('\n') + str('+---')*self.perco.shape[1] + '+\n/ '
        return fig[:-2] + 'grade de dimensão: '+ str(self.perco.shape[0]) + 'x' + str(self.perco.shape[1]) + '\nNúmero de sítios abertos: ' + str(n_open)+'\npercolou: '+ str(perco(self))
        
    def is_open(self, int1, int2):
        if (int1, int2) >= (0,0) and len(self.perco) - int1 >= 0 and len(self.perco[0]) - int2 >= 0:
            if self.perco[int1, int2] == OPEN or self.perco[int1, int2] == FULL:
                return True
            else:
                return False
        else:
            print('Valor inserido invalido.')
            return None
        
        
    def is_full(self, int1, int2):
        if (int1, int2) >= (0,0) and len(self.perco) - int1 >= 0 and len(self.perco[0]) - int2 >= 0:
            if self.perco[int1, int2] == 2:
                return True
            else:
                return False
        else:
            print('Valor inserido invalido.')
            return None
        
    def no_open(self):
        n_int = 0
        for i in range(0, self.shape[0]):
            for j in range(0, self.shape[1]):
                if self.perco[i,j] == OPEN or self.perco[i, j] == FULL:
                    n_int += 1
        return n_int
    
    def get_grid(self):
        return np.copy(self.perco)
    
    def open(self, int1, int2):
        if (int1+1, int2+1) > self.shape or int1<0 or int2<0:
            print('A posição: [{},{}] está fora da grade.'.format(int1,int2))
            return None
        
        if self.perco[int1, int2] == BLOCKED:
            self.perco[int1, int2] = OPEN
            if int1 == 0:
                self.perco[int1, int2] = FULL
            look(self, [int1, int2])
            
    def __setitem__(self, instance, value):
        self.perco[instance] = value
        
    def percolates(self):
        return perco(self)


def perco(matrix):
    for i in range(matrix.shape[1]):
        if matrix.perco[matrix.shape[0]-1, i] == FULL:
            return True
    return False
        

def look(matrix, pos):
    q = []
    q.append(pos)
    p = []
    
    while not q == []:
        
        i = q.pop()[:]
        p.append(i)
        if i[0] + 2 <= matrix.shape[0] and matrix.is_open(i[0]+1, i[1]) == True:
            if matrix.is_full(i[0]+1, i[1]) == True:
                matrix[i[0], i[1]] = FULL
            if [i[0]+1, i[1]] not in p:
                q.append([i[0]+1, i[1]])
                p.append([i[0]+1, i[1]])
        
        if i[0] > 0 and matrix.is_open(i[0]-1, i[1]) == True:
            if matrix.is_full(i[0]-1, i[1]) == True:
                matrix[i[0], i[1]] = FULL
            if [i[0]-1, i[1]] not in p:
                q.append([i[0]-1, i[1]])
                p.append([i[0]-1, i[1]])
            
        if i[1] + 2 <= matrix.shape[1] and matrix.is_open(i[0], i[1]+1) == True:
            if matrix.is_full(i[0], i[1]+1) == True:
                matrix[i[0], i[1]] = FULL
            if [i[0], i[1]+1] not in p:
                q.append([i[0], i[1]+1])
                p.append([i[0], i[1]+1])
            
        if i[1] > 0 and matrix.is_open(i[0], i[1]-1) == True:
            if matrix.is_full(i[0], i[1]-1) == True:
                matrix[i[0], i[1]] = FULL
            if [i[0], i[1]-1] not in p:
                q.append([i[0], i[1]-1])
                p.append([i[0], i[1]-1])
            
            
        
                
        
    
    
          
'''   
def look(matrix, pos): #array, tuple
    if matrix.perco[pos[0], pos[1]] == OPEN:
        
        if pos[0] == 0:
            matrix[pos[0], pos[1]] = FULL
                
                
        if pos[0] > 0: #olha de baixo p/ cima
            if matrix.is_open(pos[0]-1, pos[1]) == True:
                if matrix.is_full(pos[0]-1, pos[1]) == True:
                    matrix[pos[0], pos[1]] = FULL
                look(matrix, (pos[0]-1, pos[1]))
    
        if pos[1] + 2 <= matrix.shape[1]: #olha da esq p/ dir
            if matrix.is_open(pos[0], pos[1]+1) == True:
                if matrix.is_full(pos[0], pos[1]+1) == True:
                    matrix[pos[0], pos[1]] = FULL #TEM UM ELSE: AQUI EM BAIXO???
                look(matrix, (pos[0], pos[1]+1))
                
        if pos[1] > 0: #olha da dir p/ esq
            if matrix.is_open(pos[0], pos[1]-1) == True:
                if matrix.is_full(pos[0], pos[1]-1) == True:
                    matrix[pos[0], pos[1]] = FULL
                look(matrix, (pos[0], pos[1]-1))
'''

    
    
    
    
    
    
    
    
    
    
    
    
    
