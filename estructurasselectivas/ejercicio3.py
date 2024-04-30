compra=int(input("digite el valor de la compra: "))
if compra>500000:
    empresa=compra*0.55
    banco=compra*0.3
    credito=compra*0.15
    intereses=credito+credito*0.2
    print(f"como la compra superó los 500000, la empresa invertirá {empresa}, pedirá prestado al banco {banco} y el resto lo pagará solicitando un crédito de {credito}, pagando un total de {intereses} con intereses por el mismo: ")
