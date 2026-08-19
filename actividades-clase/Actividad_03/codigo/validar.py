import argparse
import csv
import re
from pathlib import Path

EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def validar_email(email: str) -> bool:
    return EMAIL_PATTERN.fullmatch(email) is not None


TELEFONO_PATTERN = re.compile(
    r"^(?:\+598(?:[249]\d{7})|(?:[24]\d{7}|09\d{7}))$"
)


def validar_telefono(telefono: str) -> bool:
    return TELEFONO_PATTERN.fullmatch(telefono) is not None


def crear_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Valida un correo y un teléfono uruguayo."
    )
    parser.add_argument(
        "--email",
        required=True,
        help="Correo electrónico que se desea validar.",
    )
    parser.add_argument(
        "--telefono",
        required=True,
        help="Teléfono uruguayo sin espacios ni guiones.",
    )
    return parser


ARCHIVO_SALIDA = Path(__file__).resolve().parent / "datos.csv"


CARACTERES_FORMULA_CSV = ("=", "+", "-", "@", "\t", "\r")


def proteger_celda_csv(valor: str) -> str:
    if valor.startswith(CARACTERES_FORMULA_CSV):
        return f"'{valor}"

    return valor


def guardar_datos(email: str, telefono: str) -> None:
    archivo_vacio = (
        not ARCHIVO_SALIDA.exists()
        or ARCHIVO_SALIDA.stat().st_size == 0
    )

    with ARCHIVO_SALIDA.open(
        mode="a",
        newline="",
        encoding="utf-8",
    ) as archivo:
        escritor = csv.writer(archivo)

        if archivo_vacio:
            escritor.writerow(["email", "telefono"])

        escritor.writerow([
            proteger_celda_csv(email),
            proteger_celda_csv(telefono),
        ])


def main() -> int:
    argumentos = crear_parser().parse_args()

    email = argumentos.email.strip()
    telefono = argumentos.telefono.strip()

    if not validar_email(email):
        print("Error: el correo electrónico no tiene un formato válido.")
        return 1

    if not validar_telefono(telefono):
        print("Error: el teléfono uruguayo no tiene un formato válido.")
        return 1

    try:
        guardar_datos(email, telefono)
    except OSError:
        print("Error: no fue posible guardar los datos.")
        return 1

    print("Los datos fueron validados y guardados correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
