llantas=int(input("digite cantidad de llantas: "))
#escribe cuantas llantas compro 
if llantas<5:
    precio_llanta = 300
    total = precio_llanta * llantas
    print(f"si su cantidad de llantas {llantas} es menor que 5 el precio es: {precio_llanta} el total es: {total} ")
    # describe que si la cantidad de llantas y el precio de ellas definiendo asi el total a pagar
elif 5<=llantas<=10:
    precio_llanta = 250
    total = precio_llanta * llantas
    print(f"si su cantidad de llantas {llantas} son de 5 a 10 el precio es: {precio_llanta} el total es: {total} ")
     # describe que si la cantidad de llantas y el precio de ellas definiendo asi el total a pagar
elif llantas>10:
    precio_llanta = 200
    total= precio_llanta * llantas
    print(f"si su cantidad de llantas {llantas} son mas de 10 el  precio es: {precio_llanta} el total es: {total} ")
 # describe que si la cantidad de llantas y el precio de ellas definiendo asi el total a pagar 
