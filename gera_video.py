# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Rafael Prudencio Leite
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

'''
import numpy as np
from numpymagem import NumPymagem
from numpymutil import mostre_video
from numpymutil import salve_video

# Escreva aqui outras constantes que desejar
ALTURA  = 240
LARGURA = 320
BLACK = 0
WHITE = 255
############# SENOS
COMP = 330
X = np.linspace(0, LARGURA, COMP)
Y = (ALTURA/3)*np.sin(X/5) + ALTURA/2

############# SQUARE WAVE

def square(x):
    val = 0
    for i in range(1, 101):
        val += np.sin(x/8)/i
    return (4 / np.pi) * val

U = np.linspace(0, LARGURA, COMP)
V = (ALTURA/20)*square(U) + ALTURA/2


#-------------------------------------------------------------------------- 

def main():
    ''' (None) -> None
    Escreva o seu programa que cria o vídeo como descrito no enunciado.
    
    O código abaixo serve para ilustrar como usar a função mostre_video()
    que recebe uma lista com NumPymagens e as mostra em um vídeo na tela
    do seu computador usando PyGame. Por isso lembre-se de seguir as 
    instruções para instalar PyGame no seu computador.

    Remova ou altere o código para gerar o seu próprio vídeo. Não se esqueça
    de criar funções para facilitar o entendimento do seu vídeo.

    Você pode (mas não precisa!) salvar o seu vídeo em um formato mp4, para
    mostrar sua obra no fórum da disciplina. Para isso, antes de salvar, 
    você deve instalar o software ffmpeg que você pode baixar de 
    https://ffmpeg.org/download.html. 
    '''
    #-----------------------------------------------------------------------
    # CRIE A SEGUIR O SEU VÍDEO
    
    video = []
    preto = NumPymagem(ALTURA, LARGURA, BLACK)    
    branco = NumPymagem(ALTURA, LARGURA, WHITE)
    print(f"Está compatível com numpymutil: {type(preto.data) is np.ndarray}")
    cor = BLACK

    for i in range(60): # gera 2s de fundo preto
        video.append(preto)
    for i in range(60): # muda fundo para branco, gradualmente
        cor = (cor+3)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        video.append(cinza)
    for i in range(60): # mostra 2s de fundo branco
        video.append(branco)
    for i in range(60): # volta para preto
        cor = (cor-3)%WHITE
        cinza = NumPymagem(ALTURA, LARGURA, cor)
        video.append(cinza)

    for i in range(COMP):
        inicio = NumPymagem(ALTURA , LARGURA, BLACK)
        inicio.pinte_disco(255, 1, int(Y[i]), int(X[i]))
        if i < COMP-2:
            inicio.pinte_disco(255/1.5, 1, int(Y[i+1]), int(X[i+1]))
            inicio.pinte_disco(255/2, 1, int(Y[i+2]), int(X[i+2]))
        video.append(inicio)

    for i in range(COMP):
        inicio = NumPymagem(ALTURA , LARGURA, BLACK)
        if i < COMP-2:
            inicio.pinte_disco(255/1.25, 2, int(V[i+1]), int(U[i+1]))
            inicio.pinte_disco(255/1.5, 2, int(V[i+2]), int(U[i+2]))
        inicio.pinte_disco(255, 2, int(V[i]), int(U[i]))
        video.append(inicio)
    print(len((video)))
        
    
    #-----------------------------------------------------------------------        
    # A CRIAÇÃO DO SEU VÏDEO TERMINA AQUI

    #------------------------------------------------------------------
    # selecione `True` ou `False` para as variáveis `mostre` e `salve`
    # para mostrar o vídeo mostre deve ser True, em caso contrário False    
    mostre = True # DEVE SER True no momento da entrega do EP
    # para gravar o vídeo salve deve ser True, em caso contrário False
    salve = False 

    #------------------------------------------------------------------
    # deste ponto em diante, nada deve ser alterado
    if mostre:
        mostre_video(video)
        
    if salve:
        print("Salvando vídeo")
        salve_video(video)
#-------------------------------------------------------------------------- 
#
# ESCREVA OUTRAS FUNÇÕES E CLASSES QUE DESEJAR

#-------------------------------------------------------------------------- 


#-------------------------------------------------------------------------- 
if __name__ == '__main__':
    main()
