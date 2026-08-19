# Informe de la Actividad 03 — Desarrollo seguro

**Fecha:** 18/08/2026  
**Actividad:** Script Python con validaciones y revisión con IA  
**Herramientas:** Python, biblioteca estándar y Codex  
**Versión del informe:** 1.0

## 1. Resumen

Se desarrolló un script de línea de comandos llamado `validar.py` que recibe un correo electrónico y un teléfono uruguayo, valida ambos datos y guarda los registros aceptados en un archivo CSV. El trabajo aplicó controles de validación de entradas, manejo seguro de errores, ausencia de secretos en el código y protección de los datos exportados.

La primera versión fue revisada por Codex desde la perspectiva de seguridad. La revisión identificó un riesgo de inyección de fórmulas en archivos CSV. El hallazgo fue corregido en la versión 2 y su mitigación se comprobó mediante una prueba específica.

## 2. Objetivo y alcance

El objetivo fue construir un script seguro que:

- recibiera un correo y un teléfono mediante argumentos de línea de comandos;
- validara completamente el formato de ambas entradas;
- rechazara datos inválidos antes de almacenarlos;
- guardara datos válidos en un archivo CSV;
- manejara errores sin revelar rutas, trazas u otros detalles internos;
- no incluyera contraseñas, claves ni tokens en el código;
- fuera revisado por una IA y corregido a partir de sus hallazgos.

El alcance se limitó al script local, su archivo CSV y pruebas manuales con entradas representativas. No se comprobó que una dirección de correo exista realmente ni que un teléfono esté asignado a una persona.

## 3. Marco de referencia

La actividad se realizó aplicando principios de desarrollo seguro descritos en la consigna y asociados con OWASP Secure Coding: no confiar en entradas externas, validar antes de procesar, reducir la exposición de información en errores y evitar secretos en el código fuente. También se consideró el dominio GH/Gestión de activos del Marco de Ciberseguridad de AGESIC indicado como referencia de la actividad.

## 4. Descripción de la solución

El script utiliza únicamente módulos de la biblioteca estándar de Python:

- `argparse` para definir y recibir los argumentos `--email` y `--telefono`;
- `re` para validar los formatos mediante expresiones regulares;
- `csv` para escribir registros con el tratamiento correcto de campos;
- `pathlib` para establecer la ubicación de `datos.csv` junto al script.

El flujo implementado es el siguiente:

1. Recibir los argumentos obligatorios desde la terminal.
2. Eliminar espacios externos con `strip()`.
3. Validar completamente el correo y el teléfono.
4. Rechazar las entradas inválidas con mensajes comprensibles.
5. Proteger los campos frente a fórmulas CSV.
6. Guardar los datos válidos en modo anexado, conservando registros anteriores.
7. Manejar los errores de archivo mediante un mensaje genérico.

## 5. Revisión de seguridad

### 5.1 Controles correctos en la versión 1

- El correo y el teléfono se validaban antes de su almacenamiento.
- Las expresiones utilizaban `fullmatch()`, por lo que debía coincidir la entrada completa.
- El programa no ejecutaba comandos del sistema ni construía consultas.
- No había claves, contraseñas, tokens ni otros secretos incorporados en el código.
- Los errores de escritura no mostraban rutas, excepciones ni trazas internas.
- La ruta de salida era fija y no estaba controlada por el usuario.

### 5.2 Hallazgo identificado

| ID | Hallazgo | Criticidad | Estado |
|---|---|---|---|
| H-01 | Posible inyección de fórmulas al abrir el CSV en una hoja de cálculo | Media | Cerrado |

La expresión regular del correo permitía valores que comenzaran con caracteres como `=`, `+` o `-`. Aunque estos valores podían cumplir el formato definido, una hoja de cálculo podría interpretarlos como fórmulas al abrir el CSV. Esto podía provocar la evaluación de contenido que debía tratarse únicamente como texto.

## 6. Corrección aplicada

En la versión 2 se añadió la función `proteger_celda_csv()`. Antes de escribir cada campo, la función comprueba si el valor comienza con `=`, `+`, `-`, `@`, tabulación o retorno de carro. Si detecta uno de esos caracteres, antepone un apóstrofo para indicar a las hojas de cálculo que el valor es texto literal.

La corrección se aplicó en el punto de salida, inmediatamente antes de escribir la fila. Esta decisión mantiene separadas la validación del formato de entrada y la protección necesaria para el contexto CSV.

## 7. Pruebas y resultados

| Prueba | Entrada | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| Datos válidos | `diego@ejemplo.com`, `099123456` | Guardar el registro | Correcto |
| Correo inválido | `correo-invalido`, `099123456` | Rechazar el correo | Correcto |
| Teléfono inválido | `diego@ejemplo.com`, `123` | Rechazar el teléfono | Correcto |
| Posible fórmula CSV | `=2+2@ejemplo.com`, `099123456` | Guardar el correo como texto protegido | Correcto: `'=2+2@ejemplo.com` |

Las pruebas inválidas produjeron mensajes controlados y no fueron guardadas. La prueba asociada al hallazgo confirmó que la versión 2 añadió la protección prevista.

## 8. Evidencias

- `EVI-2026-08-18-01-revision-IA.png`: revisión de seguridad realizada con Codex.
- `EVI-2026-08-18-02-codigo-v1.py`: código anterior a la corrección.
- `EVI-2026-08-18-03-codigo-v2.py`: código posterior a la corrección.
- `EVI-2026-08-18-04-pruebas.png`: ejecución de pruebas válidas, inválidas y de seguridad.

## 9. Limitaciones y mejoras futuras

- Las pruebas realizadas fueron manuales; podrían transformarse en pruebas automatizadas con `unittest`.
- La validación comprueba el formato, pero no confirma la existencia real del correo ni la asignación del teléfono.
- El CSV contiene datos personales en texto plano; en un entorno real deberían definirse controles de acceso, conservación y eliminación.
- La protección frente a fórmulas debe revisarse según la aplicación que consuma el CSV, porque distintos programas pueden interpretar los campos de manera diferente.
- Podría incorporarse un registro técnico controlado para diagnóstico, separado de los mensajes mostrados al usuario y sin incluir datos sensibles.

## 10. Conclusión

La actividad demostró que el desarrollo seguro debe considerarse desde el diseño. Validar entradas es necesario, pero no suficiente: también se debe analizar cómo se utilizarán y almacenarán los datos. La revisión permitió detectar que un valor formalmente válido podía resultar peligroso en el contexto de una hoja de cálculo.

La versión 2 cumple los objetivos de la actividad: valida correo y teléfono, rechaza entradas incorrectas, evita secretos, maneja errores sin revelar información interna, protege la salida CSV y conserva evidencias de la revisión y la corrección. El hallazgo de criticidad media quedó mitigado y verificado.

## 11. Reflexión sobre el uso de IA

La IA fue útil para revisar el código desde una perspectiva diferente y detectar un riesgo que no estaba limitado a la expresión regular, sino al uso posterior del archivo CSV. Sin embargo, no debe considerarse una garantía de seguridad. Sus sugerencias requieren verificación, pruebas y análisis del contexto real.

Una IA podría omitir problemas relacionados con permisos del sistema, configuraciones del entorno, concurrencia, protección real de datos personales o comportamientos particulares de otras aplicaciones. También puede producir falsos positivos o recomendar controles incompletos. Por eso, la decisión final debe apoyarse en criterio humano, pruebas reproducibles y herramientas especializadas.
