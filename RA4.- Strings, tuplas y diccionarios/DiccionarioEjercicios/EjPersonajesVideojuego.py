'''Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. 
Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

    El caballero tiene el doble de vida y defensa que un guerrero.
    El guerrero tiene el doble de ataque y alcance que un caballero.
    El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
    Muestra como quedan las propiedades de los tres personajes.
'''

personajes = {
    "caballero": {
        "vida": "",
        "defensa": "",
        "ataque": 2,
        "alcance": 2
    },
    "guerrero": {
        "vida": 2,
        "defensa": 2,
        "ataque": "",
        "alcance": ""
    },
    "arquero": {
        "vida": "",
        "defensa": "",
        "ataque": "",
        "alcance": ""
    },
}

def configurarPersonaje(personaje):
    match personaje:
        case "caballero":
            personajes["caballero"]["vida"] = personajes["guerrero"]["vida"] * 2
            personajes["caballero"]["defensa"] = personajes["guerrero"]["defensa"] * 2
        case "guerrero":
            personajes["guerrero"]["ataque"] = personajes["caballero"]["ataque"] * 2
            personajes["guerrero"]["alcance"] = personajes["caballero"]["alcance"] * 2
        case "arquero":
            personajes["arquero"]["vida"] = personajes["guerrero"]["vida"]
            personajes["arquero"]["ataque"] = personajes["guerrero"]["ataque"]
            personajes["arquero"]["defensa"] = personajes["guerrero"]["defensa"] // 2
            personajes["arquero"]["alcance"] = personajes["guerrero"]["alcance"] * 2

configurarPersonaje("caballero")
configurarPersonaje("guerrero")
configurarPersonaje("arquero")
print(personajes)