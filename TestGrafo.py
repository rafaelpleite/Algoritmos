from grafo import Grafo        

g0 = Grafo(None) # grafo vazio                
g1 = Grafo("grafo\grafo.txt") # carrega o grafo representado em grafo.txt      
g2 = g2 = Grafo("grafo\cast.G.txt","/")      

print(g0)
print(g1)
print(g2)


print('g0')
g0.insira_aresta('', 'x')                                                                              
print(g0)                                                                                              
g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/bib')                                               
g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/dcc')                                               
g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/mae')                                               
g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/map')                                               
g0.insira_aresta('www.ime.usp.br', 'www.ime.usp.br/mat')                                               
print(g0)                      



g1.insira_aresta('H','X') # vértices devem ser strings                
print(g1) 

g1.insira_aresta(' Z ',' X ') # espaços devem ser removidos
print(g1)            


print(g0.tem_vertice('www.ime.usp.br/mac'))
print(g0.tem_vertice('www.ime.usp.br/dcc'))
print(g1.tem_vertice('blá'))
print(g1.tem_vertice('Z'))
print(g2.tem_vertice('Chaplin, Charles'))
print(g2.tem_vertice('Streep, Meryl'))
print(g2.tem_vertice('Andrews, Julie (I)'))                


print(g0.V())
print(g1.V())
print(g2.V())
print('\n')
print(g0.A())
print(g1.A())
print(g2.A()) 
'''

print(g0.vertices())      
print(g1.vertices())
print(g2.vertices()[:5])

print('\n')
print(g0.adjacentes('www.ime.usp.br/dcc') )
print(g0.adjacentes('www.ime.usp.br') )
print(g1.adjacentes('A') )
print(g1.adjacentes('Z') )
print(g2.adjacentes('Chaplin, Charles'))
print(g2.adjacentes('Andrews, Julie (I)'))

print(g0.grau("www.ime.usp.br/dcc"))

print(g0.tem_aresta("www.ime.usp.br", "www.ime.usp.br/dcc"))
print(g0.tem_aresta("www.ime.usp.br/mae", "www.ime.usp.br/dcc"))
print(g1.tem_aresta("A","Z"))
print(g1.tem_aresta("A","B"))
print(g2.tem_aresta("Chaplin, Charles", "Great Dictator, The (1940)"))                                 
print(g2.tem_aresta("Sound of Music, The (1965)", "Andrews, Julie (I)"))                                 
print(g2.tem_aresta("Great Dictator, The (1940)", "Andrews, Julie (I)"))
'''
             