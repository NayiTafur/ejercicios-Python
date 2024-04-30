valorCompra=float(input("digite el valor de la compra"))
promocion=input("inserte el color de la balota,rojo,verde,otro color")
if promocion == "rojo":
    descuento=0.15
    valorPagar=valorCompra-(valorCompra-descuento)
    print(f" El valor de la compra fue: {valorCompra} y de acuerdo a la balota roja tiene un descuento del 15%, el total de la compra es de:{valorPagar} ")

elif promocion == "Verde":
    descuento=0.2
    valorPagar=valorCompra-(valorCompra-descuento)
    print(f" El valor de la compra fue: {valorCompra} y de acuerdo a la balota verde tiene un descuento del 100%, el total de la compra es de:{valorPagar} ")

elif promocion == "otro color":
    descuento=0
    valorPagar=valorCompra-(valorCompra-descuento)
    print(f" El valor de la compra fue: {valorCompra} y de acuerdo a la balota de otro color tiene un descuento del 0%%, el total de la compra es de:{valorPagar} ")