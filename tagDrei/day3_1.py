def process_day3(filename):
    maxVoltage = 0

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            # Platzhalter für größte und zweitgrößte Ziffer
            best_digit = -1
            best_index = -1

            second_digit = -1
            second_index = -1

            # Einmal über die Zeile iterieren (O(n))
            for index, char in enumerate(line):
                digit = int(char)

                # Größte Ziffer gefunden?
                if digit > best_digit:
                    # alter best wird second
                    second_digit = best_digit
                    second_index = best_index

                    # neuer best
                    best_digit = digit
                    best_index = index

                # zweitgrößte Ziffer gefunden?
                elif digit > second_digit:
                    second_digit = digit
                    second_index = index

            # Zweistellige Zahl in richtiger Reihenfolge bilden
            if best_index < second_index:
                double_digit = best_digit * 10 + second_digit
            else:
                double_digit = second_digit * 10 + best_digit

            # Aufaddieren
            maxVoltage += double_digit

    return maxVoltage


# Beispielaufruf:
result = process_day3("input_tag3.txt")
print("Gesamt-Maximalspannung:", result)