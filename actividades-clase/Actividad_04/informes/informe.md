# Informe — Actividad 04: API REST segura con Flask

## Resumen

Se desarrolló una API REST con Flask para simular la consulta de usuarios de una institución financiera. La API incorpora autenticación mediante token, validación de entradas, restricción de CORS, cabeceras de seguridad y limitación de solicitudes.

El funcionamiento y los controles se comprobaron con `curl`. Posteriormente, el código fue revisado tomando como referencia OWASP API Security Top 10 2023. La revisión identificó como hallazgo principal la ausencia inicial de límites de solicitudes, que fue corregida mediante Flask-Limiter y verificada con una respuesta `429 Too Many Requests`.

La API es adecuada para el entorno local de la actividad. Su publicación en producción requeriría autenticación individual, autorización por roles, HTTPS, registros de auditoría y un servidor WSGI de producción.

## Alcance y herramientas

- Período de ejecución: 17/08/2026 al 19/08/2026.
- Lenguaje: Python 3.14.7.
- Framework: Flask 3.1.3.
- Control de CORS: flask-cors 6.0.5.
- Limitación de solicitudes: Flask-Limiter 4.1.1.
- Cliente de pruebas: curl 8.7.1.
- Herramienta de asistencia y revisión: Codex.
- Marco de referencia: OWASP API Security Top 10 2023 y buenas prácticas de desarrollo seguro.

## Descripción de la API y sus endpoints

### `GET /health`

Endpoint público utilizado para comprobar la disponibilidad de la API. Devuelve `200 OK` con el siguiente cuerpo:

```json
{"estado": "ok"}
```

### `GET /usuarios`

Endpoint protegido que devuelve usuarios ficticios almacenados en memoria. El cliente debe enviar el token mediante:

```http
Authorization: Bearer <token>
```

Admite el parámetro opcional `rol`, cuyos únicos valores permitidos son `analista` y `auditor`. Por ejemplo:

```text
/usuarios?rol=analista
```

Sin el parámetro se devuelven todos los usuarios. Con un rol válido se filtra la respuesta. Un valor no permitido produce `400 Bad Request`.

## Controles de seguridad implementados

### Autenticación

El endpoint `/usuarios` exige un token Bearer. El token se obtiene desde la variable de entorno `API_TOKEN` y no se almacena en el código fuente. Una solicitud sin el token correcto recibe `401 Unauthorized`.

### Validación de entradas

El parámetro `rol` se normaliza eliminando espacios y convirtiéndolo a minúsculas. Posteriormente se compara con el conjunto cerrado de roles permitidos. Los valores no admitidos se rechazan antes de procesar la consulta.

### Exposición mínima de datos

Los registros ficticios contienen solamente `id`, `nombre` y `rol`. No se devuelven contraseñas, tokens ni otros datos sensibles.

### Control de CORS

CORS está restringido al origen conocido `http://localhost:3000`. Esta configuración controla qué aplicaciones web pueden leer las respuestas desde un navegador. CORS no sustituye la autenticación.

### Cabeceras de seguridad

Todas las respuestas incluyen:

- `X-Content-Type-Options: nosniff`.
- `X-Frame-Options: DENY`.
- `Content-Security-Policy: default-src 'none'`.
- `Cache-Control: no-store`.

### Limitación de solicitudes

Flask-Limiter aplica un límite general de 60 solicitudes por minuto y por dirección IP. Para `/usuarios` se configuró un límite más estricto de 10 solicitudes por minuto y por IP.

### Configuración local

El modo de depuración se encuentra deshabilitado. La aplicación escucha solamente en `127.0.0.1:5000`, reduciendo la exposición durante las pruebas locales.

