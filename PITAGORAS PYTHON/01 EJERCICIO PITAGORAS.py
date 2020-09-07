from math import sqrt
o = float(input("Escriba cateto o: "))
acm = float(input("Escriba cateto acm: "))
#hipotenusa
hipotenusa = sqrt(o*o)+(acm*acm)
#Resultado 
print("La hipotenusa es: {}".format(hipotenusa))