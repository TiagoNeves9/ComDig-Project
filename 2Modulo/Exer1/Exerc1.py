# a) Sobre a implementação do Binary Symmetric Channel (BSC), apresentado na Figura 1 (a), considere os valores de
# probabilidade de erro de bit p pertencente {10^1; 10^2; 10^3; 10^4; 10^5}. Na transmissão de quatro ficheiros à sua escolha,
# usando o diagrama apresentado na Figura 1 (b), calcule os seguintes valores de BER:

import random as rand
from AuxFunctions import binarySymmetricChannel, string_para_binario


# i) BER1, entre a entrada e a saída do BSC, sem controlo de erros;
def bscWOErrorsControl(file, ber):
    with open(file, 'r') as fr:
        data = fr.read()
    data2 = string_para_binario(data)
    return binarySymmetricChannel(data2, ber)

    # a = bscWOErrorsControl('fileA.txt', 0.1)
    # b = bscWOErrorsControl('fileB.txt', 00.1)             #tirar de comentario para testar
    # c = bscWOErrorsControl('fileC.txt', 000.1)
    # d = bscWOErrorsControl('fileD.txt', 0000.1)
    # f = bscWOErrorsControl('fileA.txt', 00000.1)

    # print(f'BSC para BER = 10^1', a)
    # print(f'BSC para BER = 10^2', b)
    # print(f'BSC para BER = 10^3', c)
    # print(f'BSC para BER = 10^4', d)
    # print(f'BSC para BER = 10^5', f)

    # ii) BER2, após a aplicação de código de repetição (3; 1) sobre o BSC, em modo de correção;
 def  bscW3_1(file, ber):
    with open(file, 'r') as fr:
        data = fr.read()
    data2 = string_para_binario(data)
    data3 = binarySymmetricChannel(data2, ber)
    return repetitionCode31(data3, ber)



    # def bscWErrorControl(file, ber):


def repetitionCode31(data, ber):
    codigo = ''
    for bit in data:
        if bit == '1':
            codigo += '111'
        else:
            codigo += '000'

    output = ""
    for bit in codigo:
        if rand.random() < ber:  # Introduz erro aleatoriamente com base na taxa de erro de bit
            output += str(1 - int(bit))  # Inverte o bit
        else:
            output += bit

    print(output)

def detect_errors(data):
    output = ""

    groups = [data[i:i+3] for i in range(0, len(data), 3)]
    for group in groups:
        count_zero = group.count('0')
        count_one = group.count('1')

        if count_zero > count_one:
            bit = '0'
        elif count_one > count_zero:
            bit = '1'
        else:
            bit = group[0]

        output += bit
    return output


def detect_Hamming(data):
    output = ""
    groups = [data[i:i+7] for i in range(0,len(data), 7)]

    for group in groups:
        group_bits = [int(bit) for bit in group]

        p1 = group_bits[2] ^ group_bits[4] ^ group_bits[6]
        p2 = group_bits[2] ^ group_bits[5] ^ group_bits[6]
        p3 = group_bits[4] ^ group_bits[5] ^ group_bits[6]

        error_pos = p1*1 + p2*2 + p3*4
        if error_pos != 0:
            group_bits[error_pos -1] = 1 - group_bits[error_pos - 1]
        output += "".join(map(str, group_bits[2:]))
    return output
