fresh_unset_list = []

def day5(range_input):
    fresh_ingredients = create_fresh_ingredient_list(range_input)
    counter = 0
    print("Frische Zutaten:", fresh_ingredients)
    counter = fresh_ingredients
    print(counter)
    return counter

def create_fresh_ingredient_list(range_input):
    with open(range_input, "r") as range_file:
        fresh_unset_list = []
        fresh_ingredients_counter = 0
        for line in range_file:
            line = line.strip()
            print(line)
            ranges = line.split(',')
            print(ranges)
            for range_str in ranges:
                ####start, end = map(int, range_str.split('-'))
                number_range = range_to_array(range_str.strip())
            print(number_range)
            print("erste zahl",number_range[0],"zweite zahl",number_range [-1])
            fresh_ingredients_counter_temp = number_range[-1] - number_range [0]
            print(fresh_ingredients_counter_temp)
            fresh_ingredients_counter += fresh_ingredients_counter_temp
    return fresh_ingredients_counter

def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return (start, end + 1)


result = day5("test_ranges.txt")
if result == 14:
    result = day5("ranges.txt")

print("Frische Zutaten:", result)
