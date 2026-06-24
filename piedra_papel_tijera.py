"""
============================================================================
 Juego: Piedra, papel o tijera
 Aprendizaje Autonomo 2 - Logica de Programacion (Primer Semestre, Paralelo 1B)
 Universidad Internacional del Ecuador (UIDE) - Modalidad En Linea
 Estudiante: Adan Vinicio Baraja Vega
 Docente:    Ing. Dario Sebastian Cabezas Erazo
----------------------------------------------------------------------------
 Descripcion general:
     Programa de consola que permite al usuario jugar "Piedra, papel o tijera"
     contra la computadora. El sistema valida la jugada del usuario, genera la
     jugada de la maquina de forma aleatoria, determina el ganador segun las
     reglas del juego y permite jugar varias rondas llevando un marcador.

 Relacion con los diagramas del Autonomo 1 (arquitectura en capas):
     - Capa de presentacion ....... entrada/salida por consola (pedir, mostrar).
     - Capa de logica del juego ... validacion, jugada aleatoria y reglas.
     - Capa de datos y recursos ... modulo random y variables del marcador.
============================================================================
"""

import random  # Capa de datos/recursos: generacion aleatoria de la jugada de la maquina

# ---------------------------------------------------------------------------
# CAPA DE DATOS Y RECURSOS
# ---------------------------------------------------------------------------

# Opciones validas del juego. Se centralizan en una sola estructura para
# generalizar el programa y evitar repetir cadenas de texto a lo largo del codigo.
OPCIONES = ("piedra", "papel", "tijera")

# Diccionario de reglas: cada jugada indica a que jugada le gana.
#   piedra -> vence a tijera ; tijera -> vence a papel ; papel -> vence a piedra
REGLAS = {
    "piedra": "tijera",
    "tijera": "papel",
    "papel": "piedra",
}


# ---------------------------------------------------------------------------
# CAPA DE LOGICA DEL JUEGO
# ---------------------------------------------------------------------------

def pedir_jugada():
    """
    Solicita y valida la jugada del usuario.

    input  : texto escrito por el usuario en la consola.
    return : una jugada valida en minusculas ('piedra', 'papel' o 'tijera').

    Usa un bucle 'while' para repetir la peticion mientras la jugada no sea
    valida (corresponde a la decision "Jugada valida?" del diagrama de flujo).
    """
    jugada = input("Elige (piedra / papel / tijera): ").strip().lower()
    while jugada not in OPCIONES:          # bucle de validacion de la entrada
        print("  -> Jugada no valida. Intenta de nuevo.")
        jugada = input("Elige (piedra / papel / tijera): ").strip().lower()
    return jugada


def jugada_maquina():
    """
    Genera la jugada de la maquina de forma aleatoria.

    return : una de las opciones validas elegida al azar con random.choice.
    """
    return random.choice(OPCIONES)


def determinar_ganador(jugador, maquina):
    """
    Compara las dos jugadas y determina el resultado de la ronda.

    input  : jugada del jugador y jugada de la maquina.
    return : 'empate', 'jugador' o 'maquina'.

    Usa estructuras condicionales (if / elif / else) para aplicar las reglas
    del juego almacenadas en el diccionario REGLAS.
    """
    if jugador == maquina:
        return "empate"
    elif REGLAS[jugador] == maquina:      # la jugada del jugador vence a la de la maquina
        return "jugador"
    else:
        return "maquina"


# ---------------------------------------------------------------------------
# CAPA DE PRESENTACION
# ---------------------------------------------------------------------------

def mostrar_resultado(jugador, maquina, resultado):
    """
    Muestra por consola las jugadas y el resultado de la ronda.
    No retorna ningun valor (None); solo produce salida en pantalla.
    """
    print("\nTu jugaste : " + jugador)
    print("La maquina : " + maquina)
    if resultado == "empate":
        print("Resultado  : Empate.")
    elif resultado == "jugador":
        print("Resultado  : Ganaste esta ronda!")
    else:
        print("Resultado  : La maquina gano esta ronda.")


def jugar():
    """
    Funcion principal. Controla el ciclo del juego y el marcador.

    Usa un bucle 'while' que permite jugar varias rondas hasta que el usuario
    decida no continuar. Mantiene en memoria el marcador del jugador, de la
    maquina y los empates (variables de la capa de datos).
    """
    print("==============================")
    print("   PIEDRA, PAPEL O TIJERA")
    print("==============================")

    # Marcador en memoria (variables que almacenan el estado del juego)
    victorias_jugador = 0
    victorias_maquina = 0
    empates = 0

    continuar = True
    while continuar:                       # bucle principal: una vuelta por ronda
        jugador = pedir_jugada()
        maquina = jugada_maquina()
        resultado = determinar_ganador(jugador, maquina)
        mostrar_resultado(jugador, maquina, resultado)

        # Actualizacion del marcador segun el resultado de la ronda
        if resultado == "jugador":
            victorias_jugador += 1
        elif resultado == "maquina":
            victorias_maquina += 1
        else:
            empates += 1

        # Marcador acumulado
        print("\nMarcador -> Tu: " + str(victorias_jugador) +
              " | Maquina: " + str(victorias_maquina) +
              " | Empates: " + str(empates))

        # Preguntar si desea jugar otra ronda (validacion de la respuesta)
        respuesta = input("\nDeseas jugar otra vez? (s/n): ").strip().lower()
        while respuesta not in ("s", "n"):
            respuesta = input("Responde 's' para si o 'n' para no: ").strip().lower()
        continuar = (respuesta == "s")

    # Mensaje final al terminar el juego
    print("\n========== FIN DEL JUEGO ==========")
    print("Ganaste " + str(victorias_jugador) + " ronda(s), perdiste " +
          str(victorias_maquina) + " y empataste " + str(empates) + ".")
    print("Gracias por jugar!")


# Punto de entrada del programa
if __name__ == "__main__":
    jugar()
