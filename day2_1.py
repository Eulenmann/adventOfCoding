def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)

def process_and_handle_ranges(filename):
    solution = 0
    with open(filename, 'r') as file:
        content = file.read().strip()
        ranges = content.split(',')

        for range_str in ranges:
            number_range = range_to_array(range_str.strip())
            for number in number_range:
                num_str = str(number)
                num_length = len(num_str)
                check_if_even_and_left_equals_right(num_length,num_str)



def check_if_even_and_left_equals_right(num_length,num_str):
                if num_length % 2 == 0:
                    half_length = num_length // 2
                    first_half = num_str[:half_length]
                    second_half = num_str[half_length:]

                    if first_half == second_half:
                        old_solution = solution
                        solution += number
                        print(f"Neue Zahl gefunden: {number}")
                        print(f"Rechnung: alte Lösung = {old_solution} + Zahl = {solution}")

    print(f"Die finale Lösung ist: {solution}")

# Beispielaufruf
process_and_handle_ranges("input.txt")