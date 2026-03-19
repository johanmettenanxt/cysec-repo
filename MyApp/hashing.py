import hashlib


GLOBAL_SALT = "mijn_geheime_salt"

opgeslagen_gebruikersnaam = None
opgeslagen_wachtwoord_hash = None


def main():
    global opgeslagen_gebruikersnaam, opgeslagen_wachtwoord_hash

    running = True

    while running:
        print("\nKies een optie:")
        print("1 - Aanmelden")
        print("2 - Inloggen")
        print("3 - Stoppen")
        keuze = input("Keuze: ")

        if keuze == "1":
            registreer_gebruiker()
        elif keuze == "2":
            login_gebruiker()
        elif keuze == "3":
            running = False
        else:
            print("Ongeldige keuze.")

    print("Programma beëindigd.")



def registreer_gebruiker():
    global opgeslagen_gebruikersnaam, opgeslagen_wachtwoord_hash

    gebruikersnaam = input("Kies een gebruikersnaam: ")
    wachtwoord = input("Kies een wachtwoord: ")

    wachtwoord_hash = hash_wachtwoord(wachtwoord)

    opgeslagen_gebruikersnaam = gebruikersnaam
    opgeslagen_wachtwoord_hash = wachtwoord_hash

    print("Account succesvol aangemaakt.")


def login_gebruiker():
    global opgeslagen_gebruikersnaam, opgeslagen_wachtwoord_hash

    if opgeslagen_gebruikersnaam is None:
        print("Er is nog geen gebruiker geregistreerd.")
        return

    gebruikersnaam = input("Gebruikersnaam: ")
    wachtwoord = input("Wachtwoord: ")

    wachtwoord_hash = hash_wachtwoord(wachtwoord)

    if (gebruikersnaam == opgeslagen_gebruikersnaam and
            wachtwoord_hash == opgeslagen_wachtwoord_hash):
        print("Succesvol ingelogd!")
    else:
        print("Onjuiste gegevens.")


def hash_wachtwoord(wachtwoord):
    gecombineerde_input = wachtwoord + GLOBAL_SALT
    hash_object = hashlib.sha256(gecombineerde_input.encode())
    return hash_object.hexdigest()


if __name__ == "__main__":
    main()