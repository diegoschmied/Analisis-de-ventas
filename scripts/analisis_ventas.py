
import pandas as pd
import matplotlib.pyplot as plt

#Lee dataset
df = pd.read_csv("datos/dataset.csv")

#Muestra las primeras filas
print(df.head())

#Calcula las métricas
ventas_totales = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()

#Muestra los resultados
print("Ventas totales:", ventas_totales)
print("Promedio:", promedio_ventas)
print("Venta máxima:", venta_maxima)
print("Venta mínima:", venta_minima)

#Convierte las fechas
df["sales_date"] = pd.to_datetime(df["sales_date"])
