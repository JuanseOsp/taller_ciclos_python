num = int(input("Escriba el número a analizar: "))

if num > 0:
    con_cifras = 0
    cop_num = num
    while True:
        cifra = cop_num % 10
        cop_num = cop_num // 10
        con_cifras = con_cifras + 1
        if cop_num == 0:
            break

    sum_cifra = 0
    cop_num = num
    while True:
        cifra = cop_num % 10
        cop_num = cop_num // 10
        sum_cifra = sum_cifra + cifra ** con_cifras
        if cop_num == 0:
            break

    if num == sum_cifra:
        print(num, "es un número de Armstrong.")
    else:
        print(num, "no es un número de Armstrong.")
else:
    print("Debe escribir un entero positivo.")
