import time
import base64
import json
from datetime import datetime, timedelta

correcte_gebruikersnaam = "admin"
correcte_wachtwoord = "wachtwoord"

jwt_token = None
jwt_verloop_tijd = None


def main():
    global jwt_token, jwt_verloop_tijd

    print("=== Login ===")

    username = input("Gebruikersnaam: ")
    password = input("Wachtwoord: ")

    if username != correcte_gebruikersnaam or password != correcte_wachtwoord:
        print("Fout: onjuiste login.")
        return

    jwt_token = genereer_jwt(username)
    jwt_verloop_tijd = datetime.now() + timedelta(minutes=1)

    print("\nLogin succesvol.")
    print("JWT ontvangen door gebruiker.")

    actief = True
    while actief:
        print("\nKies een actie:")
        print("1 - Doe actie")
        print("2 - Stop")
        keuze = input("Keuze: ")

        if keuze == "1":
            print("Actie wordt uitgevoerd...")

            if not is_jwt_geldig():
                print("JWT verlopen. Opnieuw inloggen vereist.")
                return

            time.sleep(2)

            print("Actie voltooid.")

        elif keuze == "2":
            actief = False
        else:
            print("Ongeldige keuze.")

    print("\nApplicatie gestopt.")



def genereer_jwt(gebruikersnaam):

    header = {"alg": "none", "typ": "JWT"}
    payload = {
        "user": gebruikerssnaam_fix(gebruikersnaam),
        "iat": datetime.now().timestamp()
    }

    header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode()
    payload_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()

    token = f"{header_b64}.{payload_b64}."
    return token


def is_jwt_geldig():
    global jwt_token, jwt_verloop_tijd

    if jwt_token is None:
        return False

    if datetime.now() > jwt_verloop_tijd:
        return False

    return True


def gebruikerssnaam_fix(u):
    return u.strip()


if __name__ == "__main__":
    main()