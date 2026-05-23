#Importo una libreria especializada en la manipulación y análisis de datos
import pandas as pd

#Lee dataset
df = pd.read_csv("datos/dataset.csv")

#Muestra las primeras filas
print(df.head())
