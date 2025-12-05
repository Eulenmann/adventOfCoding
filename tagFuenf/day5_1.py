def day5(ingredients_input,range_input):
    fresh_ingredients = 0
    fresh_unset_list = []
    create_fresh_ingredient_list(range_input)
    create_ingredients_to_check_list(ingredients_input)
    print("Frische Zutaten:", fresh_ingredients)
    print("Zutaten zum Überprüfen:", ingredients_to_check_list)
    
    
 def create_fresh_ingredient_list(range_input):  
    with open(range_input, "r") as rangefile:
        for line in rangefile:
            line = line.strip()
            ranges = line.split(',')
            for range_str in ranges:
                number_range = range_to_array(range_str.strip())
            print(number_range)
            fresh_unset_list.extend(list(number_range))
            fresh_list = list(set(fresh_unset_list))
            print(fresh_unset_list)    
            print(fresh_list)  
    return fresh_ingredients

def create_ingredients_to_check_list(ingredients_input):
    with open(ingredients_input, "r") as ingredientsfile:
        for line in ingredientsfile:
            line = line.strip()
            ingredients_to_check_list.append(int(line))        
            print(ingredients_to_check_list)
    return ingredients_to_check_list

result = day5("test_ingredients.txt","test_ranges.txt")
if result == 3:
    result = day5("ingredients.txt","ranges.txt")

print("Frische Zutaten:", result)