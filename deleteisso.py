import numpy as np
from paguime  import Paguime

def main():
    '''(None) -> None
    programa para testar a classe Paguime
    '''

    saldo = np.array( [[20,1],[9,2],[4,2],[2,5]] )
    v = 43
    maq = Paguime( saldo )
    print( maq )

    pag = maq.pague(v)
    if pag is None:
        print(f"Não consegui pagar {v}")
    else:
        print(f"Paguei {v} usando:")
        print( pag )
        print( maq )

main()