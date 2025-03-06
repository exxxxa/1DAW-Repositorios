from videojuegos import Videojuego

resident_evil = Videojuego(
    "Resident Evil",
    ["Terror", "Acción"],
    "5/5/1996",
    9.6,
    18,
    10.99,
    1.45
)

print(resident_evil)

league_of_legends = Videojuego(
    "League of Legends",
    ["MOBA", "ONLINE"],
    "27/10/2009",
    0.1,
    12,
    0,
    20.52
)

league_of_legends.peso += 10
league_of_legends.generos.append("RPG")
print(league_of_legends)
print(resident_evil.apto_menores())
print(league_of_legends.apto_menores())
