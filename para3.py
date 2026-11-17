print("Ingrese la cantidad de numeros")
while True:
    cant_num = int(input())
    if not cant_num < 0:
        break

for num in range(1, cant_num + 1, 1):
    print(num, num * num, num + num * num)
