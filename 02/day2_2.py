def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)


def process_and_handle_ranges(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        ranges = content.split(',')

        for range_str in ranges:
            number_range = range_to_array(range_str.strip())
            for number in number_range:
                num_str = str(number)
                num_length = len(num_str)
                divisors = []
                for i in range(1, number + 1):
                    print(i)
                    if number % i == 0:
                        divisors.append(i)
                #print("Ganzzahlige Divisoren für",number,"sind:",divisors)
                for divisor in divisors:                                     
                    if divisor != 1 and divisor != number:
                        #Ermittle wieviele Teile entstehen wenn man die Ziffer durch den ganzzahligen Divisor teilt
                        teile = number / divisor
                        teile = int(teile)
                        stelle = number / teile
                        stelle = int(stelle)
                       # a = 1
                       # b = 0
                       # if a < teile:
                        if teile == 2:
                            first_half = num_str[:stelle-1]
                            second_half = num_str[stelle:]
                            print("2 Teile","erster Teil:",first_half,"zweiter Teil:",second_half)  
                        if teile == 3:
                            teil3 = num_str[divisor*2:divisor*3]
                            print("3 Teile",teil3) 
                        if teile == 4:
                            teil4 = num_str[divisor*3:divisor*4]
                            print("4 Teile",teil4)
                        if teile == 5:
                            teil5 = num_str[divisor*4:divisor*5]
                            print("5 Teile",teil5)
                        if teile == 6:
                            teil6 = num_str[divisor*5:divisor*6]
                            print("6 Teile",teil6)
                       #a += 1


                        #old_solution = solution
                        #solution += number
                        #print("Neue Zahl gefunden: {number}")
                        #print("Rechnung: alte Lösung = {old_solution} + Zahl = {solution}")
                        #break

                        print(f"Teile: {teile} mit Divisor: {divisor} für Zahl: {number}")  
                
    return solution 

solution = process_and_handle_ranges("input.txt")
print("Die finale Lösung ist: {solution}")

