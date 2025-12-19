def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)


def process_and_handle_ranges(filename, verbose=False):
    # stream ranges from file without loading whole file into memory
    def iter_ranges(path, sep=',', chunk_size=8192):
        with open(path, 'r', encoding='utf-8') as f:
            buf = ''
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                buf += chunk
                parts = buf.split(sep)
                for p in parts[:-1]:
                    yield p.strip()
                buf = parts[-1]
            if buf.strip():
                yield buf.strip()

    solution = 0
    for range_str in iter_ranges(filename):
        number_range = range_to_array(range_str.strip())
        for number in number_range:
                num_str = str(number)
                num_length = len(num_str)
                # Divisoren beziehen sich auf die Länge der Zahl (num_length),
                # nicht auf die Zahl selbst — iteriere daher nur bis num_length.
                divisors = [i for i in range(1, num_length + 1) if num_length % i == 0]
                if verbose:
                    print("Ganzzahlige Divisoren für", number, "sind:", divisors)
                for divisor in divisors:                                     
                    if divisor != 1 and divisor != num_length:
                        #Ermittle wieviele Teile entstehen wenn man die länge der Ziffer durch den ganzzahligen Divisor teilt
                        # teile = wie viele Teile entstehen (z.B. 2 für zwei Hälften)
                        teile = num_length // divisor
                        if verbose:
                            print("Anzahl der Teile:", teile)
                        # stelle = Länge eines Teils (Anzahl Zeichen pro Teil)
                        stelle = num_length // teile
                        if verbose:
                            print("Stelle:", stelle)
                       # a = 1
                       # b = 0
                       # if a < teile:
                        if teile == 2:
                            first_half = num_str[:stelle]
                            second_half = num_str[stelle:]
                            if first_half == second_half:
                                old_solution = solution
                                solution += number
                                if verbose:
                                    print("Neue Zahl gefunden:", number)
                                    print("Rechnung: alte Lösung =", old_solution, " + Zahl = ", number)
                                break
                            if verbose:
                                print("2 Teile","erster Teil:",first_half,"zweiter Teil:",second_half)  
                        if teile == 3:
                            teil3 = num_str[stelle*2:stelle*3]
                            if verbose:
                                print("3 Teile", teil3)
                        if teile == 4:
                            teil4 = num_str[stelle*3:stelle*4]
                            if verbose:
                                print("4 Teile", teil4)
                        if teile == 5:
                            teil5 = num_str[stelle*4:stelle*5]
                            if verbose:
                                print("5 Teile", teil5)
                        if teile == 6:
                            teil6 = num_str[stelle*5:stelle*6]
                            if verbose:
                                print("6 Teile", teil6)
                       #a += 1

                        #if verbose: Ausgabe zu Teilen/Divisor
                        if verbose:
                            print(f"Teile: {teile} mit Divisor: {divisor} für Zahl: {number}")  
                
    return solution


if __name__ == '__main__':
    loesung = process_and_handle_ranges("test_input.txt")
    print("Die finale Lösung ist:",loesung)

