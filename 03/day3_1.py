def day3(filename):
    maxVoltage = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Platzhalter für größte und zweitgrößte Ziffer
            hoechste_ziffer = 0
            hoechste_ziffer_index = 0

            zweithoechste_ziffer = 0
            zweithoechste_ziffer_index = 0
            letzter_index = len(str(line))
            print(letzter_index)
            # Einmal über die Zeile iterieren (O(n))
            for index, char in enumerate(line):
                ziffer = int(char)

                # Größte Ziffer gefunden?
                if ziffer > hoechste_ziffer:
                    print("Ziffer", ziffer ,"ist höher als", hoechste_ziffer)
                    if index == letzter_index-1:
                       zweithoechste_ziffer = ziffer
                       break
                    # second wird auf 0 gesetzt
                    zweithoechste_ziffer = 0
                    zweithoechste_ziffer_index = 0
                    print("Zweite Ziffer", zweithoechste_ziffer)

                    # neuer best
                    hoechste_ziffer = ziffer
                    hoechste_ziffer_index = index
                    print("Neue höchste", hoechste_ziffer,"\n")
                # zweitgrößte Ziffer gefunden?
                elif ziffer > zweithoechste_ziffer:
                    zweithoechste_ziffer = ziffer
                    zweithoechste_ziffer_index = index
                    print("Neue Zweite", zweithoechste_ziffer)
            # Zweistellige Zahl bilden
            doppel_ziffer = hoechste_ziffer * 10 + zweithoechste_ziffer
            print("Voltage der Zeile:", doppel_ziffer)
            # Aufaddieren
            maxVoltage += doppel_ziffer

    return maxVoltage


# Beispielaufruf:
result = day3("inputTag3.txt")
print("Gesamt-Maximalspannung:", result)