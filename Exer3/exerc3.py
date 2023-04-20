import numpy as np
import string


#################################################################################### Alinea a) e c) #########################################################################################

def symbCreation(N=None, M=None, word=False):
    ret = []
    if not word:
        # Criar N símbolos, de acordo com a FMP definida, de forma aleatoria 
        symbols = np.random.choice(list(M.keys()), size=N, p=list(M.values()))

        # Guardar os símbolos num ficheiro
        with open('symbols.txt', 'w') as f:
            f.write(' '.join(str(s) for s in symbols))
    else:

        for i in range(5):
            length = np.random.randint(8, 13)
            symbols = np.random.choice(list(M.keys()), size=length, p=list(M.values()))
            words = ''.join(symbols)
            ret.append(words)
        """for i in ret:
            with open('symbols.txt', 'a') as f:
                f.write(i)"""
        print(ret)


z = {'a': 0.3, 'b': 0.5, 'c': 0.1, 'd': 0.1}
n = 100

symbCreation(n, z)

###########################################################################################################################################################################################
