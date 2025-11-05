DELIMITER = ","

def collectWords():
    collected_words = ""
    while True:
        word = input("Insert word(empty stops): ").strip()
        if word == "":
            break
        if collected_words:
            collected_words += DELIMITER
        collected_words += word
    return collected_words


def analyseWords(words_str):
    word_list = words_str.split(DELIMITER) if words_str else []

    word_list = [w for w in word_list if w]

    words = len(word_list)
    chars = sum(len(w) for w in word_list)
    avg_length = chars / words if words > 0 else 0

    print(f"- {words} Words")
    print(f"- {chars} Characters")
    print("- {:.2f} Average word length".format(avg_length))


def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")


if __name__ == "__main__":
    main()