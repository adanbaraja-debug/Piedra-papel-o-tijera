# Piedra, papel o tijera — Aprendizaje Autónomo 2

**Asignatura:** Lógica de Programación — Primer Semestre (Paralelo 1B)
**Carrera:** Ingeniería en Software — Modalidad En Línea
**Universidad:** Universidad Internacional del Ecuador (UIDE)
**Estudiante:** Adán Vinicio Baraja Vega
**Docente:** Ing. Darío Sebastián Cabezas Erazo

---

## Descripción

Implementación en **Python (consola)** del juego *Piedra, papel o tijera*,
diseñado previamente en el Aprendizaje Autónomo 1 mediante diagramas de flujo,
de casos de uso y de arquitectura. El programa valida la jugada del usuario,
genera la jugada de la máquina de forma aleatoria, determina el ganador según
las reglas del juego y permite jugar varias rondas llevando un marcador.

## Estructura del repositorio

```
piedra-papel-tijera/
├── README.md                  # Este archivo
├── piedra_papel_tijera.py     # Código fuente del programa
└── diagramas/
    ├── diagrama_flujo.png      # Diagrama de flujo (Autónomo 1)
    ├── casos_de_uso.png        # Diagrama de casos de uso (Autónomo 1)
    └── arquitectura.png        # Diagrama de arquitectura en capas (Autónomo 1)
```

## Reglas del juego

- La **piedra** vence a la **tijera**.
- La **tijera** vence al **papel**.
- El **papel** vence a la **piedra**.
- Si ambos eligen la misma opción, la ronda es **empate**.

## Cómo ejecutar

Requisito: tener instalado Python 3.

```bash
python piedra_papel_tijera.py
```

## Conceptos aplicados

- Funciones con documentación (docstrings).
- Estructuras condicionales (`if` / `elif` / `else`).
- Estructuras repetitivas (`while`) para la validación y el ciclo de rondas.
- Módulo `random` de la biblioteca estándar de Python.
- Organización del código siguiendo la arquitectura en capas del Autónomo 1.
