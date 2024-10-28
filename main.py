def read_binary_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def write_binary_file(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)


def find_bit_sequence(data, bit_sequence):
    byte_sequence = int(bit_sequence, 2).to_bytes((len(bit_sequence) + 7) // 8, byteorder="big")
    bit_sequence_length = len(bit_sequence)
    indices = []
    pos = 0
    data_bits = ''.join(f"{byte:08b}" for byte in data)

    while pos <= len(data_bits) - bit_sequence_length:
        if data_bits[pos:pos + bit_sequence_length] == bit_sequence:
            indices.append(pos)
            pos += bit_sequence_length
        else:
            pos += 1

    return indices


def main():
    mode = input("Vnesite način (f za iskanje, fr za iskanje in zamenjavo): ").strip()
    file_path = input("Vnesite ime binarne datoteke: ").strip()
    data = read_binary_file(file_path)

    if mode == "f":
        bit_sequence = input("Vnesite zaporedje bitov za iskanje: ").strip()
        positions = find_bit_sequence(data, bit_sequence)
        print("Pozicije pojavitve niza bitov:", positions)
    else:
        print("Neveljaven način. Uporabite 'f' za iskanje ali 'fr' za iskanje in zamenjavo.")


if __name__ == '__main__':
    main()
