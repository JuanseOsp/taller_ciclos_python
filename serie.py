can_termi = int(input("Ingrese la cantidad de terminos a generar: "))
ter = 1
con_num = 0

while True:
    print(ter)
    ter = ter + 2
    con_num = con_num + 1
    if not con_num <= can_termi - 1:
        break
