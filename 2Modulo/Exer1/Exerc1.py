# a) Sobre a implementação do Binary Symmetric Channel (BSC), apresentado na Figura 1 (a), considere os valores de
# probabilidade de erro de bit p pertencente {10^1; 10^2; 10^3; 10^4; 10^5}. Na transmissão de quatro ficheiros à sua escolha,
# usando o diagrama apresentado na Figura 1 (b), calcule os seguintes valores de BER:

import random as rand
import os
from AuxFunctions import binarySymmetricChannel, string_para_binario, escrever_tabela, binario_para_string, \
    count_diff_symb, calculateBER

resultados = []
diretoria = '2Modulo\\Exer1\\files'
# 'E:\\ISEL_inst\\4ºSemestre22-23\\CD\\CD-G09-2223\\2Modulo\\Exer1\\files'


# i) BER1, entre a entrada e a saída do BSC, sem controlo de erros;
def bscWOErrorsControl(file, BER):
    with open(file, 'r') as fr:
        data = fr.read()
    data2 = string_para_binario(data)

    bscData = binarySymmetricChannel(data2, BER)

    fileOut = binario_para_string(bscData)

    diff = count_diff_symb(data, fileOut)

    ber = calculateBER(string_para_binario(data2), string_para_binario(bscData))
    ber = round(ber, 6)
    resultado = (file.split("\\")[-1], ber, BER, len(data2), diff, "Sem Controlo")
    resultados.append(resultado)


# ii) BER2, após a aplicação de código de repetição (3; 1) sobre o BSC, em modo de correção;
def bscW3_1(file, BER):
    with open(file, 'r') as fr:
        data = fr.read()
    originalBinary = string_para_binario(data)
    channeledData = binarySymmetricChannel(originalBinary, BER)
    encrypted = repetitionCode31(channeledData)  # aplicação do codigo de repetição(3,1), após passagem pelo BSC
    decrypeted = detect_errors(encrypted)

    fileOut = binario_para_string(channeledData)

    diff = count_diff_symb(data, fileOut)

    ber = calculateBER(originalBinary, decrypeted)
    ber = round(ber, 6)
    resultado = (file.split("\\")[-1], ber, BER, len(originalBinary), diff, "Repetição(3,1)")
    resultados.append(resultado)



def repetitionCode31(data):
    codigo = ''
    for bit in data:
        if bit == '1':
            codigo += '111'
        else:
            codigo += '000'

    return codigo


def detect_errors(data):
    output = ""

    groups = [data[i:i + 3] for i in range(0, len(data), 3)]
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

# iii) BER3, após a aplicação de código de Hamming (7, 4) sobre o BSC, em modo de correção.
def bscWHamming(file, BER):
    with open(file, 'r') as fr:
        data = fr.read()

    originalBinary = string_para_binario(data)
    channeledData = binarySymmetricChannel(originalBinary, BER)
    encrypted = Hamming7_4(channeledData, BER)
    decrypted = detect_Hamming(encrypted)

    ber = calculateBER(originalBinary, decrypted)

    fileOut = binario_para_string(channeledData)

    diff = count_diff_symb(data, fileOut)

    ber = calculateBER(originalBinary, decrypted)
    ber = round(ber, 6)
    resultado = (file.split("\\")[-1], ber, BER, len(originalBinary), diff, "Hamming (7,4)")
    resultados.append(resultado)


def Hamming7_4(data, ber):
   
    output = ''
    groups = [data[i:i + 4] for i in range(0, len(data), 4)]

    for group in groups:
        group_bits = [int(bit) for bit in group]

        p1 = group_bits[1] ^ group_bits[2] ^ group_bits[3]
        p2 = group_bits[0] ^ group_bits[1] ^ group_bits[2]
        p3 = group_bits[0] ^ group_bits[2] ^ group_bits[3]

        output += group + str(p1) + str(p2) + str(p3)

    res = ''
    for bit in output:
        if rand.random() < ber:
            res += '0' if bit == '1' else '1'
        else:
            res += bit
    
    return res



def detect_Hamming(data):
    message = ""
    groups = [data[i:i + 7] for i in range(0, len(data), 7)]
    
    for group in groups:
        group_bits = [int(bit) for bit in group]

        s1 = group_bits[4] ^ group_bits[1] ^ group_bits[2] ^ group_bits[3]
        s2 = group_bits[5] ^ group_bits[0] ^ group_bits[1] ^ group_bits[2]
        s3 = group_bits[6] ^ group_bits[0] ^ group_bits[2] ^ group_bits[3]
        
        sindroma = str("{}{}{}").format(s1,s2,s3)

    
        message += decoder(sindroma, group)

    return message

def decoder(sindroma, palavra_codigo):

    tabela_sindromas = {
        '000': '0000000',
        '011': '1000000', 
        '110': '0100000',
        '101': '0010000',
        '111': '0001000', 
        '100': '0000100',
        '010': '0000010',
        '001': '0000001',
        }
    
    
    if sindroma == "000" :
        return palavra_codigo[0:4]

    else:
        padrao_erro = tabela_sindromas[sindroma]

        palavra_estimada = ""
        for bit1, bit2 in zip(padrao_erro,palavra_codigo):
    
            int1 = int(bit1)
            int2 = int(bit2)
            
           
            bit_result = int1 & int2
            
            palavra_estimada += str(bit_result)

        return palavra_estimada[0:4]

       


    





def main():
    berValues = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    for ficheiro in os.listdir(diretoria):
        path = os.path.join(diretoria, ficheiro)
        if os.path.isfile(path):
            for ber in berValues:
                # bscWOErrorsControl(path, ber)
                # bscW3_1(path, ber)
                bscWHamming(path, ber)
                
    escrever_tabela(resultados)




if __name__ == '__main__':
    main()
