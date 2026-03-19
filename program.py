import sqlite3

# Probeer dit in te voeren:
# Skyrim
# ' OR 1=1 --
# Zelda

def main():
    while True:
        print("=== Game Library ===")
        user_input = input("Zoek een game op titel: ")

        connection_string = "games.db"

        with sqlite3.connect(connection_string) as connection:
            cursor = connection.cursor()

            query = (
                "SELECT title, genre, year FROM games WHERE title = '"
                + user_input +
                "'"
            )

            cursor.execute(query)
            rows = cursor.fetchall()

            gevonden = False

            for row in rows:
                gevonden = True
                print("\nGame gevonden:")
                print("Titel:", row[0])
                print("Genre:", row[1])
                print("Jaar:", row[2])


            if not gevonden:
                print("\nGeen games gevonden.")


if __name__ == "__main__":
    main()
