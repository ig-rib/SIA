# Requerimientos
Python 3

# Ejecución
Para ejecutar el programa, situarse en la carpeta TP2 y ejecutar en consola:
```
python3 main.py [Clase Objetivo] [ubicación de la carpeta de archivos de prueba]
```

# Archivos de Configuraciones

Es necesario el archivo solver.config, que tiene la siguiente forma (el orden de las líneas no importa):

    CROSSING-OVER [Método]
    MUTATION [Método]
    SELECTION [M1, M2, M3, M4]
    IMPLEMENTATION [Método]
    STOP-CRITERION [Método, Parámetro Crítico]
    PM [Probabilidad de Mutación]
    CLASS [ Una de WARRIOR, ARCHER, DEFENDER, SPY ]
    T [Temperatura de Boltzmann]
    T2Thresh [Threshold de Torneos 2]
    a [Porcentaje de M1 para selección de Padres]
    b [Porcentaje de M3 para selección de individuos de la nueva generación]
    PQTY [Cantidad de Padres]

Hay dos ejemplos, "solver.config" y "solver.config2" 

Operadores Genéticos
CROSSING-OVER (Cruce):
    SINGLE-POINT (Cruce de un punto)
    TWO-POINT (Cruce de dos puntos)
    ANNULAR (Cruce anular)
    UNIFORM (Cruce Uniforme)
MUTATION (Mutación):
    GEN (Gen)
    LIM-MULTIGEN (Multigen Limitado)
    UNIFORM-MULTIGEN (Multigen Uniforme)
    COMPLETE (Completa)
SELECTION (Selección):
    ELITE (Elite)
    R-WHEEL (Ruleta)
    UNIV (Universal)
    BOLTZMANN (Boltzmann)
    TOURNAMENTS-1 (Torneos 1)
    TOURNAMENTS-2 (Torneos 2)
    RANKING (Ranking)
IMPLEMENTATION (Implementación):
    FILL-ALL
    FILL-PARENT
STOP-CRITERION (Criterio de finalización):
    TIME (Tiempo)
    GENERATIONS (Generación)
    ACCEPTABLE (Aceptable)
    STRUCT (Estructura)
    CONTENT (Contenido)