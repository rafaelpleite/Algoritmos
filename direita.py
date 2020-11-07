PAREDE = '+'
PEGADA = '*'
BECO   = 'b'
INICIO = 'I'

def main():
    
    # um corredor sem saidas
    corredor = [
        ['+','+','+','+','+','+','+','+','+','+','+'],
        ['+',' ',' ',' ',' ',' ',' ',' ',' ',' ','+'],
        ['+','+','+','+','+','+','+','+','+','+','+']
    ]
    corredor[1][2] = INICIO
    anda(corredor, 1, 2)
    print(to_string(corredor))
          
#---------------------------------------------------------------            
def anda(corredor, i, j):
    ''' (list, int, int) -> None
    RECEBE um `corredor` sem saídas e uma posição [i][j].
    RECURSIVAMENTE, anda para a direita marcando as posições em que 
    passa com PEGADA  e volta marcando as posições com BECO.

    NOTA: essa função altera `corredor`.
    '''
    print(f"posição = [{i}][{j}]")
    print(to_string(corredor))
    pause()   
    
    if corredor[i][j] == PAREDE:
        return 
    
    corredor[i][j] = PEGADA
    
    print('Vai para direita')
    anda(corredor, i, j+1)
    
    print('Voltando')
    corredor[i][j] = BECO
    print(to_string(corredor))
    pause()
    
#-----------------------------------------------------------
# COSMÉTICO: exibe o labirinto
#
#-----------------------------------------------------------            
def to_string(lab):
    '''(list) -> string 
    '''
    s = ''
    nlins = len(lab)
    ncols = len(lab[0])
    linha = "  " + "+---"*ncols + "+\n"
    regua = " "
    for j in range(ncols):
        regua += f"  {j:2}"
            
    s += regua + '\n'
    for i in range(nlins):
        s += linha
        s += f"{i:2}"
        for j in range(ncols):
            s += f"| {lab[i][j]} "
        s += '|\n'
    s += linha    
    return s

def pause():
    input("Tecle ENTER para continuar.")      
            
main()
