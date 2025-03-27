from datetime import datetime


def tiempo_pasado(fec_pasada: datetime) -> int:
    hoy = datetime.now()
    # Calcular la diferencia de años teniendo en cuenta si ya pasó el cumpleaños este año
    edad = hoy.year - fec_pasada.year - ((hoy.month, hoy.day) < (fec_pasada.month, nacimiento.day))
    return edad


# Creo una fecha concreta
nacimiento = datetime(1999, 1, 31)
print(nacimiento)
print(nacimiento.year)
print(nacimiento.month)
print(nacimiento.hour)
print(nacimiento.minute)
print(nacimiento.day)
# Puedo definir también la hora, minuto y segundo
# (Si no se especifica se pone como 00:00:00)
nacimiento = datetime(1999, 1, 31, 23, 15)
print(nacimiento)


# La ventaja de usar datetime en vez de str para fechas
# es que podemos compararlas


pedro_nacimiento = datetime(1998, 4, 5)
maria_nacimiento = datetime(1999, 7, 8)


if pedro_nacimiento < maria_nacimiento:
    print("Pedro es más viejo que María")
else:
    print("María es más vieja de que Pedro")


# Creada una fecha podemos obtener sus atributos por separado
print(f"María nació en el año {maria_nacimiento.year}")


# Para obtener el día actual, también podemos usar
hoy = datetime.now()
print(hoy)


# Podemos formatear la fecha como queramos con strftime
print(hoy.strftime("%m - %Y"))

