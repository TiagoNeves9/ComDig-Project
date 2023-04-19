import numpy as np

def symbCreation(N, M):
    
    # Normalização da FMP
    #total_prob = sum(M)
    #fmp_norm = [p/total_prob for p in M]

    # Criar um ficheiro com N símbolos, de acordo com a FMP definida
    symbols = np.random.choice(list(M.keys()), size=N, p=list(M.values()))

    # Guardar os símbolos num ficheiro
    with open('symbols.txt', 'w') as f:
        f.write(' '.join(str(s) for s in symbols))

z = {'a':0.3,'b':0.2,'c':0.1,'d':0.15,'e':0.05,'f':0.1,'g':0.1}

x = symbCreation(32,z)
print("File created")       