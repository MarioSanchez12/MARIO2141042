contador = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Digite un numero entero (cero para terminar): "))

    if numero != 0:
        suma += numero
        contador += 1
if contador == 0:
    print("No digito ningun numero.")
else:       
    promedio = suma / contador

    print("El promedio de los {} numeros es igual a {}.".format(contador, promedio))