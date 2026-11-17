vot_and = 0
vot_ios = 0

while True:
    cod = input("Ingrese el codigo del estudiante: ")
    print("PLATAFORMAS DISPONIBLES")
    print("[A] Android")
    print("[I] iOS")
    voto = input("Elija su opcion: ")
    if voto == "A" or voto == "a":
        vot_and = vot_and + 1
    elif voto == "I" or voto == "i":
        vot_ios = vot_ios + 1
    else:
        print("La opcion no es valida")
    seguir = input("Desea realizar un nuevo voto [S] [N]? ")
    if not (seguir == "S" or seguir == "s"):
        break

print("Votos por Android:", vot_and)
print("Votos por iOS:", vot_ios)

if vot_and > vot_ios:
    print("Android gano")
elif vot_and < vot_ios:
    print("iOS gano")
else:
    print("Hay empate")
