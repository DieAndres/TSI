import argparse


def main():
    parser = argparse.ArgumentParser(description="Muestra un saludo personalizado.")
    parser.add_argument("--nombre", required=True, help="Nombre de la persona a saludar")
    args = parser.parse_args()
    print(f"Hola, {args.nombre}!")


if __name__ == "__main__":
    main()
