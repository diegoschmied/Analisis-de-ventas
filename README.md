# Analisis-de-ventas
# TP Organización Empresarial

## Integrantes
- Santino Maire
- Diego Schmied

## Escenario elegido
Análisis de ventas de una pequeña empresa.

## Dataset utilizado
El dataset utilizado es el siguiente:
https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6
Este archivo CSV cuenta con 3 tipos de datos:
- La ID de cada venta
- La fecha de esta
- El monto que le corresponde

## Tecnologías
- Python
- Git
- GitHub
- Jira
- Google Colab

## Cómo ejecutar

- Clonar el repositorio desde GitHub.
- Abrir el proyecto en Google Colab.
- Verificar que el dataset se encuentre en la carpeta `/datos`.
- Ejecutar el script ubicado en `/scripts/analisis_ventas.py`.
- Los resultados y gráficos generados se almacenarán automáticamente en la carpeta `/resultados`.
- Para visualizar el gráfico generado, ejecutar:

```python
from IPython.display import Image
Image("resultados/grafico_ventas.png")
```

## Objetivo del proyecto
Analizar información de ventas para generar indicadores básicos que permitan interpretar el desempeño de la empresa.

## Funciones del proyecto
- Importación de datos desde un archivo CSV
- Procesamiento de ventas
- Cálculo de métricas básicas
- Visualización de resultados
