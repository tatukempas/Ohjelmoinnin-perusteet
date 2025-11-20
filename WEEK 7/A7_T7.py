ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def load_config(file):
    rotors, reflector = [], ""
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("Rotor"):
                    rotors.append(line.split(":")[1].strip())
                elif line.startswith("Reflector"):
                    reflector = line.split(":")[1].strip()
    except FileNotFoundError:
        print(f"Config file '{file}' not found. Using default configuration.")
        rotors = [
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    return rotors, reflector

def rotate(rotor_pos):
    rotor_pos[0] = (rotor_pos[0] + 1) % 26
    if rotor_pos[0] == 0:
        rotor_pos[1] = (rotor_pos[1] + 1) % 26
        if rotor_pos[1] == 0:
            rotor_pos[2] = (rotor_pos[2] + 1) % 26
    return rotor_pos

def encode_char(c, rotors, pos, reflector):
    idx = ALPHABET.index(c)
    for i in range(3):
        rotor = rotors[i]
        p = pos[i]
        idx = (rotor.index(ALPHABET[(idx+p)%26]) - p + 26) % 26
    idx = ALPHABET.index(reflector[idx])
    for i in reversed(range(3)):
        rotor = rotors[i]
        p = pos[i]
        idx = (rotor[(idx+p)%26])
        idx = (ALPHABET.index(idx) - p + 26) % 26
    return ALPHABET[idx]

def encode_line(line, rotor_pos, rotors, reflector):
    encoded = ""
    pos = rotor_pos.copy()
    for char in line.upper():
        if char not in ALPHABET:
            encoded += char
            continue
        pos = rotate(pos)
        encoded += encode_char(char, rotors, pos, reflector)
    return encoded

def main():
    cfg_file = input("Insert config(filename): ").strip()
    rotors, reflector = load_config(cfg_file)
    init_pos = [0,0,0]

    plugs = input("Insert plugs (y/n)?: ").strip().lower()
    if plugs == "y":
        print("Plugboard not implemented. Continuing without it.")
    else:
        print("No plugs inserted.")
    print("Enigma initialized.\n")

    while True:
        line = input("Insert row (empty stops): ").upper()
        if not line:
            print("\nEnigma closing.")
            break
        rotor_pos = init_pos.copy()
        converted = encode_line(line, rotor_pos, rotors, reflector)
        print()
        for orig, enc in zip(line, converted):
            print(f'Character "{orig}" illuminated as "{enc}"')
        print(f'Converted row - "{converted}".\n')

if __name__ == "__main__":
    main()
