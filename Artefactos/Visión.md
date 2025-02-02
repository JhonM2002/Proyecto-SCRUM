# Documento de Visión y Alcance

## Proyecto: Juego Torre de Hanoi

### 1. Tema
El proyecto consiste en un juego basado en las reglas clásicas de la Torre de Hanoi, que permite al usuario interactuar con el juego en un entorno digital. Este juego guía al usuario para mover los discos siguiendo las reglas, valida sus movimientos, y contabiliza el número de movimientos realizados hasta completar el objetivo.

### 2. Objetivos
- Proveer una plataforma sencilla para compartir y ver contenido visual.
- Ofrecer un entorno interactivo para jugar la Torre de Hanoi.
- Validar que los movimientos del jugador cumplan con las reglas.
- Contar y mostrar los movimientos realizados.
- Detectar y notificar al usuario cuando gane el juego.
- La metodología SCRUM se aplicará para asegurar un desarrollo ágil y eficiente. Los principios y prácticas de SCRUM a implementar son:


### 3. Alcance
El proyecto abarcará las siguientes funcionalidades:


#### Representación visual del estado del juego
**Objetivo:** Mostrar las tres torres y los discos en su estado actual.
**Alcance:**
- Representación gráfica de las torres y los discos.
- Actualización en tiempo real de la posición de los discos en las torres.
- Indicación de la torre destino y la torre origen para cada movimiento.

#### Movimiento interactivo de discos
**Objetivo:** Permitir al usuario mover los discos entre las torres.
**Alcance:**
- Validación de movimientos según las reglas de la Torre de Hanoi.


#### Validación de movimientos
**Objetivo:** Verificar que los movimientos del usuario cumplan con las reglas del juego.
**Alcance:**
- Verificación de que no se pueda mover un disco desde una torre vacía
- Verificación de que no se pueda colocar un disco más grande sobre uno más pequeño
- Notificación al usuario si el movimiento no cumple con las reglas.


#### Contador de movimientos
**Objetivo:** Contar y mostrar el número de movimientos realizados por el usuario.
**Alcance:**
- Incremento del contador cada vez que se realiza un movimiento válido.

#### Condición de victoria
**Objetivo:** Detectar cuando el usuario ha completado el juego.
**Alcance:**
- Verificación de que los discos estén apilados correctamente en la torre destino.
- Notificación al usuario cuando gana el juego.

### 4. Requisitos Generales del Sistema
- **Interfaz de Usuario:** Consola de comandos.
- **Plataforma:** Desarrollado para ejecutarse en sistemas operativos basados en consola (Windows, Linux, MacOS).

### Referencias
- Documento de Visión y Alcance proporcionado.
- Historias de Usuario detalladas para la implementación en consola.
