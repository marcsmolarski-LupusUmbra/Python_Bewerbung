import random


def spieler_ratet():
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
    geheime_zahl = random.randint(1, 100)
    versuche = 0

    while True:
        tipp = input("Dein Tipp: ")

        if not tipp.isdigit():
            print("Bitte gib eine ganze Zahl ein.")
            continue

        tipp = int(tipp)
        versuche += 1

        if tipp < geheime_zahl:
            print("Zu niedrig.")
        elif tipp > geheime_zahl:
            print("Zu hoch.")
        else:
            print(f"Richtig! Du hast {versuche} Versuche gebraucht.")
            break


def computer_ratet():
    print("Denke dir eine Zahl zwischen 1 und 100.")
    print("Antworte mit: höher, tiefer oder richtig.")

    untere_grenze = 1
    obere_grenze = 100
    versuche = 0

    while True:
        tipp = (untere_grenze + obere_grenze) // 2
        versuche += 1

        antwort = input(f"Ist deine Zahl {tipp}? ").lower()

        if antwort == "höher":
            untere_grenze = tipp + 1
        elif antwort == "tiefer":
            obere_grenze = tipp - 1
        elif antwort == "richtig":
            print(f"Ich habe deine Zahl in {versuche} Versuchen erraten!")
            break
        else:
            print("Bitte antworte mit: höher, tiefer oder richtig.")


def hauptmenue():
    print("\nZahlenratespiel")
    print("1 - Ich rate")
    print("2 - Computer rät")

    auswahl = input("Auswahl: ")

    if auswahl == "1":
        spieler_ratet()
    elif auswahl == "2":
        computer_ratet()
    else:
        print("Ungültige Auswahl")


hauptmenue()
