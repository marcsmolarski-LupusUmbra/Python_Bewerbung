def addieren(a, b):
    return a + b


def subtrahieren(a, b):
    return a - b


def multiplizieren(a, b):
    return a * b


def dividieren(a, b):
    if b == 0:
        return "Fehler: Division durch 0 ist nicht erlaubt."
    return a / b


def zahl_eingeben(text):
    while True:
        eingabe = input(text)
        try:
            return float(eingabe)
        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


def hauptmenue():
    while True:
        print("\nTaschenrechner")
        print("1 - Addieren")
        print("2 - Subtrahieren")
        print("3 - Multiplizieren")
        print("4 - Dividieren")

        auswahl = input("Auswahl: ")

        zahl1 = zahl_eingeben("Erste Zahl: ")
        zahl2 = zahl_eingeben("Zweite Zahl: ")

        if auswahl == "1":
            ergebnis = addieren(zahl1, zahl2)
        elif auswahl == "2":
            ergebnis = subtrahieren(zahl1, zahl2)
        elif auswahl == "3":
            ergebnis = multiplizieren(zahl1, zahl2)
        elif auswahl == "4":
            ergebnis = dividieren(zahl1, zahl2)
        else:
            print("Ungültige Auswahl.")
            continue

        print(f"Ergebnis: {ergebnis}")

        erneut = input("Möchtest du noch eine Rechnung durchführen? (j/n): ").lower()
        if erneut != "j":
            print("Programm beendet.")
            break


hauptmenue()
