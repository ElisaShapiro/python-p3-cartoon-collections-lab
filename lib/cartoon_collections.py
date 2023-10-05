def roll_call_dwarves(list_of_dwarves):
    i = 1
    for dwarf in list_of_dwarves:
        print(f'{i}. {dwarf}')
        i += 1

def summon_captain_planet(list_of_calls):
    return[f'{call.title()}!' for call in list_of_calls]

def long_planeteer_calls(list_of_calls):
    for call in list_of_calls:
        if len(call) > 4:
            return True
    return False

CHEESES = ["camembert", "cheddar", "gouda"]

def find_the_cheese(list_of_foods):
    for food in list_of_foods:
        if food in CHEESES:
            return food
    return None
