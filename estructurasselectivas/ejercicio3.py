compra=int(input("digite el valor de la compra: "))
#escribir el precio de la compra
if compra>500000:
    empresa=compra*0.55
    banco=compra*0.3
    credito=compra*0.15
    intereses=credito+credito*0.2
    print(f"como la compra superó los 500000, la empresa invertirá {empresa}, pedirá prestado al banco {banco} y el resto lo pagará solicitando un crédito de {credito}, pagando un total de {intereses} con intereses por el mismo: ")
   # indica cuanto invierte la empresa,cuanto le pedira al banco y el precio de lo que tienen que poner la persona pagando una serie de intenreses que le brinden mostrando asi el valor total que debe de pagar de acuerdo a si supera los 500000
elif  compra <= 500000:
   capacidadEmpresa=compra*0.7 
   credito=compra*0.3
   intereses=credito*0.2
   print(f"Puesto que el monto total de la compra no supera los 500000, la empresa tendrá la capacidad de invertir {capacidadEmpresa}, y el restante {credito} lo pagará solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un {intereses} sobre la cantidad que se le pague a crédito: ")
    # indica cuanto invierte la empresa,cuanto le pedira al banco y el precio de lo que tienen que poner la persona pagando una serie de intenreses que le brinden mostrando asi el valor total que debe de pagar de acuerdo a si no supera los 500000