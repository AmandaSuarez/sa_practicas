# Reporte de Deuda Técnica y Adaptabilidad del Software

**Asignatura:** Sistemas Ágiles
**Integrantes:** Leidya Estefania Almeida Ipiales
**Fecha:** 04-07-2026

## 1. Diagnóstico de Calidad (Código Legacy)
* **Problema 1:** Antipatrón "God Object" en el código inicial; una sola función gestionaba validación, cálculo, persistencia y formato.
* **Problema 2:** Hardcoding de constantes (como el IVA del 15% o 12%), lo que restaba flexibilidad al software ante cambios legales.
* **Problema 3:** Código duplicado en la lógica de cálculo de IVA e impresión, lo que aumentaba el riesgo de errores al realizar actualizaciones.

## 2. Mapeo de Dificultades para la Evolución
* **Cambio de impuesto:** La rigidez del código base requirió modificar la lógica central en múltiples puntos en lugar de cambiar una configuración.
* **Cambio a JSON:** El sistema colapsó al intentar migrar desde archivos de texto plano, obligando a reestructurar la capa de almacenamiento.
* **Código de barras:** La integración fue compleja debido a la ausencia de una estructura de objetos definida previamente.

## 3. Propuesta de Refactorización
* **Modularización:** Separación exitosa en `models.py` (datos), `storage.py` (persistencia), `logic.py` (reglas de negocio) y `main.py` (interfaz).
* **Formato Estructurado:** Migración a formato JSON para asegurar la integridad y escalabilidad de los datos.
* **Encapsulamiento:** Implementación de clases para gestionar productos, facilitando la validación y el mantenimiento.

## 4. Conclusiones y Reflexión Ágil
* **Deuda Técnica:** Se estima que el código original mantenía una deuda técnica cercana al 90%, lo que impedía una entrega de valor continua.
* **Reflexión:** En marcos ágiles como Scrum, un software con alta deuda técnica genera fricción, obligando al equipo a priorizar la corrección de errores sobre la entrega de funcionalidades.