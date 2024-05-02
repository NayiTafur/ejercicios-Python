promedio=int(input("digite su promedio: "))
#escribir su promedio 
pension=int(input(" digite el valor de la pension: "))
if promedio>=9 :
   descuento = 0.3 * pension
   total = pension-descuento
   print(f" si el promedio{promedio} es mayor o igual a 9 obtendra un descuento {descuento} del 30% sobre la pension {total}: ")
   #describe el  descuento que obtuvo la persona segun su descuento del 30% dependiendo de promedio si es mayo o igual a 9 definiendo el total de la pension
elif promedio<9:
     iva=0.1+pension  
     total=iva+pension
     print(f" si el promedio {promedio} es menor que 9 debera pagar la pension {pension} con el iva {iva}: ")
    #describe el su promedio que si es menor a 9 debera pagar su pension junto con el iva 
