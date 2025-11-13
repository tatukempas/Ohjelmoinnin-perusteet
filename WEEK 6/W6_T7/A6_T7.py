LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ";"

LOCATIONS = ["Home", "Galba's palace", "Otho's palace", "Vitellius' palace", "Vespasian's palace"]

PROGRESS_FILE = "player_progress.txt"

def shiftCharacter(char: str, shift) -> str:
    if isinstance(shift, str):
        shift = 13
    if char in LOWER_ALPHABETS:
        index = (LOWER_ALPHABETS.index(char) + shift) % 26
        return LOWER_ALPHABETS[index]
    elif char in UPPER_ALPHABETS:
        index = (UPPER_ALPHABETS.index(char) + shift) % 26
        return UPPER_ALPHABETS[index]
    else:
        return char

def rot13(text: str) -> str:
    result = ""
    for char in text:
        result += shiftCharacter(char, 13)
    return result

def readFile():
    with open(PROGRESS_FILE, "r", encoding="UTF-8") as f:
        lines = f.readlines()
    return lines

def writeFile(next_location_id: int, passphrase_encrypted: str, passphrase_plain: str) -> str:
    encrypted_filename = f"{next_location_id}_{passphrase_encrypted}.gkg"
    with open(encrypted_filename, "r", encoding="UTF-8") as f:
        encrypted_content = f.read()
    first_line_encrypted = encrypted_content.split('\n')[0]
    plain_content = rot13(encrypted_content)
    plain_filename = f"{next_location_id}-{passphrase_plain}.txt"
    with open(plain_filename, "w", encoding="UTF-8") as f:
        f.write(plain_content)
    return first_line_encrypted

def appendFile(current_id: int, next_id: int, passphrase: str):
    new_line = f"{current_id}{DELIMITER}{next_id}{DELIMITER}{passphrase}"
    with open(PROGRESS_FILE, "a", encoding="UTF-8") as f:
        f.write(new_line + "\n")
    print("[Game] Progress autosaved!")

def main():
    print("Travel starting.")
    PlayerProgress = "player_progress.txt"
    Progress = readFile()
    Progress = [line for line in Progress if line.strip()]
    LastProgress = Progress[-1].strip().split(DELIMITER)
    Current_ID = int(LastProgress[0])
    CurrentLocation = LOCATIONS[Current_ID]
    NextLocationID = int(LastProgress[1])
    NextLocation = LOCATIONS[NextLocationID]
    passphrase = LastProgress[2]
    passphrase_plain = rot13(passphrase)

    print(f"Currently at {CurrentLocation}.")
    print(f"Travelling to {NextLocation}...")
    print(f"...Arriving to {NextLocation}.")
    print("Passing the guard at the entrance.")
    print(f'\"{passphrase_plain.capitalize()}!\"')
    print("Looking for the message in the palace...")
    print("Ah, there it is! Seems cryptic.")

    if Current_ID == NextLocationID:
        print(f"Already at final location: {CurrentLocation}. No more travel.")
        print("Travel ending.")
        return

    print("Deciphering Emperor's message...")

    next_progress = writeFile(NextLocationID, passphrase, passphrase_plain)
    new_current, new_next, new_passphrase = next_progress.split(DELIMITER)
    appendFile(int(new_current), int(new_next), new_passphrase)

    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")

if __name__ == "__main__":
    main()