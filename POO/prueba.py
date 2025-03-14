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
print(resident_evil.precio_final(4, 0))

juegos_borja = [
    Videojuego("Dark Souls III", ["RPG", "Acción", "Souls-like"], "2016-04-12", 9.3, 16, 39.99, 25),
    Videojuego("Bloodborne", ["RPG", "Acción", "Souls-like"], "2015-03-24", 9.7, 18, 19.99, 41),
    Videojuego("Elden Ring", ["RPG", "Acción", "Souls-like"], "2022-02-25", 9.8, 16, 59.99, 60),
    Videojuego("Sekiro: Shadows Die Twice", ["Acción", "Souls-like"], "2019-03-22", 9.5, 18, 49.99, 25),
    Videojuego("Lies of P", ["RPG", "Acción", "Souls-like"], "2023-09-19", 9.0, 16, 59.99, 35)
]

juegos_para_menores = [
    juego for juego in juegos_borja
    if juego.PEGI < 18 and juego.puntuacion >= 9.0 and juego.peso < 50
]

print(juegos_borja[0].fecha_salida[-2:])
print(juegos_para_menores)
