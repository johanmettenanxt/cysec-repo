def encode(text, shift):
    result = ""
    i = 0

    while i < len(text):
        c = text[i]

        if c.isalpha():
            s = 0
            while s < shift:
                if c == 'Z':
                    c = 'A'
                elif c == 'z':
                    c = 'a'
                else:
                    c = chr(ord(c) + 1)
                s += 1
            result += c
        else:
            result += c

        i += 1

    return result


def decode(text, shift):
    result = ""
    i = 0

    while i < len(text):
        c = text[i]

        if c.isalpha():
            s = 0
            while s < shift:
                if c == 'A':
                    c = 'Z'
                elif c == 'a':
                    c = 'z'
                else:
                    c = chr(ord(c) - 1)
                s += 1
            result += c
        else:
            result += c

        i += 1

    return result


print("Caesar Cipher")

choice = input("Wil je encoden of decoden? (E/D): ").upper()
shift = int(input("Geef de shift (bijvoorbeeld 3): "))
message = input("Geef het bericht: ")

if choice == "E":
    result = encode(message, shift)
elif choice == "D":
    result = decode(message, shift)
else:
    print("Ongeldige keuze")
    quit()

print("Resultaat:")
print(result)
