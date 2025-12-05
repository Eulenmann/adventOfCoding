fresh_unset_list = []
def day5(ingredients_input, range_input):
    fresh_ingredients = create_fresh_ingredient_list(range_input)
    ingredients_to_check_list = create_ingredients_to_check_list(ingredients_input)
    counter = 0
    for ingredient in ingredients_to_check_list:
        if ingredient in fresh_ingredients:
            counter += 1
            print(ingredient , counter)

    print("Frische Zutaten:", fresh_ingredients)
    print("Zutaten zum Überprüfen:", ingredients_to_check_list)

    return counter


def create_fresh_ingredient_list(range_input):
    with open(range_input, "r") as rangefile:
        fresh_unset_list = []
        for line in rangefile:
            line = line.strip()
            ranges = line.split(',')
            for range_str in ranges:
                number_range = range_to_array(range_str.strip())
            print(number_range)
            fresh_unset_list.extend(list(number_range))
            fresh_ingredients = list(set(fresh_unset_list))
            print(fresh_unset_list)    
            print(fresh_ingredients)
    return fresh_ingredients

def create_ingredients_to_check_list(ingredients_input, ingredients_to_check_list=[]):
    with open(ingredients_input, "r") as ingredientsfile:
        for line in ingredientsfile:
            line = line.strip()
            ingredients_to_check_list.append(int(line))        
            print(ingredients_to_check_list)
    return ingredients_to_check_list

def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)

result = day5("test_ingredients.txt","test_ranges.txt")
if result == 3:
    result = day5("ingredients.txt","ranges.txt")

print("Frische Zutaten:", result)