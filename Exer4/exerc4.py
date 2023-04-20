# 4. Considere a cifra de Vernam para ficheiros de texto.
#   Esta cifra realiza o XOR bit a bit de todos os caracteres
#   de duas sequências, plainText e theKey, resultando ainda uma sequência de caracteres, cipherText.

# a) Implemente a função cypherText = makeVernamCypher(plainText, theKey), sendo os parâmetros de entrada
#   e o valor de retorno, sequências de caracteres com a dimensão do texto em claro (plainText). Demonstre o (bom)
#   funcionamento fazendo a cifra e a decifra da sequência abcabcd, considerando a chave constante e igual a 3333333.


def makeVernamCypher(plainText, theKey):
    cyperText = ""
    p = 0

    key = str(theKey)

    with open(plainText, 'r') as f:
        data = f.read()

    for char in data:
        cyperText += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p == len(key):
            p = 0

    return cyperText


x = makeVernamCypher('cypher.txt', 3333333)
print(x)


#   alinea b - chave ser maior ou igual a plain text em termos de tamanho -> garantir isto

