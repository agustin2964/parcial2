from graph import Graph

personajes = Graph()

characters = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO",
    "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

chapters_by_character = {
    "Luke Skywalker": [1, 2, 3, 5],
    "Darth Vader": [1, 3, 6],
    "Yoda": [2, 5],
    "Boba Fett": [4, 6],
    "C-3PO": [1, 2, 3],
    "Leia": [1, 2, 4],
    "Rey": [7, 8, 9],
    "Kylo Ren": [8, 9],
    "Chewbacca": [1, 4],
    "Han Solo": [1, 2, 4],
    "R2-D2": [1, 2, 3],
    "BB-8": [7, 8]
}

for c in characters:
    other_values = {"capitulos": chapters_by_character.get(c, [])}
    personajes.insert_vertex(c, other_values)

edges = [
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Leia", 6),
    ("Luke Skywalker", "Han Solo", 5),
    ("Luke Skywalker", "R2-D2", 5),
    ("Luke Skywalker", "C-3PO", 4),
    ("Luke Skywalker", "Yoda", 1),

    ("Leia", "Han Solo", 5),
    ("Leia", "Chewbacca", 3),
    ("Leia", "C-3PO", 4),

    ("Han Solo", "Chewbacca", 6),
    ("Han Solo", "Boba Fett", 1),

    ("Chewbacca", "R2-D2", 2),

    ("C-3PO", "R2-D2", 6),

    ("Darth Vader", "Yoda", 1),
    ("Darth Vader", "Boba Fett", 2),

    ("Rey", "BB-8", 3),
    ("Rey", "Kylo Ren", 3),
    ("Rey", "Leia", 1),
    ("Kylo Ren", "Darth Vader", 2),
    ("BB-8", "R2-D2", 1)
]

for o, d, w in edges:
    personajes.insert_edge(o, d, w)

print("kruskal desde: C-3PO")
print(personajes.kruskal("C-3PO"))
print()
print("kruskal desde: Yoda")
print(personajes.kruskal("Yoda"))
print()
print("kruskal desde: Leia")
print(personajes.kruskal("Leia"))
print()

max,pares= personajes.max_edge()
print(f"{pares} se contraron {max} veces")
print()

print("dijkstra desde C-3PO a R2-D2:")
print(personajes.dijkstra("C-3PO"))
print()
print("dijkstra desde Yoda a Darth Vader:")
print(personajes.dijkstra("Yoda"))
print()

aux=personajes.capitulos()
if aux==[]:
    print("Ningun personaje aparece en todos los capitulos")
else:
    print(f"Personajes que aparecen en todos los capitulos: {aux}")