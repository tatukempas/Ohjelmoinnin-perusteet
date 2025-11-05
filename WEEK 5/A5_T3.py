def askname() -> str:
    name = input("Insert name: ")
    return name


def greetuser(Pname) -> None:
    print(f"Hello {Pname}!")
    return None


def main() -> None:
    print("Program starting.")
    name = askname()
    greetuser(name)
    print("Program ending")
    return None

main ()