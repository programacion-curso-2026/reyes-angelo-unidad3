# Deber: Análisis de Datos de Mantenimiento con NumPy y Pandas

## 1. Descripción del Problema
El proyecto consiste en procesar, validar, limpiar y analizar un conjunto de registros de mantenimiento de equipos tecnológicos e industriales. El objetivo es identificar errores en los datos (como duplicados, costos negativos, fechas erróneas o estados inválidos) y extraer métricas estadísticas y financieras clave utilizando Python, NumPy y Pandas.

## 2. Ejecución
Para ejecutar correctamente el proyecto:
1. Abrir el archivo `Deber_8_P3_Mejora_Analitica.ipynb` en Google Colab o Jupyter Notebook.
2. Asegurarse de tener en el mismo directorio los archivos de datos (`mantenimientos.csv` y `mantenimientos_con_errores.csv`).
3. Ir al menú superior y seleccionar **Entorno de ejecución > Ejecutar todo** para procesar todas las celdas secuencialmente.

## 3. Decisiones Tomadas y Algoritmo
* **Estandarización:** Se implementó una función para normalizar los nombres de las columnas a minúsculas y sin tildes para evitar errores de tipo `KeyError`.
* **Estructura de Control:** Se utilizó un ciclo `for` combinado con condicionales `if` para recorrer fila por fila e inspeccionar las reglas de negocio de forma estricta.
* **Manejo de Excepciones:** Se aplicaron bloques `try-except` para capturar fallos críticos como archivos inexistentes (`FileNotFoundError`), vacíos o con formatos corruptos.
* **NumPy y Pandas:** Se utilizaron arreglos de NumPy para cálculos vectorizados y funciones de agregación (`mean`, `median`, `percentile`, `np.where`), mientras que Pandas facilitó la manipulación de DataFrames y agrupaciones.

## 4. Archivos Generados
* `mantenimientos_limpios.csv`: Archivo resultante con los registros que superaron todas las validaciones de calidad.
* `resumen_por_equipo.csv`: Reporte agregado que detalla la cantidad, costo promedio y costo total por cada tipo de equipo.