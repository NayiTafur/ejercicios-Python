genero=(input("digite el genero femenino si es mujer o masculino si es hombre: "))
#describe que genero eres 
edad=int(input("digite su edad: "))
#escribir su edad actual
if genero == "femenino":
    numPulsaciones= (220*edad) /10
    print(f"la persona de {genero}  de {edad},tiene {numPulsaciones}")
    #indica cuantos numeros de pulsaciones tiene la persona si es de genero fememenino
elif genero == "masculino":
    numPulsaciones= (210*edad) /10
    print(f"la persona de genero {genero} de edad {edad}, tiene {numPulsaciones}")
     #indica cuantos numeros de pulsaciones tiene la persona si es de genero masculino

   
 





