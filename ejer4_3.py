num = int(input("Escriba un numero entero: "))

if num > 0:
    copia_numero = num
    contador_cifra = 0
    suma_cifra = 0
    while copia_numero > 0:
        cifra = copia_numero % 10
        copia_numero = copia_numero // 10
        suma_cifra = suma_cifra + cifra
        contador_cifra = contador_cifra + 1
    print("La cantidad de cifras del numero", num, "es", contador_cifra)
    print("La sumatoria de las cifras es", suma_cifra)
else:
    print("No es un numero positivo")
