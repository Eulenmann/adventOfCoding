fresh_unset_list = []
ingredients_to_check_list = []

def day5(ingredients_input, range_input):
    fresh_ingredients = create_fresh_ingredient_list(range_input)
    ingredients_to_check_list = create_ingredients_to_check_list(ingredients_input)
    counter = 0
    for ingredient in ingredients_to_check_list:
        for r in fresh_ingredients:
            templist = list(r)
            if templist[0] < ingredient < templist [-1]: 
                print(templist[0] , "<" , ingredient , "<" , templist[-1])
                counter += 1
                #print(ingredient , counter)
                break
            else:
               # print(templist[0] , "<" , ingredient , "<" , templist[-1])
                print(counter)

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
                start, end = map(int, range_str.split('-'))
                #number_range = range_to_array(range_str.strip())
            #print(number_range)
            #fresh_unset_list.extend(list(number_range))
            #fresh_ingredients = list(set(fresh_unset_list))
            #print(fresh_unset_list)
            #print (start)
            #print (end)
            fresh_unset_list.append([start, end+1]) 
            #print(fresh_unset_list)
            fresh_ingredients = list(fresh_unset_list)
            #print(fresh_ingredients)
    return fresh_ingredients

def create_ingredients_to_check_list(ingredients_input):
    with open(ingredients_input, "r") as ingredientsfile:
        for line in ingredientsfile:
            line = line.strip()
            ingredients_to_check_list.append(int(line))        
            #print(ingredients_to_check_list)
    return ingredients_to_check_list

def range_to_array(range_str):
    start, end = map(int, range_str.split('-'))
    return range(start, end + 1)

result = day5("test_ingredients.txt","test_ranges.txt")
if result == 3:
    result = day5("ingredients.txt","ranges.txt")

print("Frische Zutaten:", result)