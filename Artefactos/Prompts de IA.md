# Registro de los Prompts Usados en el Proyecto Torre de Hanoi

## Uso de la IA ChatGPT:
### **SPRINT I - FUNCIONALIDADES BÁSICAS**
#### **PLANIFICACIÓN**
##### **PROMPT 1:**  
*"Definir un artefacto que concuerde con el ciclo de vida de Scrum, prioriza, define tareas de cada historia de usuario y coloca estimaciones en cada tarea."*

---

## **Historia de Usuario 1: Representación Básica del Juego**
**Como** jugador,  
**Quiero** visualizar tres torres y un conjunto de discos,  
**Para** comprender el estado actual del juego y realizar movimientos.

### Criterios de Aceptación:
- El sistema debe mostrar tres torres (pueden ser gráficos simples o texto).
- Los discos deben representarse claramente y estar apilados en la primera torre al inicio.
- El número de discos debe ser configurable.

##### **PROMPT 2:**  
*"Crea un esquema básico en código para representar el juego de la Torre de Hanoi con tres torres y un conjunto de discos, asegurando que sean visualizables en la pantalla."*

---

## **Historia de Usuario 2: Movimiento de Discos**
**Como** jugador,  
**Quiero** mover un disco desde una torre a otra,  
**Para** resolver el rompecabezas.

### Criterios de Aceptación:
- El jugador puede seleccionar un disco y una torre de destino.
- Solo un disco puede moverse a la vez.
- El sistema actualiza el estado visual de las torres después de cada movimiento.

##### **PROMPT 3:**  
*"Implementa en código la funcionalidad para mover discos entre torres en el juego de la Torre de Hanoi, asegurando que solo se mueva un disco a la vez y que la visualización se actualice después de cada movimiento."*

---

## **Historia de Usuario 3: Validación de Movimientos**
**Como** jugador,  
**Quiero** que el sistema valide los movimientos,  
**Para** evitar colocar un disco más grande sobre uno más pequeño.

### Criterios de Aceptación:
- El sistema debe mostrar un mensaje de error si el movimiento no es válido.
- Los discos no se mueven si violan las reglas del juego.
- El sistema debe permitir solo movimientos válidos.

##### **PROMPT 4:**  
*"Modifica la lógica del juego para validar los movimientos y evitar que un disco más grande sea colocado sobre uno más pequeño. Muestra un mensaje de error en caso de un movimiento inválido."*

---

### **SPRINT II - FUNCIONALIDADES AVANZADAS**
## **Historia de Usuario 4: Contador de Movimientos**
**Como** jugador,  
**Quiero** ver el número de movimientos realizados,  
**Para** medir mi progreso y optimizar mis movimientos.

### Criterios de Aceptación:
- El sistema debe mostrar un contador visible en pantalla.
- El contador aumenta en 1 después de cada movimiento válido.
- El contador no debe incrementarse con movimientos inválidos.

##### **PROMPT 5:**  
*"Añade un contador de movimientos al juego de la Torre de Hanoi que incremente en 1 con cada movimiento válido y se muestre en pantalla."*

---

## **Historia de Usuario 5: Condición de Victoria**
**Como** jugador,  
**Quiero** que el sistema detecte cuando haya resuelto el rompecabezas,  
**Para** recibir una notificación de victoria.

### Criterios de Aceptación:
- El sistema muestra un mensaje de victoria cuando todos los discos están apilados en la última torre en el orden correcto.
- El juego termina después de mostrar el mensaje de victoria.

##### **PROMPT 6:**  
*"Implementa una función en el juego de la Torre de Hanoi que detecte la condición de victoria cuando todos los discos están correctamente apilados en la tercera torre y muestre un mensaje de finalización."*

---

## **CIERRE DEL PROYECTO**
##### **PROMPT 7:**  
*"Adquiere los conocimientos de un Ingeniero de Software experto en Agilismo. Tu proyecto de la Torre de Hanoi en el marco de Scrum está en la etapa de cierre. Redacta un acta de finalización del proyecto."*

---

Este documento registra los prompts utilizados durante el desarrollo del proyecto **Torre de Hanoi**, siguiendo el marco de trabajo **Scrum**.
