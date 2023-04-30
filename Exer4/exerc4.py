# 4. Considere a cifra de Vernam para ficheiros de texto.
#   Esta cifra realiza o XOR bit a bit de todos os caracteres
#   de duas sequências, plainText e theKey, resultando ainda uma sequência de caracteres, cipherText.

# a) Implemente a função cypherText = makeVernamCypher(plainText, theKey), sendo os parâmetros de entrada
#   e o valor de retorno, sequências de caracteres com a dimensão do texto em claro (plainText). Demonstre o (bom)
#   funcionamento fazendo a cifra e a decifra da sequência abcabcd, considerando a chave constante e igual a 3333333.

import numpy as np
import Exer2.exerc2 as exerc2


def makeVernamCypher(plainText, theKey):
    cypherText = ""
    with open(plainText, 'r') as f:
        data = f.read()
    p = 0
    keyStr = str(theKey)

    # if len(data) > len(key):
    # return f"Key given({theKey}) is not enough to cypher the text given({plainText})!"

    for char in data:
        cypherText += chr(ord(char) ^ ord(keyStr[p]))
        p += 1
        if p == len(keyStr):
            p = 0
    return cypherText


#   alinea b - chave ser maior ou igual a plain text em termos de tamanho -> garantir isto

# b)  Realize a cifra do ficheiro alice29.txt (texto em claro) com a chave constante e com chave correspondendo a uma
# sequência aleatória de caracteres. Para ambas as situações determine os histogramas e entropias do texto em claro e
# do texto cifrado. Compare os resultados e comente.

def cypherKeyMaker(file, const=False):
    with open(file, 'r') as f:
        data = f.read()

    filesize = len(data)
    if not const:
        key = np.random.randint(0, 9, filesize, int)
    else:
        key = np.random.random_integers(3, 3, filesize)

    return key
# ^^^ nao esta a ser utilizada


def cypherBigText(file):
    # constKey = cypherKeyMaker(file, True)
    # randomKey = cypherKeyMaker(file)

    constKey = 33333333
    randomKey = "asdwQaks"

    constCypherFile = makeVernamCypher(file, constKey)
    randomCypherFile = makeVernamCypher(file, randomKey)

    with open('constFile.txt', 'w', encoding='utf-8') as cw:
        cw.write(''.join(c for c in constCypherFile))
        cw.close()

    with open('randomFile.txt', 'w', encoding='utf-8') as rw:
        rw.write(''.join(r for r in randomCypherFile))
        rw.close()

    exerc2.histMaker('constFile.txt')
    exerc2.histMaker('randomFile.txt')


cypherBigText('../TestFilesCD/alice29.txt')
