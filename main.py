#Domača naloga Urejanje binarnih datotek - Sabina Paurič
import sys

def read_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, "wb") as file:
        file.write(data)

def find_bit_sequence(data, search_string):
    searching_string_length = len(search_string) #bit
    indices = []
    pos = 0
    data_bits = ''.join(f"{byte:08b}" for byte in data) #byte to bit
    print(data_bits)

    while pos <= len(data_bits) - searching_string_length:
        if data_bits[pos:pos + searching_string_length] == search_string:
            indices.append(pos)
            pos += searching_string_length
        else:
            pos += 1

    return indices

def replace_bit_sequence(data, old_search_string, new_search_string):
    data_bits = ''.join(f"{byte:08b}" for byte in data)
    print(data_bits)

    new_data_bits = data_bits.replace(old_search_string, new_search_string)

    while len(new_data_bits) % 8 != 0:
        new_data_bits += '0'
    new_data = int(new_data_bits, 2).to_bytes(len(new_data_bits) // 8, byteorder="big")

    return new_data


def main():
    if len(sys.argv) < 4:
        print("Uporaba:")
        print("Za iskanje: dn1 <ime_datoteke> f <iskani_bitni_niz>")
        print("Za iskanje in zamenjavo: dn1 <ime_datoteke> fr <iskani_bitni_niz> <nov_bitni_niz>")
        return

    file_path = sys.argv[2]
    print(file_path)
    mode = sys.argv[3]
    data = read_file(file_path)

    if mode == "f":
        search_string = sys.argv[4]
        positions = find_bit_sequence(data, search_string)
        print("Iskalni niz", search_string)
        print("Izpis indeksov pojavitve (pozicije):", positions)
    elif mode == "fr":
        old_search_string = sys.argv[4]
        new_search_string = sys.argv[5]
        new_data = replace_bit_sequence(data, old_search_string, new_search_string)
        output_path = "output_" + file_path
        write_file(output_path, new_data)
        print(f"Zamenjava končana. Nova datoteka je shranjena kot: {output_path}")
    else:
        print("Neveljaven način! Uporabite 'f' za iskanje ali 'fr' za iskanje in zamenjavo.")

if __name__ == '__main__':
    main()
