import random
import AuxFunctions as aux


arduino = aux.arduinoSetup()


# Função para calcular o Fletcher Checksum
def fletcher_checksum(data):
    sum1 = 0
    sum2 = 0

    for bit in data:
        # Converte cada bit em seu valor inteiro (0 ou 1)
        bit_value = int(bit)
        sum1 = (sum1 + bit_value) % 255
        sum2 = (sum2 + sum1) % 255

    return (sum2 << 8) | sum1


def introduce_error(data, first_idx, errors):
    if first_idx < 0 or first_idx >= len(data):
        return

    last_idx = first_idx + errors
    bits_list = list(data)
    for i in range(first_idx, last_idx):
        if bits_list[i] == '0':
            bits_list[i] = '1'
        else:
            bits_list[i] = '0'

    data = ''.join(bits_list)
    return data

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode().strip()
        bits = aux.string_para_binario(data)
        print()
        print(f"Dado recebido: {data}")
        print(f"Dados em binario: {bits} ")

        original_checksum = fletcher_checksum(bits)

        # Introduz um erro (inverte um bit aleatório)
        error_position = 3  # Define a posição do bit a ser invertido
        errors = random.randint(0, 5)
        bits_alterados = introduce_error(bits, error_position, errors)
        print(f"Dados apos introdução de erros: {bits_alterados}")

        new_checksum = fletcher_checksum(bits_alterados)

        error_detected = (original_checksum != new_checksum)

        print("Valor checksum original:", original_checksum)
        print("Valor checksum recebido:", new_checksum)
        print("Erro detectado:", "Sim" if error_detected else "Não")
