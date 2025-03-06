from videojuegos import Videojuego

lista_juegos = [
    Videojuego("The Witcher", ["RPG", "ACCION", "AVENTURA"], "2015-05-19", 9.7, 18, 39.99, 50),
    Videojuego("Grand Theft Auto", ["ACCION", "MUNDO ABIERTO"], "2013-09-17", 9.5, 18, 29.99, 95),
    Videojuego("The Legends of Zelda: Breath of the Wild", ["ACCION", "MUNDO ABIERTO"], "2017-03-03", 10, 12, 59.99, 13.4),
    Videojuego("Minecraft", ["Supervivencia", "Sandbox"], "2011-11-18", 9.0, 7, 26.95, 1.2),
    Videojuego("Red Dead Redemption", ["ACCION", "MUNDO ABIERTO"], "2018-10-26", 9.8, 18, 59.99, 150),
    Videojuego("God of War(2018)", ["ACCION", "AVENTURA"], "2018-04-20", 9.6, 18, 49.99, 45),
    Videojuego("Dark Souls III", ["RPG", "ACCION"], "2016-04-12", 9.3, 16, 39.99, 25),
    Videojuego("Animal Crossing: New Horizons", ["SIMULACIÓN", "SOCIAL"], "2020-03-20", 9.1, 3, 49.99, 10.2),
    Videojuego("Cyberpunk 2077", ["RPG", "MUNDO ABIERTO"], "2020-12-10", 8.5, 18, 59.99, 70),
    Videojuego("Super Mario Odyssey", ["PLATAFORMAS", "AVENTURA"], "2017-10-27", 9.8, 7, 49.99, 5.6)
]

for v in lista_juegos:
    print(v)
