print("Willkommen beim Unit Converter. Ich bin dir gerne beim Umrechnen von Kilometerangaben in Meilen behilflich.")

while True:
    user_input = input("Bitte gib die gewünschte Anzahl Kilometer ein: ")
    km = int(user_input)
    miles = km * 0.621371
    print(str(km) + " Kilometer entsprechen " + str(miles) + " Meilen.")
    proceed = input("Möchtest Du eine weitere Zahl eingeben? Falls ja, gib bitte JA ein. Falls nicht, gibt bitte NEIN ein: ")
    if proceed.upper() == str("NEIN"):
        print("Vielen Dank für Deinen Besuch!")
        break