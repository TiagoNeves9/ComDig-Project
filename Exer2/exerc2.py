import collections
import math
from matplotlib import pyplot as plt


#  a)   Para todos os ficheiros do conjunto TestFilesCD.zip,
#       apresente o histograma, o valor da informação própria de cada
#       símbolo e o valor da entropia do ficheiro.


def entropyMaker(ent, info, p):
    ent += p * info
    return ent


def histMaker(file):
    bins_ = 100
    entropy = 0

    with open(file, 'r') as f:
        data = f.read()

    file_size = len(data)
    plot = []
    histogram = collections.Counter(data)

    for i in range(file_size):
        plot.append(data[i])

    for key in histogram:
        count = histogram.__getitem__(key)
        p = count / file_size
        info = -math.log2(p)
        print(f"Informação Própria: {info} para simbolo {key}")
        entropy = entropyMaker(entropy, info, p)

    print(f"Entropia: {entropy}")

    print(f"Numero de simbolos: {file_size}")

    plt.title("Histogram")
    plt.hist(plot, bins=bins_)
    plt.show()


#histMaker('texto.txt')


############################################################################

# b) Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt, os quais contêm listagens de palavras em
#    Língua Inglesa e Língua Portuguesa. Para cada Língua:
#           (i) Apresente uma estimativa da percentagem de ocorrência de cada símbolo (carater).
#           (ii) Apresente o valor da entropia de ambos os ficheiros.

def occPercent(file):
    entropy = 0
    with open(file, 'r') as f:
        data = f.read()

    file_size = len(data)
    histogram = collections.Counter(data)

    def checkSimbolo(key):
        if key == "\n":
            return r"\n"
        else:
            return key

    for k in histogram:
        counter = histogram.__getitem__(k)
        p = counter / file_size
        info = -math.log2(p)
        print(f"A estimativa de ocorrência do simbolo {checkSimbolo(k)} é {p * 100}%")
        entropy = entropyMaker(entropy, info, p)

    print(f"Entropia do ficheiro {file}: {entropy}")


#occPercent('../ListaPalavrasPT.txt')
