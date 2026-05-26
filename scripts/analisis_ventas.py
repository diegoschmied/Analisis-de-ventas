# =====================================
# IMPORTACIÓN DE LIBRERÍAS
# =====================================

import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# CARGA DEL DATASET
# =====================================

# Se carga el archivo CSV desde la carpeta /datos.
# El uso de rutas relativas permite ejecutar el
# proyecto correctamente en distintos entornos.

df = pd.read_csv("datos/dataset.csv")

# Se muestran las primeras filas para verificar
# que los datos fueron importados correctamente.
print(df.head())

# =====================================
# CÁLCULO DE INDICADORES
# =====================================

# Se calculan métricas básicas para analizar
# el rendimiento general de ventas.

ventas_totales = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()

print("Ventas totales:", ventas_totales)
print(f"Promedio: {promedio_ventas:.2f}")
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)

# =====================================
# PROCESAMIENTO DE FECHAS
# =====================================

# La columna de fechas se convierte al formato datetime
# para facilitar el análisis temporal y la generación
# de gráficos.

df["sales_date"] = pd.to_datetime(df["sales_date"]
)

# =====================================
# GENERACIÓN DEL GRÁFICO
# =====================================

# Se genera un gráfico de líneas para visualizar
# la evolución de ventas a lo largo del tiempo.

plt.figure(figsize=(10,5))
plt.plot(
    df["sales_date"],
    df["sales_amount"]
)

plt.title("Evolución de ventas")
plt.xlabel("Fecha")
plt.ylabel("Monto")

# El gráfico se guarda automáticamente en la carpeta
# /resultados para mantener organizada la salida del análisis.

plt.savefig("resultados/grafico_ventas.png")

print("Gráfico generado correctamente.")