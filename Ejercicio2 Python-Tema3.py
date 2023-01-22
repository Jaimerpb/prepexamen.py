import os
def compareTriplets(a, b):
    points_a = 0
    points_b = 0
    for i in range(3):
        if a[i] > b[i]:
            points_a += 1
        elif a[i] < b[i]:
            points_b += 1
    return [points_a, points_b]

#Programa principal para ejecutarl la funcion comparetriplets utilizando archivos de entrada y salida 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    
    fptr.close()

#En el programa principal, se utiliza fptr para abrir un archivo de salida en la ruta especificada por la variable de entorno OUTPUT_PATH. Luego, se utiliza la función built-in input() para solicitar al revisor que ingrese las calificaciones de Lucía y Carlos. 
# Se utiliza list(map(int, input().rstrip().split())) para convertir las calificaciones ingresadas en una lista de números enteros.
#Luego, se llama a la función compareTriplets con las calificaciones de Lucía y Carlos como argumentos y se guarda el resultado en una variable llamada result