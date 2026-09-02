FILAS = 8
COLUMNAS = 8
VACIO = "○"
LLENO = "●"

cuadricula = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
seleccionadas = []


def mostrar_cuadricula():
    print("\n    " + " ".join(str(i).rjust(2) for i in range(1, COLUMNAS + 1)))
    for i, fila in enumerate(cuadricula, start=1):
        print(f"{str(i).rjust(2)}  " + "  ".join(fila))
    print()


def validar_coordenada(x, y):
    return 1 <= x <= COLUMNAS and 1 <= y <= FILAS


def seleccionar_circulo(x, y):
    if (x, y) in seleccionadas:
        print(f"La coordenada ({x},{y}) ya estaba seleccionada.")
        return
    cuadricula[y - 1][x - 1] = LLENO
    seleccionadas.append((x, y))
    print(f"Círculo en ({x},{y}) cambiado a relleno.")


def reiniciar():
    global cuadricula, seleccionadas
    cuadricula = [[VACIO for _ in range(COLUMNAS)] for _ in range(FILAS)]
    seleccionadas = []
    print("Cuadrícula reiniciada.")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingresa un número entero válido.")


def mostrar_menu():
    print("=" * 40)
    print("1. Ver cuadrícula")
    print("2. Seleccionar coordenada")
    print("3. Ver seleccionadas")
    print("4. Reiniciar")
    print("5. Salir")


def main():
    print(f"Cuadrícula de {FILAS}x{COLUMNAS}. Coordenadas de 1 a {COLUMNAS}.")
    mostrar_cuadricula()

    while True:
        mostrar_menu()
        opcion = input("Opción (1-5): ").strip()

        if opcion == "1":
            mostrar_cuadricula()

        elif opcion == "2":
            x = pedir_entero("X: ")
            y = pedir_entero("Y: ")
            if validar_coordenada(x, y):
                seleccionar_circulo(x, y)
                mostrar_cuadricula()
            else:
                print(f"Coordenada ({x},{y}) fuera de rango.")

        elif opcion == "3":
            if seleccionadas:
                print("Seleccionadas:", seleccionadas)
            else:
                print("Aún no hay coordenadas seleccionadas.")

        elif opcion == "4":
            reiniciar()
            mostrar_cuadricula()

        elif opcion == "5":
            print("Hasta pronto.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()