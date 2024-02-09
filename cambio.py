""" Construye un programa que, al recibir como datos el costo de un articulo vendido y la cantidad de dinero entregado
    por el cliente, calcule e imprima:

    1.- El cambio que se debe regresar al cliente, si el pago efectuado es mayor que el precio del producto.
    2.- ¿Qué pasa si el cliente paga exactamente lo que vale el producto?
    3.- La cantidad de dinero que falta por pagar, si el pago efectuado es menor que el precio del producto.    """

precio = float(input("Ingresa el precio del articulo: "))
pago = float(input("¿Cuánto ha pagado el cliente? "))

cambio = pago-precio
faltante = precio-pago

if (cambio < 0):
    print ("Falta dinero en el pago. El monto faltante es: ", faltante)

elif (cambio==0):
    print("El monto es exacro. No es necesario dar cambio.")

if (cambio>0):
    print("El cambio a dar es: ", cambio)


