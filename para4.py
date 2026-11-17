print("Ingrese el valor maximo para x")
while True:
    valor_x = int(input())
    if not valor_x < 0:
        break

for x in range(0, valor_x + 1, 2):
    func = x ** 3 + x ** 2 - 5
    print("Para x =", x, " f(x) =", func)
