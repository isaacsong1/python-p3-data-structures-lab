spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [dict["name"] for dict in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [dict for dict in spicy_foods if dict["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for dict in spicy_foods:
        print(f"{dict['name']} ({dict['cuisine']}) | Heat Level: {dict['heat_level'] * '🌶'}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for dict in spicy_foods:
        if dict['cuisine'] == cuisine:
            return dict

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    # array = []
    # for dict in spicy_foods:
    #     array.append(dict['heat_level'])
    # return sum(array)/len(array)

    # Cleaner solution
    return sum([dict['heat_level'] for dict in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
