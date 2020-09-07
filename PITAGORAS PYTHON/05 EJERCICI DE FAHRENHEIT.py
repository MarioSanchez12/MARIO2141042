fahrenheit = int(input('Ingrese una temperatura en grados Fahrenheit: '))

celsius = (fahrenheit - 32) * 5.0/9.0

# Hacemos uso de la funcion str.format() para darle formato a nuestra respuesta
print('{} grados Fahrenheit son {} grados Celsius '.format(fahrenheit, celsius))
celsius = int(input('Ingrese la temperatura en grados Celsius: '))
fahrenheit = 9.0/5.0 * celsius +32
print('{} grados Celsius son {} grados Fahrenheit'.format(fahrenheit, celsius))