from tree import BinaryTree

pokemon_numeros = BinaryTree()
pokemon_nombres = BinaryTree()
pokemon_tipos = BinaryTree()
pokemons = [
    {"name": "Charizard", "number": 6, "types": ["Fire", "Flying"], "weaknesses": ["Water", "Electric", "Rock"], "mega": True, "gigamax": True},
    {"name": "Gengar", "number": 94, "types": ["Ghost", "Poison"], "weaknesses": ["Ground", "Psychic", "Ghost", "Dark"], "mega": True, "gigamax": True},
    {"name": "Scizor", "number": 212, "types": ["Bug", "Steel"], "weaknesses": ["Fire", "Flying"], "mega": True, "gigamax": False},
    {"name": "Jolteon", "number": 135, "types": ["Electric"], "weaknesses": ["Ground"], "mega": False, "gigamax": False},
    {"name": "Lycanroc", "number": 745, "types": ["Rock"], "weaknesses": ["Water", "Grass", "Fighting", "Ground", "Steel"], "mega": False, "gigamax": False},
    {"name": "Tyrantrum", "number": 697, "types": ["Rock", "Dragon"], "weaknesses": ["Water", "Grass", "Fighting", "Ground", "Ice"], "mega": False, "gigamax": False},
    {"name": "Pikachu", "number": 25, "types": ["Electric"], "weaknesses": ["Ground"], "mega": False, "gigamax": True},
    {"name": "Heatran", "number": 485, "types": ["Fire", "Steel"], "weaknesses": ["Ground", "Water", "Fighting"], "mega": False, "gigamax": False},
    {"name": "Mimikyu", "number": 778, "types": ["Ghost", "Fairy"], "weaknesses": ["Ghost", "Steel"], "mega": False, "gigamax": False},
    {"name": "Blaziken", "number": 257, "types": ["Fire", "Fighting"], "weaknesses": ["Water", "Flying", "Psychic"], "mega": True, "gigamax": False},
    {"name": "Metagross", "number": 376, "types": ["Steel", "Psychic"], "weaknesses": ["Fire", "Ground", "Ghost", "Dark"], "mega": True, "gigamax": False},
]

for p in pokemons:
    info = {
        "name": p["name"],
        "number": p["number"],
        "types": p["types"],
        "weaknesses": p["weaknesses"],
        "mega": p["mega"],
        "gigamax": p["gigamax"],
    }


    info_by_number = info.copy()
    info_by_number.pop("number", None)
    pokemon_numeros.insert(p["number"], info_by_number)

    info_by_name = info.copy()
    info_by_name.pop("name", None)
    pokemon_nombres.insert(p["name"], info_by_name)

    info_by_types = info.copy()
    info_by_types.pop("types", None)
    pokemon_tipos.insert((p["types"]), info_by_types)

print("Pokemon por numero:")
print(pokemon_numeros.search(135))
print()

print("Pokemones por proximidad:")
pokemon_nombres.proximity_search("M")
print()

print("Pokemones por tipo ghost:")
pokemon_tipos.proximity_search("Ghost","name")
print()

print("Pokemones por tipo fire:")
pokemon_tipos.proximity_search("Fire","name")
print()

print("Pokemones por tipo steel:")
pokemon_tipos.proximity_search("Steel","name")
print()

print("Pokemones por tipo electric:")
pokemon_tipos.proximity_search("Electric","name")
print()

print("pokemones en orden por numero:")
pokemon_numeros.in_order()
print()

print("pokemones en orden por nombre:")
pokemon_nombres.in_order()
print()

print("pokemones por nivel:")
pokemon_nombres.by_level()
print()

print("pokemones debiles contra Jolteon:")
print(pokemon_nombres.weak_against(pokemon_nombres.search("Jolteon").other_values["types"]))
print()
print("pokemones debiles contra Lycanroc:")
print(pokemon_nombres.weak_against(pokemon_nombres.search("Lycanroc").other_values["types"]))
print()
print("pokemones debiles contra Tyrantrum:")
print(pokemon_nombres.weak_against(pokemon_nombres.search("Tyrantrum").other_values["types"]))
print()

print("cantidad de pokemones por tipo:")
print(pokemon_nombres.count_types())
print()

print(f"pokemones mega evolucionados: {pokemon_nombres.count_bool("mega")}")
print()

print(f"pokemones gigamax: {pokemon_nombres.count_bool("gigamax")}")