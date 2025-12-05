fresh_unset_list = []

def day5(ingredients_input, range_input):
    fresh_ingredients = create_fresh_ingredient_list(range_input)
    counter = 0
    print("Frische Zutaten:", fresh_ingredients)
    counter = len(fresh_ingredients)
    return counter


def create_fresh_ingredient_list(range_input):
    with open(range_input, "r") as rangefile:
        fresh_unset_list = []
        for line in rangefile:
            line = line.strip()
            ranges = line.split(',')
            for range_str in ranges:
                start, end = map(int, range_str.split('-'))
                number_range = range_to_array(range_str.strip())
            print(number_range)
            fresh_unset_list = fresh_unset_list + list(set(number_range) - set(fresh_unset_list))
            #fresh_unset_list.extend(list(number_range))
            fresh_ingredients = list(set(fresh_unset_list))
            print(fresh_unset_list)    
            print(fresh_ingredients)
    return fresh_ingredients


def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)

result = day5("test_ingredients.txt","test_ranges.txt")
if result == 14:
    result = day5("ingredients.txt","ranges.txt")

print("Frische Zutaten:", result)