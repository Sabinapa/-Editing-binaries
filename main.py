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

def replace_bit_sequence(data, old_bit_sequence, new_bit_sequence):
    data_bits = ''.join(f"{byte:08b}" for byte in data)

    old_length = len(old_bit_sequence)
    new_length = len(new_bit_sequence)

    new_data_bits = data_bits.replace(old_bit_sequence, new_bit_sequence)

    while len(new_data_bits) % 8 != 0:
        new_data_bits += '0'
    new_data = int(new_data_bits, 2).to_bytes(len(new_data_bits) // 8, byteorder="big")

    return new_data


def main():
    mode = input("Vnesite način (f za iskanje, fr za iskanje in zamenjavo): ").strip()
    file_path = input("Vnesite ime binarne datoteke: ").strip()
    data = read_binary_file(file_path)

    if mode == "f":
        bit_sequence = input("Vnesite zaporedje bitov za iskanje: ").strip()
        positions = find_bit_sequence(data, bit_sequence)
        print("Pozicije pojavitve niza bitov:", positions)
    elif mode == "fr":
        old_bit_sequence = input("Vnesite zaporedje bitov za iskanje: ").strip()
        new_bit_sequence = input("Vnesite novo zaporedje bitov za zamenjavo: ").strip()
        new_data = replace_bit_sequence(data, old_bit_sequence, new_bit_sequence)
        output_path = input("Vnesite ime izhodne datoteke: ").strip()
        write_binary_file(output_path, new_data)
        print("Zamenjava končana in nova datoteka je shranjena kot:", output_path)
    else:
        print("Neveljaven način. Uporabite 'f' za iskanje ali 'fr' za iskanje in zamenjavo.")


if __name__ == '__main__':
    main()
