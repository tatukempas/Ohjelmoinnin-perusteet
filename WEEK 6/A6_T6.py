LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char: str, alphabet: str) -> str:
    index = alphabet.find(char)
    if index == -1:
        return char
    return alphabet[(index + 13) % 26]

def rot13(text: str) -> str:
    output_chars = []
    for ch in text:
        if ch in LOWER_ALPHABETS:
            output_chars.append(shiftCharacter(ch, LOWER_ALPHABETS))
        elif ch in UPPER_ALPHABETS:
            output_chars.append(shiftCharacter(ch, UPPER_ALPHABETS))
        else:
            output_chars.append(ch)
    return "".join(output_chars)

def writeFile(filename: str, content: str) -> None:
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(content)

def collectWords() -> list[str]:
    lines = []
    while True:
        row = input("Insert row(empty stops): ").strip()
        if row == "":
            break
        lines.append(row)
    return lines

def main() -> None:
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    rows = collectWords()
    plain_text = "\n".join(rows)
    if rows:
        plain_text += "\n"
    print("\n#### Ciphered text ####")
    coded_text = rot13(plain_text)
    print(coded_text, end="")
    print("#### Ciphered text ####\n")
    file_name = input("Insert filename to save: ").strip()
    if not file_name:
        print("Filename not defined.\nAborting save operation.")
    else:
        writeFile(file_name, coded_text)
        print("Ciphered text saved!")
    print("Program ending.")

if __name__ == "__main__":
    main()
