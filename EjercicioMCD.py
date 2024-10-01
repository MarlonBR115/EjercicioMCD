def obtener_divisores(numero: int) -> list[int]:
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores


def leer_numero_natural() -> int:
    while True:
        try:
            # Solicitar entrada del usuario
            numero = int(input("Ingrese un número natural: "))
            if numero < 1:
                raise ValueError("El número no es un número natural.")
            return numero
        except ValueError as e:
            print(f"Entrada no válida: {e}. Intente de nuevo.")


def main():
    print("Aplicación para calcular divisores de un número natural.")

    # Leer un número natural válido
    numero = leer_numero_natural()

    # Obtener y mostrar los divisores
    divisores = obtener_divisores(numero)
    print(f"Los divisores de {numero} son: {divisores}")


if __name__ == "__main__":
    main()
