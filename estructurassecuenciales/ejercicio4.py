sueldo=100000
comisiones=20000
cantidad=0
valor_comisiones=0
valor_total=0


nombre=str(input("digite el nombre del vendedor: "))
ventas=int(input("digite el valor de las ventas: "))
valor_comisiones=ventas*comisiones
valor_total=valor_comisiones+sueldo
print(f"el vendedor {nombre}, tiene un sueldo de {sueldo},durante el mes obtuvo una comision de {valor_comisiones} y el valor a pagar {valor_total}")
