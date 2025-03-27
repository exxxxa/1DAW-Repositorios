from datetime import datetime
import math


class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, descubierto: datetime, lunas: list):
        """
        Clase que representa un planeta.

        :param nombre: Nombre del planeta.
        :param masa: Masa del planeta en kilogramos.
        :param radio: Radio del planeta en metros.
        :param descubierto: Fecha de descubrimiento (datetime).
        :param lunas: Lista de lunas, cada una representada por [nombre, radio, masa].
        """
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.descubierto = descubierto
        self.lunas = lunas

    def get_densidad(self) -> float:
        """
        Calcula la densidad del planeta en kg/m³.
        Fórmula: densidad = masa / volumen
        Volumen de una esfera: (4/3) * π * r³
        """
        volumen = (4 / 3) * math.pi * (self.radio ** 3)
        return self.masa / volumen if volumen > 0 else 0

    def __str__(self):
        """
        Representación en cadena del planeta.
        """
        fecha_desc = self.descubierto.strftime("%Y-%m-%d")  # Convertir datetime a string
        lunas_info = ", ".join([f"{luna[0]} (radio: {luna[1]}m, masa: {luna[2]}kg)" for luna in self.lunas])
        return (f"🌍 Planeta: {self.nombre}\n"
                f"   - Masa: {self.masa} kg\n"
                f"   - Radio: {self.radio} m\n"
                f"   - Descubierto: {fecha_desc}\n"
                f"   - Densidad: {self.get_densidad():.2f} kg/m³\n"
                f"   - Lunas: {lunas_info if lunas_info else 'No tiene'}")


planetas = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna", 1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4, 1.0659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Júpiter", 1.898e27, 6.9911e7, datetime.min, [["Ganimedes", 2.634e6, 1.0659e16], ["Calisto", 2.410e6, 1.0759e23], ["Ío", 1.821e6, 8.9319e22], ["Europa", 1.560e6, 4.7998e22]]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [["Titán", 2.572e6, 1.3452e23], ["Rea", 1.527e6, 2.3166e21], ["Japeto", 1.470e6, 1.8056e21], ["Dione", 1.123e6, 1.0955e21]]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6, 3.527e21]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Tritón", 1.353e6, 2.14e22]]),
    Planeta("Plutón", 1.303e22, 1.1883e6, datetime(1930, 2, 18), [["Caronte", 6.057e5, 1.586e21]])
]

print(planetas[2].masa)
print(planetas[4].lunas[0])

for planeta in planetas:
    print(planeta.masa)

planeta_mayor_densidad = 0
mayor_densidad = 0

for planeta in planetas:
    densidad = planeta.get_densidad()
    if densidad > mayor_densidad:
        mayor_densidad = densidad
        planeta_mayor_densidad = planeta

print(f"El planeta con mayor densidad es: {planeta_mayor_densidad.nombre} con una densidad de {planeta_mayor_densidad.get_densidad()} kg/m³")


densidades = [planeta.get_densidad() for planeta in planetas]

mayor_densidad = max(densidades)
planeta_mayor_densidad = [planeta for planeta in planetas if planeta.get_densidad() == mayor_densidad][0]

print(planeta_mayor_densidad)

# Encuentra las lunas que sean mas grandes que la Luna
# Paso 1 encuentro el radio de la Luna
radio_luna = 0
for planeta in planetas:
    for luna in planeta.lunas:
        if luna[0] == "Luna":
            radio_luna = luna[1]
            break
# Paso 2, encontramos las lunas mas grandes que la Luna
lunas_mas_grandes = []
for planeta in planetas:
    for luna in planeta.lunas:
        if luna[1] > radio_luna:
            lunas_mas_grandes.append(luna[0])

print(f"Las lunas mas grandes que la luna son: {lunas_mas_grandes}")

# Encuentra la luna mas pequeña
radios_lunas = []

for planeta in planetas:
    for luna in planeta.lunas:
        radios_lunas.append(luna[1])

radio_min = min(radios_lunas)

for planeta in planetas:
    for luna in planeta.lunas:
        if luna[1] == radio_min:
            print(f"La luna mas pequeña es: {luna[0]}")
            break
