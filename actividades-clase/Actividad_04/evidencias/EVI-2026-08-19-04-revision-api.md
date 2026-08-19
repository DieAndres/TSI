# Revision de seguridad - OWASP API Security Top 10 2023

**API evaluada:** API REST desarrollada con Flask, con los endpoints `GET /health` y `GET /usuarios`.

**Fecha de revision:** 19/08/2026.

## H-01 - Autenticacion debil

- **Categoria:** API2:2023 - Broken Authentication.
- **Criticidad:** Media.
- **Descripcion:** La API utiliza un unico token compartido. El token no identifica usuarios, no tiene vencimiento y no puede revocarse individualmente.
- **Impacto:** Si el token se filtra, un atacante puede acceder a `/usuarios` y la API no puede diferenciarlo de un cliente legitimo.
- **Control actual:** El token se obtiene desde una variable de entorno y no esta escrito en el codigo fuente.
- **Recomendacion:** En produccion, utilizar autenticacion individual, tokens de corta duracion, rotacion, revocacion y autorizacion por roles.
- **Estado:** Aceptado para la practica; pendiente para produccion.

## H-02 - Consumo de recursos sin limites

- **Categoria:** API4:2023 - Unrestricted Resource Consumption.
- **Criticidad:** Alta.
- **Descripcion:** Inicialmente no existia un limite para la cantidad de solicitudes recibidas.
- **Impacto:** Un atacante podia automatizar solicitudes y provocar una denegacion de servicio o consumo excesivo de recursos.
- **Correccion aplicada:** Se instalo y configuro Flask-Limiter.
- **Control implementado:** Limite general de 60 solicitudes por minuto y limite de 10 solicitudes por minuto para `/usuarios`, ambos por direccion IP.
- **Prueba:** Las primeras 10 solicitudes devolvieron `200 OK`; la solicitud numero 11 devolvio `429 Too Many Requests`.
- **Estado:** Mitigado.

## H-03 - Autorizacion sin roles reales

- **Categoria:** API5:2023 - Broken Function Level Authorization.
- **Criticidad:** Media.
- **Descripcion:** El token solamente representa acceso permitido o denegado; no identifica al usuario ni contiene sus permisos.
- **Impacto:** Todos los clientes que conocen el token tienen el mismo nivel de acceso.
- **Recomendacion:** Incorporar identidad y roles dentro de un mecanismo de autenticacion y comprobar los permisos requeridos por cada endpoint.
- **Estado:** Pendiente para produccion.

## H-04 - Configuracion solo apta para desarrollo

- **Categoria:** API8:2023 - Security Misconfiguration.
- **Criticidad:** Media.
- **Descripcion:** La API utiliza HTTP y el servidor de desarrollo incluido con Flask.
- **Impacto:** En una red real, el token podria ser interceptado y el servidor no tendria las protecciones necesarias para produccion.
- **Controles actuales:** `debug=False`, CORS restringido, validacion de entradas y cabeceras de seguridad.
- **Recomendacion:** Publicar mediante HTTPS y utilizar un servidor WSGI de produccion.
- **Estado:** Aceptado unicamente para ejecucion local.

## Controles verificados

- Token almacenado fuera del codigo fuente.
- Endpoint `/usuarios` protegido mediante el encabezado `Authorization`.
- Validacion del parametro opcional `rol`.
- Exposicion minima de datos: `id`, `nombre` y `rol`.
- CORS restringido a `http://localhost:3000`.
- Cabeceras `X-Content-Type-Options`, `X-Frame-Options`, `Content-Security-Policy` y `Cache-Control`.
- Modo de depuracion deshabilitado.
- Rate limiting implementado y probado correctamente.

## Conclusion

La API cumple los objetivos educativos de autenticacion, validacion, control de CORS, cabeceras de seguridad y limitacion de solicitudes. Es adecuada para pruebas locales. Antes de utilizarla en produccion se requiere autenticacion individual, autorizacion por roles, HTTPS, registros de auditoria y un servidor WSGI de produccion.

## Referencias

- [OWASP API Security Top 10 2023](https://owasp.org/API-Security/editions/2023/en/0x00-header/)
- [API2:2023 - Broken Authentication](https://owasp.org/API-Security/editions/2023/en/0xa2-broken-authentication/)
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
