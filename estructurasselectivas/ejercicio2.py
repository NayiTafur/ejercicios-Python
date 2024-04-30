cantidadZapatillas=float(input("digite cantidad de zapatillas compradas: "))
compra=(input("digite el valor de la compra"))



if cantidadZapatillas>= 3:
   descuento=compra*0.2
   compraTotal=compra-descuento
   print(f" El valor de la compra fue: {compra} y de acuerdo a la cantidad  tiene un descuento del 20%, el total de la compra es de:{compraTotal} ")
elif cantidadZapatillas<3:
   descuento=compra*0.1
   compraTotal=compra-descuento
   print(f" El valor de la compra fue: {compra} y de acuerdo a la cantidad  tiene un descuento del 10%, el total de la compra es de:{compraTotal} ")





