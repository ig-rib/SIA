# SIA - TP1 

## Ejecución

Ejecución de todos los algoritmos sobre un mapa

```bash
git clone https://bitbucket.org/itba/sia-2020-1c-02.git && cd TP1
chmod +x ./all.sh
./all.sh [MAP_NAME]
```
Las respuestas apareceran en la carpeta `test`, y las estadisticas en formato csv en `stats`

Otra opción es realizar la configuración deseada en `solver.config` y ejecutar

```bash
git clone https://bitbucket.org/itba/sia-2020-1c-02.git && cd TP1
chmod +x ./run.sh
./run.sh [MAP_NAME]
```
Por `stdout` se obtendrá lo solicitado

## Ejemplo

Ejecutar el algoritmo A* sobre el mapa `easy`.

Primero abrimos el archivo `solver.config` e indicamos con `1` el algoritmo deseado

```txt
DFS 0
BFS 0
IDDFS 1
GG 0
A* 0
IDA* 0
H 0
IDDFS-Step 50
PrintState 0
CornerSense 1
```
* En `IDDFS-Step` se debe indicar el incremento deseado para cada iteracion del algoritmo IDDFS
* El flag `PrintState` activa la impresion de nodos explorados 
* El flag `CornerSense` mejora la performance del algoritmo evitando que se exploren ramas no ganadoras. 

Ejecutamos de la siguiente manera

```bash
./run.sh easy
```

## Visual

Para visualizar el resultado de una manera animatda ejectuamos

Los archivos de test poseen el formato:
`[ALG]-[MAP_NAME].txt` o `H[0-2]-[ALG]-[MAP_NAME].txt` en el caso de los algoritmos de busqueda informados. 

```bash
chmod +x ./visual.sh
./visual.sh BFS-easy.txt
```

## Autores
* Ribas, Ignacio
* Marchetti, Gianfranco
