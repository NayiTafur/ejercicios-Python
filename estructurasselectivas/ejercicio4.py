valorCompra=float(input("digite el valor de la compra"))
# escribe el valor de la compra
promocion=input("inserte el color de la balota,rojo,verde,otro color")
#escribe el color que obtiene de la balota
if promocion == "rojo":
    descuento=0.15
    valorPagar=valorCompra-(valorCompra-descuento)
    print(f" El valor de la compra fue: {valorCompra} y de acuerdo a la balota roja tiene un descuento del 15%, el total de la compra es de:{valorPagar} ")
    #define el descuento que obtiene segun la balota roja  y indica que tiene un descuento del 30% y define el total a pagar

elif promocion == "Verde":
    descuento=0.2
    valorPagar=valorCompra-(valorCompra-descuento)
    print(f" El valor de la compra fue: {valorCompra} y de acuerdo a la balota verde tiene un descuento del 100%, el total de la compra es de:{valorPagar} ")
    #define el descuento que obtiene segun la balota ver  y indica que tiene un descuento del 20 y define el total a pagar

elif promocion == "otro color":
    descuento=0
    valorPagar=valorCompra-(valorCompra-descuento)
    print(f" El valor de la compra fue: {valorCompra} y de acuerdo a la balota de otro color tiene un descuento del 0%%, el total de la compra es de:{valorPagar} ")
    #define el descuento que obtiene segun la balota cualquier color indica que no tiene descuento y  define el total a pagar
