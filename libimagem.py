#!/usr/bin/env python
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
    Tudo que foi utilizando para a realização deste EP faz parte do conhecimento 
    adquirido nas aulas de MAC122 e MAC115 (oferecida para os alunos de bach em 
    física no 2 sem de 2019).
    O monitor Raphael me ajudou na função imagem_carrega(dest, orig). Estava
    estava com erro, pois eu tinha colocado para retornar uma clone, quando
    na verdade, deveria retornar uma cópia. Obrigado pela ajudar, Raphael!

'''

#--------------------------------------------------------------------------        
def imagem_nova(nlin, ncol, valor):
    ''' (int, int, obj) -> list

    Recebe dois inteiros nlin e ncol e um valor. 
    Cria e retorna uma imagem de dimensão nlin x ncol com valor em cada 
    posição.

    Exemplos:
    >>> t = imagem_nova(3,4,-1)
    >>> t
    [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
    >>> tt = imagem_nova(3,3,0)
    >>> tt
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> 
    '''
    l = []
    for i in range(nlin):
        m = []
        for j in range(ncol):
            m.append(valor)
        l.append(m)
    #print("imagem_nova(): Vixe! Essa função ainda não foi feita.")
    return l

#--------------------------------------------------------------------------        
def imagem_carrega(dest, orig):
    ''' (list, list) -> None

    Recebe duas imagens de mesma dimensão e carrega o conteúdo de orig 
    na imagem dest.

    Exemplo:

    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = [[11, 22, 33],[44, 55, 66]]
    >>> imagem_carrega(tt, t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 777
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[777, -122, 3], [1, 2, 3]]
    '''
    for i in range(len(orig)):
        for j in range(len(orig[0])):
            dest[i][j] = orig[i][j]
    #print("imagem_carrega(): Vixe! Essa função ainda não foi feita.")

#--------------------------------------------------------------------------        
def imagem_clone(imagem):
    ''' (list) -> list

    Recebe uma imagem e retorna um clone da imagem.

    Exemplo:
    >>> t = [[12, -122, 3],[1, 2, 3]]
    >>> tt = imagem_clone(t)
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[12, -122, 3], [1, 2, 3]]
    >>> tt[0][0] = 111111
    >>> t
    [[12, -122, 3], [1, 2, 3]]
    >>> tt
    [[111111, -122, 3], [1, 2, 3]]
    >>> 
    '''
    clone = []
    for i in range(len(imagem)):
        l = []
        for j in range(len(imagem[0])):
            l.append(imagem[i][j])
        clone.append(l)
    #print("imagem_clone(): Vixe! Essa função ainda não foi feita.")
    return clone

#--------------------------------------------------------------------------        
def imagem_regiao(imagem, left, top, right, bottom):
    ''' (list, int, int, int, int) -> list

    Recebe uma imagem e 4 valores que definem um região retangular onde:
    top define a primeira linha, bottom define a última linha,  
    left define a primeira coluna, e right define a última coluna da região.
    A função cria e retorna uma imagem de dimensão
    (bottom - top) linhas por (right-left) colunas, 
    com conteúdo igual à região correspondente na imagem. 
    Observe que os pontos na linha bottom e coluna right NÃO 
    fazem parte da região retangular.
    
    Exemplo:
    >>> imagem_regiao([[1, 2, 3, 4, 5], 
                       [2, 3, 4, 5, 6], 
                       [3, 4, 5, 6, 7], 
                       [4, 5, 6, 7, 8] ], 1, 0, 4, 3)
    [[2,3,4], [3,4,5], [4, 5, 6]]
    
    >>> imagem_regiao([[1, 2, 3, 4, 5], 
                       [6, 7, 8, 9, 0], 
                       [0, 9, 8, 7, 6], 
                       [1, 2, 3, 4, 5] ], 1, 2, 3, 4)
    [[9,8], [2,3]]
    '''
    matriz_regiao = []
    for i in range(top, bottom): #3 - 0 acessando linhas
        complemento = []
        for j in range(left, right): #4 - 1 acessando colunas
            complemento.append(imagem[i][j])
        matriz_regiao.append(complemento)
    #print("imagem_regiao(): Vixe! Essa função ainda não foi feita.")
    return(matriz_regiao)


