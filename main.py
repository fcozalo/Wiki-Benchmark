import time
import os


def leer_numeros(ruta_archivo):
    numeros = []

    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

            contenido = contenido.replace(",", " ")
            contenido = contenido.replace(";", " ")

            partes = contenido.split()

            for dato in partes:
                numeros.append(int(dato))

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
        print("Ruta buscada:", ruta_archivo)
        return []

    except ValueError:
        print("Error: El archivo contiene datos que no son números enteros.")
        return []

    return numeros


def shellsort(lista):
    n = len(lista)
    salto = n // 2

    while salto > 0:
        for i in range(salto, n):
            temporal = lista[i]
            j = i

            while j >= salto and lista[j - salto] > temporal:
                lista[j] = lista[j - salto]
                j = j - salto

            lista[j] = temporal

        salto = salto // 2

    return lista


def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False

    return True


def guardar_resultado(ruta_archivo, lista):
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        for numero in lista:
            archivo.write(str(numero) + "\n")


def main():
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))

    ruta_datos = os.path.join(carpeta_actual, "datos.txt")
    ruta_salida = os.path.join(carpeta_actual, "datos_ordenados.txt")

    print("Carpeta del programa:", carpeta_actual)
    print("Buscando archivo en:", ruta_datos)

    numeros = leer_numeros(ruta_datos)

    if len(numeros) == 0:
        print("No hay datos para ordenar.")
        return

    print("Cantidad de números leídos:", len(numeros))

    inicio = time.perf_counter()

    shellsort(numeros)

    fin = time.perf_counter()

    tiempo_ms = (fin - inicio) * 1000

    print("Ordenamiento terminado.")
    print("Tiempo de ejecución:", round(tiempo_ms, 4), "ms")

    if esta_ordenada(numeros):
        print("Verificación: La lista está ordenada correctamente.")
    else:
        print("Verificación: La lista NO está ordenada correctamente.")

    guardar_resultado(ruta_salida, numeros)
    print("Resultado guardado en:", ruta_salida)


main()