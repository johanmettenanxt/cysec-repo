class CaesarCipher:

    @staticmethod
    def Main():
        print("Caesar Cipher")
        print("Wil je encoden of decoden? (E/D)")

        choice = input().upper()

        print("Geef de shift (bijvoorbeeld 3):")
        shift = int(input())

        print("Geef het bericht:")
        message = input()

        if choice == "E":
            result = CaesarCipher.Encode(message, shift)

        elif choice == "D":
            result = CaesarCipher.Decode(message, shift)

        else:
            print("Ongeldige keuze.")
            return

        print("Resultaat:")
        print(result)

    @staticmethod
    def Encode(text, shift):
        result = ""

        for a in text:

            if a.isalpha():
                base = ord('A') if a.isupper() else ord('a')

                result += chr((ord(a) - base + shift) % 26 + base)

            else:
                result += a

        return result

    @staticmethod
    def Decode(text, shift):
        return CaesarCipher.Encode(text, -shift)

if __name__ == "__main__":
    CaesarCipher.Main()
