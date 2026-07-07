# Reporte de Deuda Técnica y Adaptabilidad del Software

**Asignatura:** Sistemas Ágiles  
**Integrantes:** Diana Trujillo  
**Fecha:** 06 de Julio de 2026  

---

## 1. Diagnóstico de Calidad (Código Legacy)
Identifiquen y describan brevemente los 3 principales problemas de diseño encontrados en el archivo `inventario_viejo.py` utilizando los conceptos de calidad de código vistos en clase:

1. **Problema 1: Números Mágicos (Falta de Constantes)** El porcentaje del impuesto (como el IVA) estaba escrito directamente como un valor absoluto (`0.15` o similar) dentro de las operaciones matemáticas de las funciones, en lugar de declararse en una constante global. Esto afecta la mantenibilidad si el impuesto cambia.

2. **Problema 2: Alto Acoplamiento y Falta de Cohesión** El archivo original manejaba la estructura del producto, la lógica de los cálculos de negocio (IVA, totales) y la presentación en consola en un solo lugar. No respetaba el Principio de Responsabilidad Única (SRP).

3. **Problema 3: Uso Indiscriminado de Estructuras Genéricas** El uso de diccionarios genéricos o arreglos sueltos para representar un "Producto" en lugar de un objeto formal (Clase) provocaba código propenso a errores de tipeo en las llaves (como `producto["precio"]`), dificultando el auto-completado y el mantenimiento.

---

## 2. Mapeo de Dificultades para la Evolución (Evidencia Git)
Expliquen qué sucedió cuando intentaron aplicar los cambios sorpresa solicitados por el docente en cada una de sus ramas. Justifiquen el impacto técnico basándose en cuántas funciones o líneas de código se vieron afectadas.

* ### Rama: `cambio-impuesto`
  * **Impacto encontrado:** Al intentar modificar el valor del impuesto, se tuvieron que buscar y reemplazar manualmente múltiples líneas de código dispersas en las funciones de cálculo. El código resistió el cambio debido a la falta de una constante centralizada, aumentando el riesgo de omitir alguna línea.

* ### Rama: `cambio-json`
  * **Impacto encontrado:** Al cambiar el formato de persistencia de texto plano a JSON, el sistema se rompió por completo en las funciones de lectura y escritura. Al estar la lógica de almacenamiento ligada directamente al archivo principal, cambiar el formato obligó a reescribir la estructura central del programa en lugar de solo cambiar un módulo aislado.

* ### Rama: `codigo-barras`
  * **Impacto encontrado:** Agregar un nuevo campo obligatorio como el código de barras obligó a modificar manualmente cada función que creaba, leía o imprimía un producto. La falta de una clase constructora estructurada hizo que el cambio impactara en casi el 80% del archivo original.

---

## 3. Propuesta de Refactorización Inicial
Si tuvieran que rediseñar este módulo utilizando principios de **Código Limpio (Clean Code)**, enumeren qué 3 acciones principales tomarían para eliminar la deuda técnica de este sistema:

1. **Modularización por Capas:** Separar el código en archivos independientes con responsabilidades únicas: `producto.py` (Modelo de datos), `inventario.py` (Lógica de negocio y cálculos) y `main.py` (Punto de entrada y ejecución).
2. **Encapsulamiento con Clases:** Definir una clase formal `Producto` con un método constructor para estandarizar sus atributos (nombre, precio, cantidad, categoría) y evitar el uso de diccionarios planos.
3. **Eliminación de Valores Absolutos:** Centralizar las configuraciones del sistema, como la tasa impositiva, mediante constantes descriptivas en mayúsculas (ej. `TASA_IVA = 0.15`) al inicio del módulo correspondiente.

---

## 4. Conclusiones del Equipo

* **Porcentaje estimado de deuda técnica en el script original (0% al 100%):** [75%]
* **Reflexión ágil:** Un software rígido y con alta deuda técnica frena drásticamente la velocidad de entrega en Scrum porque cualquier cambio pequeño genera un "efecto dominó" que rompe otras partes del sistema, requiriendo más tiempo para corregir errores (refactorización de emergencia) que para entregar nuevo valor al cliente.