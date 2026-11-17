can_estu = int(input("Ingrese la cantidad de estudiantes: "))
sum_not = 0
contador = 1
apro = 0
repro = 0

while contador <= can_estu:
    nota = float(input(f"Ingrese la nota del estudiante {contador}: "))
    sum_not = nota + sum_not
    contador = contador + 1
    if nota >= 3.0:
        apro = apro + 1
    else:
        repro = repro + 1

if can_estu > 0:
    prom = sum_not / can_estu
    print("La cantidad de estudiantes que reprobaron fueron:", repro)
    print("La cantidad de estudiantes que aprobaron fueron:", apro)
    print("El promedio del curso es de:", round(prom, 2))
else:
    print("No hay estudiantes para calcular el promedio")
