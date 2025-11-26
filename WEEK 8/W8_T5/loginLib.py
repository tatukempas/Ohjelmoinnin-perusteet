import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    user_id = 0
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                if line.strip():
                    user_id += 1
    except FileNotFoundError:
        pass
    pw_hash = hash_password(PPassword)
    with open(CREDENTIALS_FILE, "a") as f:
        f.write(f"{user_id}{DELIMITER}{PUsername}{DELIMITER}{pw_hash}\n")


def login(PUsername: str, PPassword: str) -> bool:
    pw_hash = hash_password(PPassword)
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(DELIMITER)
                if len(parts) == 3:
                    _, username, stored_hash = parts
                    if username == PUsername and stored_hash == pw_hash:
                        return True
    except FileNotFoundError:
        return False
    return False


def viewProfile(PUsername: str) -> list[str]:
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split(DELIMITER)
                if len(parts) == 3:
                    user_id, username, _ = parts
                    if username == PUsername:
                        return [user_id, username]
    except FileNotFoundError:
        pass
    return []


def change_password(PUsername: str, PNewPassword: str) -> None:
    try:
        with open(CREDENTIALS_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    pw_hash = hash_password(PNewPassword)
    new_lines = []

    for line in lines:
        parts = line.strip().split(DELIMITER)
        if len(parts) == 3:
            user_id, username, old_hash = parts
            if username == PUsername:
                new_lines.append(f"{user_id}{DELIMITER}{username}{DELIMITER}{pw_hash}\n")
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    with open(CREDENTIALS_FILE, "w") as f:
        f.writelines(new_lines)

