# Benchmark de Algoritmo de Ordenamiento: Shellsort


## Descripción del proyecto

Este proyecto implementa el algoritmo de ordenamiento **Shellsort** en Python.  
El programa lee un archivo llamado `datos.txt`, el cual contiene números enteros, los ordena y mide el tiempo que tarda el algoritmo en realizar el ordenamiento.

El objetivo principal es analizar el comportamiento del algoritmo con una cantidad grande de datos, en este caso 50,000 números.

---

## ¿Qué es Shellsort?

Shellsort es un algoritmo de ordenamiento basado en el método de inserción directa, pero con una mejora importante: en lugar de comparar únicamente elementos vecinos, compara elementos separados por una distancia llamada `salto` o `gap`.

Al inicio, el algoritmo usa saltos grandes para mover rápidamente los elementos hacia una posición más cercana a la correcta. Después, el salto se va reduciendo hasta llegar a 1. Cuando el salto es 1, el algoritmo se comporta como un ordenamiento por inserción, pero la lista ya está parcialmente ordenada, por lo que el proceso suele ser más eficiente.

---

## Funcionamiento general

El algoritmo realiza los siguientes pasos:

1. Calcula un salto inicial, normalmente la mitad del tamaño de la lista.
2. Compara elementos separados por ese salto.
3. Si un elemento está en una posición incorrecta, lo mueve.
4. Reduce el salto a la mitad.
5. Repite el proceso hasta que el salto sea igual a 0.
