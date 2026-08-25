# Bitácora — Actividad 05

## Datos de la ejecución

- Fecha: 19/08/2026.
- Herramienta y versión: Bandit 1.9.4.
- Versión de Python: 3.14.7 (64 bits).
- Archivos analizados: `codigo/validar.py` y `codigo/app.py`.
- Objetivo del análisis: aplicar análisis estático de seguridad (SAST) al código Python de las actividades 03 y 04 para identificar patrones inseguros antes de ejecutar las aplicaciones.

## Resultado inicial de Bandit

La primera revisión de las copias originales de `validar.py` y `app.py` no identificó problemas de seguridad. Este resultado se conservó como línea base limpia en `EVI-2026-08-19-00-linea-base-limpia.txt` y `EVI-2026-08-19-00-linea-base-limpia.json`.

Para realizar el ejercicio práctico de identificación y corrección, se incorporó deliberadamente en `codigo/app.py` un endpoint de diagnóstico vulnerable. El endpoint recibe el parámetro `host` desde una solicitud HTTP, lo concatena en un comando `ping` y lo ejecuta mediante `subprocess.run()` con `shell=True`. La vulnerabilidad se introdujo únicamente con fines didácticos y permanece sin corregir en esta etapa.

Bandit informó los siguientes hallazgos:

- `B404` — uso del módulo `subprocess`: severidad baja, confianza alta y referencia `CWE-78`.
- `B602` — ejecución de un comando variable con `shell=True`: severidad alta, confianza alta y referencia `CWE-78`.

El resultado inicial suma un hallazgo bajo, ningún hallazgo medio y un hallazgo alto. La salida completa se guardó en `evidencias/EVI-2026-08-19-01-bandit-v1.txt`.
