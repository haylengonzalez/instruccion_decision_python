"""Ejercicio 1:
Programa para ubicar las coordenadas de un
plano cartesiano""" 

print("---------------------------------------------")
print("-----------Lector de coordenadas-------------")
print("---------------------------------------------")

#input

X = int(input("digite la coordenada en X: "))
Y = int(input("digite la coordenada en Y: "))

# prossecing

if X==0 and Y==0:
    resultado=("El punto está sobre el origen")
elif X==0 and Y>0:
    resultado=("El punto está sobre el eje positivo de las abscisas")
elif X==0 and Y<0:
    resultado=("El punto está sobre el eje negativo de las abscisas")
elif X>0 and Y>0:
    resultado=("El punto está en el primer cuadrante")
elif X<0 and Y>0:
    resultado=("El punto está en el segundo cuadrante")
elif X<0 and Y<0:
    resultado=("El punto está en el tercer cuadrante")
elif X>0 and Y<0:
    resultado=("El punto está en el cuarto cudrante")
elif X>0 and Y==0:
    resultado=("El punto está sobre el eje positivo de las ordenadas")
elif X<0 and Y==0:
    resultado=("El punto está sobre el eje negativo de las ordenadas")

    # output

    print("Si x equivle a :" + str(X) + " y Y equivale a " + str(Y) + " entonces... " + str(resultado))