#declarar variables
descuento=0.8
valor_de_compra=int(input("indique el valor de la compra: "))

#descuento
descuento=valor_de_compra*descuento
valor=valor_de_compra-descuento
print(f"el valor de la compra es {valor_de_compra}, con un descuento de 20%, con un valor total de {valor}")