"""Ejercicio N°3
Programa para calcular el precio de venta
de un producto"""

print("---------------------------------")
print("----------PRECIO DE VENTA--------")
print("---------------------------------")

# input

PC=int(input(" Digite el costo del producto "))

# prossecing

if PC<3000:
    Z=(PC * 0.15)
elif PC<=6000:
    Z=(500)
elif PC>6000:
    Z=(PC * 0.25)

P=(PC+Z)
# output

print("Sie le costo del producto es de: " + str(PC) + "entonce el precio de venta es: " + str(P))