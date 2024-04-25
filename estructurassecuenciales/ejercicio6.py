estudiante=(input("digite el nombre del estudiante: "))
#escriba nombre de estudiante
promedio=float(input("digite el nota promedio de las actividas 30%: "))
#indica nota del promedio de actividades
proyecto_final=int(input("digite nota del proyecto final 50%: "))
#indica nota de  proyecto final
evaluacion=float(input("digite nota de las parciales 20%: "))
# indica nota de evaluacion
nota_final=(promedio*0.3)+(proyecto_final*0.5)+(evaluacion*0.2)
#calcula promedios de notas
print("la nota final del estudiante" , estudiante,"es:",nota_final)
#describe nota final