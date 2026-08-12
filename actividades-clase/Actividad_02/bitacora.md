# Bitácora — Actividad 02: Git y gestión de evidencias

## Identidad de Git

- Usuario: `DieAndres`
- Estado: identidad verificada correctamente.

## Convención de ramas y commits

- `main`: rama principal con trabajo estable.
- `dev`: rama utilizada para desarrollar y verificar cambios antes de integrarlos.
- Se realizará un commit por cada cambio lógico o actividad terminada.
- Los mensajes de commit serán breves, descriptivos y escritos en infinitivo.
- Flujo aplicado: crear `dev`, preparar cambios, hacer commit y fusionar con `main`.

## Registro de evidencias

| Evidencia | Fecha | Descripción | Commit relacionado |
|---|---|---|---|
| `EVI-2026-08-12-01-git-log.png` | 12/08/2026 | Historial gráfico de Git después de fusionar `dev` con `main`. | `893ecd0` |
| `EVI-2026-08-12-02-gitignore.png` | 12/08/2026 | Contenido del `.gitignore` con exclusiones para Python, secretos y VS Code. | `893ecd0` |

## Trabajo realizado

- Se verificó la identidad configurada en Git.
- Se renombró la rama principal de `master` a `main` para ajustarla a la convención de la actividad.
- Se creó la rama `dev` para trabajar de forma separada de la rama principal.
- Se creó `README.md` con la descripción y organización del repositorio.
- Se amplió `.gitignore` para excluir entornos virtuales, caché de Python, archivos `.env` y la configuración local de VS Code.
- Se prepararon los cambios con `git add` y se creó el commit `893ecd0` con el mensaje `Actividad 02: agregar README y mejorar gitignore`.
- Se fusionó la rama `dev` con `main` mediante un avance rápido.
- Se revisó el historial con `git log --oneline --graph --decorate --all`.

## Decisiones tomadas

- Se adoptó `main` como rama principal y `dev` como rama de desarrollo.
- Se estableció la regla de realizar un commit por cada cambio lógico o actividad terminada.
- Se decidió no incluir secretos ni configuraciones locales en el repositorio.
- No se configuró un repositorio remoto, ya que era un paso opcional de la actividad.

## Uso de IA

Se utilizó Codex como tutor para interpretar la consigna, verificar el flujo de Git, crear la documentación y revisar cada resultado antes de avanzar. Los comandos fueron ejecutados y comprobados por el estudiante.

## Reflexión

La trazabilidad permite que un RSI demuestre qué cambios realizó, cuándo los realizó y por qué. Versionar la documentación y las evidencias con Git facilita su seguimiento, evita que queden archivos aislados y permite relacionar cada resultado con un commit concreto. También es necesario evitar que contraseñas, variables de entorno u otros datos sensibles ingresen al historial del repositorio.
