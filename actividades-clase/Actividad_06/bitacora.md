# Bitácora — Actividad 06

## Registro de trabajo

| Fecha | Actividad realizada | Resultado / observaciones |
|---|---|---|
| 25/08/2026 | Instalación de `pip-audit` | Se instaló correctamente la versión 2.10.1 en el entorno virtual de la Actividad 4. |
| 25/08/2026 | Auditoría inicial | No se encontraron vulnerabilidades conocidas. Evidencia: `EVI-2026-08-25-01-pipaudit-antes.txt`. |
| 25/08/2026 | Revisión de dependencias desactualizadas | No se encontraron paquetes desactualizados; no fue necesario actualizar dependencias. |
| 25/08/2026 | Auditoría posterior | Se repitió la auditoría y no se encontraron vulnerabilidades conocidas. Evidencia: `EVI-2026-08-25-02-pipaudit-despues.txt`. |
| 25/08/2026 | Reporte estructurado | Se generó el reporte JSON: `EVI-2026-08-25-03-audit.json`. |

## Conclusión provisional

La auditoría inicial y la posterior no detectaron vulnerabilidades conocidas. Como tampoco había dependencias desactualizadas, no se realizó ninguna actualización y se conservaron las versiones instaladas.

## Interpretación de CVE de referencia

Se analizó el CVE-2023-43804 de `urllib3` como ejemplo preventivo, ya que la auditoría del proyecto no reportó CVEs.

- **Descripción:** una aplicación podía enviar accidentalmente el encabezado `Cookie` a otro origen cuando seguía redirecciones HTTP, exponiendo información sensible.
- **Severidad:** alta según NVD, con CVSS 3.1 de 8.1. La explotación requiere que la aplicación permita que un usuario con privilegios configure el encabezado y que se sigan redirecciones.
- **Versiones afectadas:** `urllib3 < 1.26.17` y `urllib3 >= 2.0.0, < 2.0.6`.
- **Mitigación:** actualizar a `urllib3 1.26.17`, `2.0.5` o una versión posterior compatible. El proyecto utiliza `urllib3 2.7.0`, por lo que no está afectado por este CVE.
- **Clasificación:** caso de referencia preventiva; no constituye un hallazgo de la auditoría realizada.

Fuente consultada: [NVD — CVE-2023-43804](https://nvd.nist.gov/vuln/detail/CVE-2023-43804).

## Evidencias del análisis del CVE

- `EVI-2026-08-25-04-cve-descripcion.png`: descripción de la vulnerabilidad.
- `EVI-2026-08-25-05-cve-severidad.png`: métricas CVSS 3.1 y severidad alta.
