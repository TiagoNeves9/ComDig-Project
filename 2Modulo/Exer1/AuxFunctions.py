import random as rand


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
    print("BER obtida: %f , BER original: %f" % (ber, BER))
    return output
