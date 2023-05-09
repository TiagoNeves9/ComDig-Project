import random as rand
import math as math


def string_para_binario(string):
    binario = ''
    for caractere in string:
        valor_numerico = ord(caractere)
        binario += bin(valor_numerico)[2:].zfill(8)
    return binario
    # verificar estas funções


def binario_para_string(binario):
    caracteres = []
    for i in range(0, len(binario), 8):
        grupo = binario[i:i + 8]
        valor_numerico = int(grupo, 2)
        caractere = chr(valor_numerico)
        caracteres.append(caractere)
    return ''.join(caracteres)


# alinea a)
def binarySymmetricChannel(data, BER):
    output = ''
    for bit in data:
        if rand.random() < BER:
            output += '0' if bit == '1' else '1'
        else:
            output += bit

    dataBin = string_para_binario(data)
    outBin = string_para_binario(output)

    errors = 0
    for i in range(len(dataBin)):
        if int(dataBin[i], 2) ^ int(outBin[i], 2):
            errors += 1
    ber = errors / len(data)
    print('BER obtida:', ber)
    return output


# print(binarySymmetricChannel('01100101011110000110010101101101011100000110110001100101', 1))

# alinea b)

def interleaving(text):
    intLeavingText = ""

    size = len(text)
    raiz = math.sqrt(size)
    inteiro = math.trunc(raiz)
    dec = raiz - inteiro

    if raiz == inteiro:
        idxRow = inteiro
        idxCol = inteiro
    elif dec < 0.5:
        idxRow = inteiro
        idxCol = inteiro + 1
    else:
        idxRow = inteiro + 1
        idxCol = inteiro + 1

    for i in range(idxCol):
        idx = 0
        for j in range(idxRow):
            newIdx = idx * idxRow + i
            if newIdx >= size:
                intLeavingText += '0'
            else:
                intLeavingText += text[newIdx]
            idx += 1

    return intLeavingText


def deInterleaving(text):
    size = len(text)
    raiz = math.sqrt(size)
    inteiro = math.trunc(raiz)
    dec = raiz - inteiro

    if dec < 0.5:
        idxRow = inteiro
        idxCol = inteiro + 1
    else:
        idxRow = inteiro + 1
        idxCol = inteiro + 1

    deInterleaving = ""
    for i in range(idxRow):
        for j in range(idxCol):
            idx = j * idxRow + i
            if idx >= size or text[idx] == '0':
                continue
            deInterleaving += text[idx]

    return deInterleaving


def interleavingBSC(file, ber):
    with open(file, 'r') as rf:
        data = rf.read()  # obter o texto do ficheiro de entrada
        rf.close()

    print('(1) -> Dentro da função esta é a string:', data)

    posInterleaving = interleaving(data)  # processar em interleaving
    print('(2) -> Apos interleaving:', posInterleaving)
    interleavingBin = string_para_binario(posInterleaving)  # passar para binario
    print('(3) -> Interleaving em binario:', interleavingBin)

    bscBin = binarySymmetricChannel(interleavingBin, ber)  # processar no BSC
    print('(4) -> Apos o BSC:', bscBin)
    retString = binario_para_string(bscBin)
    print('(5) -> BSC em string:', retString)
    deInter = deInterleaving(retString)
    print('(6) -> Deinterleaving:', deInter)

    with open('rxFile.txt', 'w') as wf:
        wf.write(deInter)
        wf.close()


interleavingBSC('txFile.txt', 0.00001)

# print(interleaving("ExemploDeTransmissaoInterleaving"))
# print(deInterleaving("EonarnxDsolgeemIe0mTina0prstv0lasei0"))
# print(string_para_binario("python"))
# print(binario_para_string('011100000111100101110100011010000110111101101110'))

# print(binarySymmetricChannel("python", 0.0001, False))