## Pruebas realizadas con curl

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| `GET /health` | `200 OK` | `200 OK` y `{"estado":"ok"}` | Correcto |
| `/usuarios` sin token | `401 Unauthorized` | `401 Unauthorized` | Correcto |
| `/usuarios` con token correcto | `200 OK` | Lista de dos usuarios | Correcto |
| `/usuarios?rol=analista` | Un usuario analista | Se devolvió solamente Ana | Correcto |
| `/usuarios?rol=administrador` | `400 Bad Request` | Error y valores permitidos | Correcto |
| Solicitud 11 a `/usuarios` en un minuto | `429 Too Many Requests` | `429 Too Many Requests` | Correcto |

La respuesta de `/health` también permitió verificar la presencia de las cuatro cabeceras de seguridad y del origen permitido por CORS.

## Hallazgos de la revisión OWASP

### H-01 — API2:2023 Broken Authentication

- Criticidad: media.
- Hallazgo: se utiliza un único token compartido, sin identidad, vencimiento ni revocación individual.
- Impacto: quien obtenga el token puede presentarse como cliente autorizado.
- Tratamiento: aceptado para la práctica. Para producción se recomiendan tokens individuales de corta duración, rotación, revocación y mecanismos estándar de autenticación.

### H-02 — API4:2023 Unrestricted Resource Consumption

- Criticidad inicial: alta.
- Hallazgo: la versión inicial no limitaba la frecuencia de las solicitudes.
- Impacto: posibilidad de denegación de servicio y consumo excesivo de recursos.
- Corrección: implementación de Flask-Limiter.
- Validación: diez solicitudes devolvieron `200` y la solicitud 11 devolvió `429`.
- Estado: mitigado.

### H-03 — API5:2023 Broken Function Level Authorization

- Criticidad: media.
- Hallazgo: el token no identifica al usuario ni diferencia permisos; todos los clientes autorizados tienen el mismo acceso.
- Tratamiento: pendiente para producción. Se recomienda incorporar identidades y permisos por rol.

### H-04 — API8:2023 Security Misconfiguration

- Criticidad: media.
- Hallazgo: la API utiliza HTTP y el servidor de desarrollo de Flask.
- Tratamiento: aceptado para el entorno local. En producción deben utilizarse HTTPS, gestión segura de secretos y un servidor WSGI adecuado.

## Reflexión sobre el uso de IA

La IA permitió explicar los controles, revisar el código y relacionar los hallazgos con OWASP API Security Top 10. Las recomendaciones no se aceptaron solamente por haber sido generadas por IA: se comprobaron ejecutando la API y observando códigos HTTP, cabeceras y respuestas reales.

Una prueba con `curl` no detecta por sí sola fallos complejos de autorización, dependencias vulnerables, condiciones de carrera, filtraciones de credenciales, ataques distribuidos ni errores de infraestructura. Del mismo modo, que una API responda correctamente demuestra funcionalidad, pero no garantiza confidencialidad, integridad, disponibilidad ni control de acceso.

## Conclusión

Los objetivos de la actividad fueron alcanzados. Se construyó una API REST funcional con rutas, autenticación, validación, control de CORS, cabeceras de seguridad y limitación de solicitudes. Las pruebas confirmaron los comportamientos esperados y permitieron documentar tanto los controles aplicados como los riesgos residuales.

El resultado constituye una base segura para continuar las próximas actividades del curso, siempre que se mantenga su uso local. Los hallazgos pendientes deben resolverse antes de considerar una publicación en un entorno real.

## Evidencias

- `EVI-2026-08-17-01-app.py`: código de la API.
- `EVI-2026-08-17-02-curl-health.txt`: respuesta de `/health` y cabeceras.
- `EVI-2026-08-17-03-curl-token.txt`: accesos con y sin token y validación de parámetros.
- `EVI-2026-08-19-04-revision-api.md`: revisión OWASP.
- `EVI-2026-08-19-05-rate-limit.txt`: prueba de limitación de solicitudes.

## Referencias

- [OWASP API Security Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x00-header/)
- [API2:2023 — Broken Authentication](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/)
- [API4:2023 — Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
