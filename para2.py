cant_term = int(input("Ingrese la cantidad de terminos a generar: "))
term = 1

if cant_term > 0:
    for cont_num in range(1, cant_term, 1):
        print(term)
        term = term + 2
    print(term)
