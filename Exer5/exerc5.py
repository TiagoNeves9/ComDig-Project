import random as rand


# alinea a)
def binarySymmetricChannel(txFile, BER):
    with open(txFile, 'rb') as rb, open('rxFile.bin', 'wb') as wb:
        while True:
            byte = rb.read(1)  # leitura da sequencia binaria
            if not byte:  #
                break  #
            byte = byte[0]  # pointer para o primeiro valor do array
            for i in range(8):
                bit = (byte >> i) & 1  # bitwise right shift e bitwise AND com 1
                if rand.random() <= BER:  # caso o valor seja menor q o valor BER fornecido, o erro é corrigido
                    bit = 1 - bit
                byte ^= (bit << 1)  # bitwise XOR entre byte e o valor obtido na operação
                                    # bitwise shift left entre bit e 1
            wb.write(bytes([byte]))  # escrita no ficheiro de saida


binarySymmetricChannel('../Exer5/txFile.bin', 0.1)
