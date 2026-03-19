def main():
    print("Vigenere Cipher")
    print("Wil je encoden of decoden? (E/D)")

    choice = input().upper()

    print("Geef het sleutelwoord (minstens 5 letters):")
    key = input()

    if len(key) < 5:
        print("Sleutelwoord is te kort.")
        return

    print("Geef het bericht:")
    message = input()

    result = ""

    if choice == "E":
        result = vigenere_encode(message, key)
    elif choice == "D":
        result = vigenere_decode(message, key)
    else:
        print("Ongeldige keuze.")
        return

    print("Resultaat:")
    print(result)


def vigenere_encode(text, key):
    result = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            base = ord('A') if char.isupper() else ord('a')
            encoded_char = chr((ord(char) - base + shift) % 26 + base)

            result.append(encoded_char)
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


def vigenere_decode(text, key):
    result = []
    key_index = 0
    key = key.upper()

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            base = ord('A') if char.isupper() else ord('a')
            decoded_char = chr((ord(char) - base - shift) % 26 + base)

            result.append(decoded_char)
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


if __name__ == "__main__":
    main()