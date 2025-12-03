def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)

def process_and_handle_ranges(input):
    solution = 0
    with open(input, 'r') as file:
        content = file.read().strip()
        ranges = content.split(',')
        teile = None

        for range_str in ranges:
            number_range = range_to_array(range_str.strip())
            for number in number_range:
                num_str = str(number)
                num_length = len(num_str)
                divisors = []
                for i in range(1, number + 1):
                    if number % i == 0:
                        divisors.append(i)
                for divisor in divisors:                                     
                    if divisor != 1 and divisor != num_str:
                        teile = number / divisor
                        print("Teile: {teile} mit Divisor: {divisor} für Zahl: {number}")    



    print("Die finale Lösung ist: {solution}")

process_and_handle_ranges("input.txt")



                        a = 1
                        b = 0
                        if a < teile:
                            if a == 1:
                                teil1 =  num_str[:divisor]
                            if a == 2:
                                teil2 =  num_str[divisor:divisor*2]   
                            if a == 3:
                                teil3 =  num_str[divisor*2:divisor*3]
                            if a == 4:
                                teil4 =  num_str[divisor*3:divisor*4]
                            if a == 5:
                                teil5 =  num_str[divisor*4:divisor*5]
                            if a == 6:
                                teil6 =  num_str[divisor*5:divisor*6]
                            a += 1


                                                    old_solution = solution
                        solution += number
                        print("Neue Zahl gefunden: {number}")
                        print("Rechnung: alte Lösung = {old_solution} + Zahl = {solution}")
                        break