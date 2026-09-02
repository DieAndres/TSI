# Bitácora — Actividad 07

## Herramientas y versiones

- Python: 3.14.7
- Semgrep: 1.174.0
- Bandit: 1.9.4

## Trabajo realizado

- Se instaló y verificó Semgrep.
- Se ejecutó el conjunto de reglas `p/security-audit`.
- Se creó `codigo/prueba_semgrep.py` para probar el uso inseguro de `eval()`.
- Se instaló y ejecutó Bandit sobre el mismo archivo.
- Se creó y probó la regla personalizada `reglas/no-eval.yaml`.
- Semgrep y Bandit detectaron el uso de `eval()` correctamente.

## Evidencias

- `EVI-2026-08-26-01-semgrep-audit.json`
- `EVI-2026-08-26-02-bandit-audit.txt`
- `EVI-2026-08-26-03-semgrep-regla.json`

## Prompts y uso de IA

Se utilizó Codex como tutor para comprender el propósito de Semgrep, interpretar los resultados, comparar Semgrep con Bandit y definir la regla personalizada. Cada ejecución fue realizada y verificada en la terminal.

## Reflexión

La actividad permitió comprender que Semgrep y Bandit pueden detectar patrones inseguros, aunque utilizan reglas y clasificaciones diferentes. También se comprobó que las reglas propias permiten adaptar el análisis a las necesidades de una institución. La principal dificultad fue configurar el acceso a los ejecutables y resolver problemas de codificación en las evidencias de texto.

## Resultados y comparación

- Semgrep detectó el uso de `eval()` mediante la regla pública `eval-detected`.
- Bandit detectó el mismo problema mediante la regla `B307`.
- Semgrep informó severidad bloqueante y CWE-95.
- Bandit informó severidad media, confianza alta y CWE-78.
- Se creó y probó la regla personalizada `no-eval-personalizado`.
- La regla propia detectó correctamente `eval()` con severidad `ERROR`.
- Evidencias generadas:
  - `EVI-2026-08-26-01-semgrep-audit.json`
  - `EVI-2026-08-26-02-bandit-audit.txt`
  - `EVI-2026-08-26-03-semgrep-regla.json`
