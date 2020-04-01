# SIA - TP1 

## Ejecución

Ejecución de todos los algoritmos sobre un mapa

```bash
git clone https://bitbucket.org/itba/sia-2020-1c-02.git && cd TP1
chmod +x ./all.sh
./all.sh [MAP_NAME]
```
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
IDDFS 0
GG 0
A* 1
IDA* 0
H 0
PrintState 0
CornerSense 1
```
* El flag `PrintState` activa la impresion de nodos explorados 
* El flag `CornerSense` mejora la performance del algoritmo evitando que se exploren ramas no ganadoras. 

Ejecutamos de la siguiente manera

```bash
./run.sh easy
```

## Autores
* Ribas, Ignacio
* Marchetti, Gianfranco
