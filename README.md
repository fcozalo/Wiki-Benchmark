# Shellsort Benchmark

## Autor

Francisco Gonzalo García Kumul

---

## Análisis de complejidad

La complejidad de Shellsort depende de la secuencia de saltos utilizada. En este programa se usa una secuencia sencilla, donde el salto se divide entre 2 en cada repetición:

n/2, n/4, n/8, ..., 1

### Complejidad temporal

| Caso | Complejidad aproximada |
|---|---|
| Mejor caso | O(n log n) |
| Caso promedio | Depende de la secuencia de saltos |
| Peor caso | O(n²) |

En el peor caso, Shellsort puede llegar a tener una complejidad de O(n²). Sin embargo, en la práctica suele ser más rápido que Insertion Sort, porque Shellsort primero compara elementos separados por saltos grandes y después va reduciendo esos saltos hasta terminar con comparaciones más cercanas.

Esto permite que los números se acerquen más rápido a su posición correcta antes de hacer el ordenamiento final.

### Complejidad espacial

| Tipo | Complejidad |
|---|---|
| Espacial | O(1) |

La complejidad espacial es O(1), porque el algoritmo ordena los datos dentro de la misma lista y no necesita crear otra lista grande adicional.

---

## Casos de uso

Shellsort es mejor usarlo cuando se necesita un algoritmo de ordenamiento sencillo, pero más eficiente que Insertion Sort.

Es recomendable usar Shellsort en estos casos:

- Cuando se trabaja con listas pequeñas o medianas.
- Cuando se quiere mejorar el rendimiento del ordenamiento por inserción.
- Cuando se necesita ordenar datos usando poca memoria adicional.
- Cuando se busca un algoritmo fácil de implementar y entender.
- Cuando no es necesario que el algoritmo sea estable.

Shellsort puede funcionar bien cuando los datos no son extremadamente grandes y se quiere un método práctico para ordenarlos.

No es la mejor opción cuando se busca el máximo rendimiento en cantidades muy grandes de datos, ya que algoritmos como QuickSort, MergeSort o TimSort suelen tener mejor rendimiento en esos casos.

---

## Comparativa teórica contra otro método

En esta comparación se toma como referencia el algoritmo Insertion Sort, ya que Shellsort puede considerarse una mejora de este método.

### Insertion Sort

Insertion Sort ordena los datos comparando elementos cercanos y moviéndolos poco a poco hasta colocarlos en su posición correcta.

Su principal desventaja es que, si un número está muy lejos de donde debería estar, necesita muchos movimientos para llegar a su lugar.

Su complejidad promedio y peor caso es O(n²).

### Shellsort

Shellsort mejora esta idea utilizando saltos o gaps.

En lugar de comparar únicamente elementos vecinos, Shellsort compara primero elementos que están separados por una distancia mayor. Después reduce esa distancia hasta llegar a 1.

Cuando el salto llega a 1, el algoritmo funciona parecido a Insertion Sort, pero la lista ya está parcialmente ordenada, por lo que el proceso final suele ser más rápido.

| Algoritmo | Ventaja | Desventaja |
|---|---|---|
| Insertion Sort | Es fácil de entender e implementar | Es lento con listas grandes |
| Shellsort | Es más rápido que Insertion Sort en muchos casos | Su rendimiento depende de la secuencia de saltos |
