# Interpretación del hallazgo de Bandit

## Identificación

- **Hallazgo:** `B602 — subprocess_popen_with_shell_equals_true`.
- **Severidad:** alta.
- **Confianza:** alta.
- **Referencia:** `CWE-78 — Inyección de comandos del sistema operativo`.
- **Archivo:** `codigo/app.py`.

## Descripción del riesgo

El endpoint `/diagnostico/ping` recibe el parámetro `host` desde una solicitud HTTP y lo concatena directamente en un comando ejecutado mediante `subprocess.run()` con `shell=True`.

Esta combinación permite que el intérprete de comandos procese caracteres especiales incluidos por un usuario. Como consecuencia, un atacante podría intentar ejecutar instrucciones adicionales con los mismos permisos de la aplicación Flask.

## Impacto potencial en una institución financiera

- Lectura o modificación de archivos accesibles por la aplicación.
- Obtención de información del servidor y de la red interna.
- Ejecución de programas o comandos no autorizados.
- Interrupción o degradación del servicio.
- Uso del servidor comprometido para intentar acceder a otros sistemas.

## Corrección prevista

La corrección deberá eliminar `shell=True`, validar estrictamente el valor de `host` y proporcionar el comando y sus argumentos como una lista. En el momento de generar esta evidencia, el código vulnerable todavía no había sido corregido.

## Contexto del laboratorio

La vulnerabilidad fue introducida deliberadamente en una copia del código con fines didácticos. No pertenece a la versión original de la Actividad 04 y no debe utilizarse fuera de este laboratorio controlado.
