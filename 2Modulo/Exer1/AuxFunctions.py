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

    #errors = 0
    #for i in range(len(dataBin)):
    #    if int(dataBin[i], 2) ^ int(outBin[i], 2):
    #        errors += 1
    #ber = errors / len(data)
    #print("BER obtida: %f , BER original: %f" % (ber, BER))
    return output

def count_diff_symb(str1, str2):
    count = 0
    for char1, char2 in zip(str1,str2):
        if char1 != char2:
            count +=1

    return count

def calculateBER(msg, decrypeted):
    errors = 0
    for i in range(len(msg)):
        if int(msg[i], 2) ^ int(decrypeted[i], 2):
            errors += 1
    ber = errors / len(msg)
    return ber



def escrever_tabela(resultados):
    print()
    print("**** TABELA DE RESULTADOS ****")
    print()
    # Cabeçalho da tabela
    print("| {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("Ficheiro", "BER Obtida", "BER Original", "nº bits no BSC", "nª simbolos diferentes" ,"Operação"))
    print("+{:-<12}+{:-<12}+{:-<12}+{:-<12}+{:-<12}+{:-<12}+".format("", "", "", "", "", ""))

    # Linhas de dados
    for ficheiro, ber1, ber2, dim, diff, func in resultados:
        print("| {:<10} | {:<10}: | {:<10} | {:<10} | {:<10} | {:<10} |".format(ficheiro, ber1, ber2, dim, diff, func))

    # Rodapé da tabela
    print("+{:-<12}+{:-<12}+{:-<12}+{:-<12}+{:-<12}+{:-<12}+".format("", "", "", "", "",""))