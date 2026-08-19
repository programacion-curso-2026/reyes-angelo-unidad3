# Deber 9: MiniTienda - Registro y Análisis de Ventas

## 📌 Descripción del Proyecto
Este proyecto de consola implementa un sistema modular en Python para la gestión de una tienda, permitiendo administrar catálogos de productos mediante tuplas y diccionarios, registrar transacciones con validación de errores, aplicar descuentos por volumen, y realizar análisis cuantitativos con NumPy, Pandas y visualizaciones con Matplotlib.

---

## 🛠️ Requisitos e Implementación Técnica
* **Estructuras de Datos:** 
  * Tuplas para el catálogo inmutable de productos.
  * Diccionarios para la gestión dinámica de precios y stock.
  * Listas como búfer temporal de transacciones.
* **Manejo de Errores (`try/except/else/finally`):** Control de excepciones ante archivos inexistentes, datos corruptos y validación de IDs inexistentes (con registro automático en `log.txt`).
* **Análisis de Datos:** Uso de Pandas para la manipulación de DataFrames y agrupaciones (`groupby`), y NumPy para métricas estadísticas (`mean`, `std`, `sum`).
* **Visualización:** Gráficos de barras con Matplotlib e industrialización de gráficos exportados a formato PNG.

---

## 📂 Archivos en el Repositorio (`Deber_9-P3`)
* `Deber_9_P3.ipynb`: Cuaderno principal ejecutable en Google Colab con el código modular y celdas de prueba.
* `ventas.csv`: Archivo de datos generado automáticamente con el registro de ventas.
* `log.txt`: Archivo de registro histórico de eventos e intentos fallidos de venta.
* `ingresos.png`: Gráfico exportado de los ingresos por producto.
* `README.md`: Documentación oficial de la solución.