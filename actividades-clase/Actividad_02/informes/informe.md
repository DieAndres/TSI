# Informe — Actividad 02: Git y gestión de evidencias

## Resumen

En esta actividad se fortaleció la trazabilidad del proyecto mediante el uso de Git y una convención uniforme para registrar evidencias. Se verificó la identidad configurada, se adoptó una estrategia básica de ramas, se documentó la organización del repositorio y se ampliaron las exclusiones destinadas a evitar el versionado de archivos sensibles o locales.

## Organización del control de versiones

El repositorio utiliza `main` como rama principal estable y `dev` como rama de desarrollo. Durante la actividad se creó `dev`, se prepararon los cambios con `git add`, se generó un commit descriptivo y posteriormente se fusionó el trabajo con `main` mediante un avance rápido.

El commit creado fue:

```text
893ecd0 Actividad 02: agregar README y mejorar gitignore
```

Se estableció como regla realizar un commit por cada cambio lógico o actividad terminada. Los mensajes deben ser breves, descriptivos y representar con claridad el trabajo incluido.

## Documentación y protección de información

Se creó el archivo `README.md` en la raíz del repositorio para describir el curso, la estructura de las actividades y la convención de evidencias. También se actualizó `.gitignore` para excluir:

- Entornos virtuales de Python.
- Directorios `__pycache__` y archivos compilados.
- Archivos temporales del sistema.
- Archivos `.env` que podrían contener secretos.
- Configuración local de Visual Studio Code.

Estas exclusiones reducen el riesgo de incorporar al historial información sensible o archivos que dependen del entorno local.

## Convención de evidencias y carpetas

Cada actividad se organiza mediante las carpetas `codigo/`, `evidencias/` e `informes/`, junto con un archivo `bitacora.md`. Las evidencias utilizan el formato:

```text
EVI-YYYY-MM-DD-NN-descripcion.ext
```

Esta convención permite identificar la fecha, el orden y el contenido de cada archivo. La bitácora relaciona cada evidencia con su descripción y con el commit que demuestra.

## Evidencias generadas

- `EVI-2026-08-12-01-git-log.png`: historial gráfico del repositorio después del flujo de ramas.
- `EVI-2026-08-12-02-gitignore.png`: contenido actualizado del archivo `.gitignore`.

No se generó la evidencia `03-remoto` porque la creación de un repositorio remoto era opcional y no formó parte del alcance realizado.

## Decisiones tomadas

- Renombrar la rama principal de `master` a `main` para coincidir con la consigna.
- Utilizar `dev` para separar el trabajo en curso de la rama estable.
- Realizar commits por cambios lógicos con mensajes descriptivos.
- Evitar el versionado de secretos y configuraciones locales.
- Mantener las evidencias dentro de la carpeta correspondiente y registrarlas en la bitácora.

## Estado del repositorio al cierre

Al momento de redactar este informe, `main` y `dev` apuntan al commit `893ecd0`. El archivo `README.md` y la actualización de `.gitignore` ya forman parte del historial. La documentación y las evidencias de la Actividad 2 están preparadas para el commit de cierre de la actividad.

## Reflexión

La trazabilidad es fundamental para que un RSI pueda demostrar qué acciones realizó, cuándo se ejecutaron y con qué resultado. Versionar código, documentación y evidencias permite conservar un historial verificable, relacionar los resultados con cambios concretos y reducir la pérdida o dispersión de información. Esta práctica debe complementarse con controles que impidan incorporar secretos al repositorio.
