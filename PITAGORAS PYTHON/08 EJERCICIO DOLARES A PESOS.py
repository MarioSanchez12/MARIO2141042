def dolaresaPesos():
    try:
        cotizacion = float(input('Ingrese la cotización del dolar ($1 = ?ARS): '))
        pesos = float(input('Ingrese la cantidad de dólares: '))
        return pesos * cotizacion
    except ValueError:
        print('Solo se permiten números')
        return dolaresaPesos()
 
print('El valor en pesos es$ %.2f' % dolaresaPesos())