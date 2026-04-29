# Shellsort Benchmark

## Autor

- Francisco García

---

## Descripción del proyecto

Este proyecto implementa el algoritmo de ordenamiento **Shellsort** en Python.

El programa lee un archivo llamado `datos.txt`, ordena los números usando Shellsort, mide el tiempo de ejecución en milisegundos y guarda el resultado en un archivo llamado `datos_ordenados.txt`.

También permite elegir si los números se ordenan:

1. De menor a mayor.
2. De mayor a menor.

---

## Análisis de complejidad

La complejidad de Shellsort depende de la secuencia de saltos utilizada.

En este programa se utiliza una secuencia sencilla, donde el salto se divide entre 2 en cada vuelta:

```text
n/2, n/4, n/8, ..., 1
