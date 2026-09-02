# Informe — Actividad 07

## Resumen

Se realizó un análisis estático de seguridad sobre un archivo Python utilizando Semgrep y Bandit. Ambas herramientas detectaron el uso inseguro de `eval()`. Además, se creó y probó una regla personalizada de Semgrep con severidad alta, adaptada a las necesidades de la institución.

## Estructura del proyecto

- `codigo/`: contiene los scripts o archivos de código de la actividad.
- `evidencias/`: contiene las capturas y archivos que documentan el trabajo.
- `informes/`: contiene este informe.
- `bitacora.md`: registra el proceso, las decisiones y la reflexión.

## Desarrollo

Se instaló Semgrep y se ejecutó el conjunto de reglas `p/security-audit` sobre el código de prueba. Luego se instaló Bandit y se analizó el mismo archivo para comparar los resultados. Finalmente, se definió la regla propia `no-eval-personalizado` en formato YAML y se verificó que detectara correctamente la llamada a `eval()`.

## Metodología

Se utilizó Semgrep como herramienta de análisis estático de seguridad. Primero se ejecutó el conjunto de reglas `p/security-audit` sobre el código de prueba. Luego se analizó el mismo archivo con Bandit para comparar los resultados.

Finalmente, se creó una regla personalizada de Semgrep en `reglas/no-eval.yaml`. Esta regla busca cualquier llamada a `eval(...)`, informa un mensaje específico, utiliza severidad `ERROR` y relaciona el hallazgo con CWE-95.

## Resultados y comparación

Semgrep analizó dos archivos y encontró un uso inseguro de `eval()` en la línea 2 de `prueba_semgrep.py`, mediante la regla pública `python.lang.security.audit.eval-detected.eval-detected`. El hallazgo fue marcado como bloqueante y asociado con CWE-95.

Bandit analizó el mismo archivo y detectó el problema mediante la regla `B307:blacklist`. Lo clasificó con severidad media, confianza alta y CWE-78. La diferencia se debe a que cada herramienta utiliza sus propias reglas y criterios de clasificación.

La regla personalizada `no-eval-personalizado` también detectó correctamente `eval()`, con severidad `ERROR` y un mensaje adaptado al proyecto.

## Evidencias

- `EVI-2026-08-26-01-semgrep-audit.json`: análisis con las reglas públicas de seguridad de Semgrep.
- `EVI-2026-08-26-02-bandit-audit.txt`: análisis del mismo código con Bandit.
- `EVI-2026-08-26-03-semgrep-regla.json`: ejecución de la regla personalizada.

## Utilidad y recomendación

Las reglas propias permiten adaptar los controles de seguridad a las necesidades específicas de una organización. En un banco podrían utilizarse para prohibir funciones inseguras, detectar registros de datos sensibles o controlar el uso de APIs no autorizadas.

Se recomienda integrar Semgrep al flujo de desarrollo y ejecutarlo antes de cada `commit` y dentro del proceso de integración continua. Los hallazgos de severidad alta o bloqueante deberían corregirse antes de aprobar los cambios.

## Conclusión

La actividad permitió comprobar que Semgrep y Bandit detectan el uso inseguro de `eval()`, aunque pueden clasificarlo con diferentes niveles y referencias CWE. La regla personalizada demostró que el equipo puede definir controles específicos para sus necesidades.

Se recomienda mantener esta regla integrada al análisis automático del código y corregir cualquier uso de `eval()` antes de aprobar cambios.
