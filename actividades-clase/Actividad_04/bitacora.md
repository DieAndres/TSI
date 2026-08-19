# Bitácora — Actividad 04

## Período de trabajo

- Inicio: 17/08/2026.
- Finalización de las pruebas y revisión: 19/08/2026.
- Entorno: Windows, Python 3.14.7 y entorno virtual `.venv`.

## Herramientas y versiones

- Flask: 3.1.3.
- flask-cors: 6.0.5.
- Flask-Limiter: 4.1.1.
- curl: 8.7.1.
- Codex: herramienta de IA utilizada como tutor y para la revisión OWASP.

## Endpoints definidos

### `GET /health`

- Propósito: comprobar que la API está disponible.
- Autenticación: no requerida.
- Respuesta esperada: `200 OK` con `{"estado":"ok"}`.

### `GET /usuarios`

- Propósito: devolver usuarios ficticios almacenados en memoria.
- Autenticación: token enviado mediante `Authorization: Bearer <token>`.
- Parámetro opcional: `rol`.
- Valores admitidos para `rol`: `analista` y `auditor`.
- Sin token o con token incorrecto: `401 Unauthorized`.
- Rol no permitido: `400 Bad Request`.
- Solicitud autorizada: `200 OK`.
- Límite: 10 solicitudes por minuto y por dirección IP.

## Token de autenticación

Se utilizó un token de prueba proporcionado mediante la variable de entorno `API_TOKEN`. En PowerShell se definió temporalmente con:

```powershell
$env:API_TOKEN = "<token-de-prueba>"
```

El valor no se incorporó al código fuente ni a esta bitácora. La variable existe durante la sesión de la terminal y debe volver a definirse al abrir una sesión nueva.

## Controles de seguridad implementados

- Token separado del código mediante una variable de entorno.
- Protección de `/usuarios` mediante el encabezado `Authorization`.
- Validación y normalización del parámetro `rol`.
- Datos de respuesta limitados a `id`, `nombre` y `rol`.
- CORS restringido a `http://localhost:3000`.
- Cabecera `X-Content-Type-Options: nosniff`.
- Cabecera `X-Frame-Options: DENY`.
- Cabecera `Content-Security-Policy: default-src 'none'`.
- Cabecera `Cache-Control: no-store`.
- Modo de depuración deshabilitado.
- Límite general de 60 solicitudes por minuto y por IP.
- Límite específico de 10 solicitudes por minuto para `/usuarios`.

## Pruebas realizadas con curl

- `GET /health`: devolvió `200 OK` y las cabeceras de seguridad esperadas.
- `GET /usuarios` sin token: devolvió `401 Unauthorized`.
- `GET /usuarios` con token correcto: devolvió `200 OK` y los dos usuarios ficticios.
- `GET /usuarios?rol=analista`: devolvió solamente el usuario con rol `analista`.
- `GET /usuarios?rol=administrador`: devolvió `400 Bad Request` e informó los valores permitidos.
- Prueba de rate limiting: las primeras 10 solicitudes devolvieron `200` y la solicitud 11 devolvió `429 Too Many Requests`.

## Revisión OWASP API Security Top 10

### H-01 — Autenticación débil

- Categoría: API2:2023 — Broken Authentication.
- Criticidad: media.
- Hallazgo: se utiliza un único token compartido, sin identidad, vencimiento ni revocación individual.
- Tratamiento: aceptado para la práctica; para producción se recomiendan tokens individuales, de corta duración, revocables y asociados a roles.

### H-02 — Consumo de recursos sin límites

- Categoría: API4:2023 — Unrestricted Resource Consumption.
- Criticidad: alta.
- Hallazgo: la versión inicial no limitaba la cantidad de solicitudes.
- Tratamiento: mitigado mediante Flask-Limiter y verificado con una respuesta `429` en la solicitud 11.

### H-03 — Autorización sin roles reales

- Categoría: API5:2023 — Broken Function Level Authorization.
- Criticidad: media.
- Hallazgo: todos los clientes que conocen el token tienen el mismo nivel de acceso.
- Tratamiento: pendiente para producción; se recomienda incorporar identidad y permisos por rol.

### H-04 — Configuración solo apta para desarrollo

- Categoría: API8:2023 — Security Misconfiguration.
- Criticidad: media.
- Hallazgo: se utiliza HTTP y el servidor de desarrollo de Flask.
- Tratamiento: aceptado para ejecución local; para producción se requieren HTTPS y un servidor WSGI adecuado.

## Evidencias

- `EVI-2026-08-17-01-app.py`: copia del código de la API.
- `EVI-2026-08-17-02-curl-health.txt`: respuesta de `/health` con cabeceras.
- `EVI-2026-08-17-03-curl-token.txt`: respuestas sin token, con token y con parámetro inválido.
- `EVI-2026-08-19-04-revision-api.md`: revisión contra OWASP API Security Top 10.
- `EVI-2026-08-19-05-rate-limit.txt`: prueba del límite de solicitudes.

## Prompts y uso de IA

Codex se utilizó como tutor para explicar cada control, guiar la construcción de la API, interpretar errores de PowerShell y Git Bash, revisar el código contra OWASP API Security Top 10 y proponer la mitigación del consumo de recursos mediante rate limiting. Cada resultado se comprobó con pruebas locales antes de registrarlo.

## Reflexión

Una prueba con curl permite verificar respuestas, códigos HTTP, cabeceras y algunos controles de autenticación y validación. Sin embargo, no detecta por sí sola problemas complejos de autorización, condiciones de carrera, dependencias vulnerables, ataques distribuidos, filtraciones de credenciales ni errores de infraestructura.

Que una API funcione significa que responde según lo esperado, pero no demuestra que sea segura. Una API segura también debe proteger la identidad y los permisos, limitar el consumo de recursos, minimizar los datos expuestos, cifrar las comunicaciones, registrar eventos relevantes y utilizar una configuración apropiada para producción.
