# Bitácora — Actividad 03: Desarrollo seguro

**Fecha:** 18/08/2026  
**Herramientas:** Python, biblioteca estándar y Codex  
**Objetivo:** desarrollar un script que valide un correo electrónico y un teléfono uruguayo, maneje errores sin revelar información interna y guarde únicamente datos válidos en un archivo CSV.

## Regla de seguridad aprendida

No se debe confiar en las entradas proporcionadas por el usuario. Los datos deben validarse antes de procesarlos o almacenarlos, los errores no deben exponer información interna y los valores exportados deben protegerse según el contexto donde serán utilizados.

## Versiones del código

### Versión 1

La primera versión validaba el correo y el teléfono mediante expresiones regulares, recibía los datos con `argparse`, manejaba errores de escritura mediante un mensaje genérico y almacenaba los registros válidos en `datos.csv`.

Evidencia: `EVI-2026-08-18-02-codigo-v1.py`.

### Revisión de seguridad con Codex

**Hallazgo H-01 — Inyección de fórmulas en CSV (criticidad media):** el correo podía comenzar con caracteres como `=`, `+` o `-`. Al abrir el CSV en una hoja de cálculo, estos valores podían interpretarse como fórmulas.

No se encontraron secretos en el código, ejecución de comandos del sistema ni mensajes de error que revelaran rutas o trazas internas.

Evidencia: `EVI-2026-08-18-01-revision-IA.png`.

### Versión 2

Se agregó `proteger_celda_csv()`, que antepone un apóstrofo a los valores que comienzan con caracteres asociados a fórmulas. La protección se aplica inmediatamente antes de escribir cada campo en el CSV.

Evidencia: `EVI-2026-08-18-03-codigo-v2.py`.

## Pruebas realizadas

| Caso | Correo | Teléfono | Resultado |
|---|---|---|---|
| Entrada válida | `diego@ejemplo.com` | `099123456` | Datos validados y guardados |
| Correo inválido | `correo-invalido` | `099123456` | Rechazado por formato de correo |
| Teléfono inválido | `diego@ejemplo.com` | `123` | Rechazado por formato de teléfono |
| Fórmula CSV | `=2+2@ejemplo.com` | `099123456` | Guardado como texto: `'=2+2@ejemplo.com` |

Se comprobó que las entradas inválidas no fueron almacenadas y que la versión 2 neutralizó el valor asociado con una posible fórmula CSV.

Evidencia: `EVI-2026-08-18-04-pruebas.png`.
