# Actividad 06 — Auditoría de dependencias

**Tema:** Vulnerabilidades en dependencias: `pip-audit` y CVEs  
**Institución:** Banco Ficticio del Uruguay  
**Responsable:** Estudiante RSI  
**Fecha:** 25/08/2026  
**Clasificación:** Confidencial — uso académico

## 1. Resumen ejecutivo

Se auditó el entorno virtual utilizado por la API desarrollada en la Actividad 4 mediante `pip-audit 2.10.1`. La herramienta comparó las dependencias Python instaladas con bases de datos de vulnerabilidades conocidas.

La auditoría inicial y la auditoría posterior no reportaron vulnerabilidades conocidas. La revisión de versiones tampoco identificó paquetes desactualizados, por lo que no fue necesario modificar dependencias. Se generó un reporte estructurado en JSON y se conservaron evidencias del antes, después y del análisis de un CVE de referencia.

## 2. Marco de referencia

La actividad se relaciona con la gestión de vulnerabilidades y dependencias, incluyendo GR.4 y GA.1 del Marco Agesic, y con los conceptos de CVE, CVSS y cadena de suministro de software.

## 3. Alcance y metodología

- **Alcance:** dependencias Python instaladas en el entorno virtual de la API de la Actividad 4.
- **Herramienta:** `pip-audit 2.10.1`.
- **Método:** instalación de la herramienta, auditoría inicial, revisión de paquetes desactualizados, auditoría posterior y generación de reporte JSON.
- **Periodo:** 25/08/2026.

## 4. Resultados

| Control / objetivo | Resultado |
|---|---|
| Instalar y ejecutar `pip-audit` | Logrado |
| Auditar las dependencias | Logrado; no se encontraron vulnerabilidades conocidas |
| Revisar actualizaciones disponibles | Logrado; no había paquetes desactualizados |
| Actualizar de forma segura y re-auditar | No fue necesario actualizar; la re-auditoría fue limpia |
| Generar reporte JSON | Logrado |
| Documentar gestión de vulnerabilidades | Logrado |

## 5. CVE de referencia analizado

Se analizó el **CVE-2023-43804** de `urllib3` como caso preventivo, no como hallazgo del proyecto.

La vulnerabilidad podía provocar que el encabezado `Cookie` se filtrara a otro origen cuando una aplicación seguía redirecciones HTTP. NVD registra una puntuación CVSS 3.1 de **8.1, severidad alta**. Las versiones afectadas son `urllib3 < 1.26.17` y `urllib3 >= 2.0.0, < 2.0.6`. La mitigación consiste en actualizar a una versión corregida.

El proyecto utiliza `urllib3 2.7.0`, por lo que queda fuera de los rangos afectados. Fuente: [NVD — CVE-2023-43804](https://nvd.nist.gov/vuln/detail/CVE-2023-43804).

## 6. Riesgos y tratamiento

| ID | Riesgo | Probabilidad | Impacto | Nivel | Tratamiento |
|---|---|---:|---:|---:|---|
| R-01 | Incorporar en el futuro una dependencia vulnerable sin detectarla | Media | Alto | Alto | Mitigado mediante auditorías periódicas y CI |
| R-02 | Actualizar una dependencia y romper compatibilidad | Media | Medio | Medio | En plan: probar en entorno aislado y revisar cambios |

No se identificaron vulnerabilidades activas en la auditoría realizada.

## 7. Política propuesta de gestión de dependencias

1. Ejecutar `pip-audit` antes de cada entrega y al menos una vez por semana en desarrollo.
2. Ejecutarlo automáticamente en el pipeline de integración continua.
3. Mantener las dependencias declaradas y sus versiones congeladas en un archivo de requisitos.
4. Clasificar cada hallazgo por severidad y registrar CVE, paquete, versión afectada y corrección.
5. Actualizar primero en un entorno aislado, ejecutar pruebas de la API y revisar las notas de versión.
6. No promover cambios a producción sin una re-auditoría limpia y aprobación del responsable de seguridad.
7. Conservar los reportes y evidencias para permitir trazabilidad y seguimiento.

## 8. Evidencias

- `EVI-2026-08-25-01-pipaudit-antes.txt`: auditoría inicial.
- `EVI-2026-08-25-02-pipaudit-despues.txt`: auditoría posterior.
- `EVI-2026-08-25-03-audit.json`: reporte estructurado.
- `EVI-2026-08-25-04-cve-descripcion.png`: descripción del CVE.
- `EVI-2026-08-25-05-cve-severidad.png`: métricas y severidad CVSS.

## 9. Reflexión sobre el uso de IA

Las dependencias representan un riesgo heredado porque el proyecto incorpora código desarrollado y mantenido por terceros. Aunque la aplicación propia no contenga errores conocidos, una biblioteca vulnerable puede afectar la confidencialidad, integridad o disponibilidad del sistema. En un equipo de desarrollo, la revisión puede automatizarse integrando `pip-audit` en CI, generando reportes ante cada cambio y estableciendo responsables y plazos para corregir los hallazgos.

## 10. Conclusión

La actividad fue completada satisfactoriamente. El entorno auditado no presenta vulnerabilidades conocidas ni dependencias pendientes de actualización. Se dejó evidencia reproducible del análisis y una política básica para mantener el control de dependencias en el futuro.
