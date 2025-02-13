import pandas as pd


file_name = "compras-contrataciones-acumar-2024.csv"
file_path = f"./samples/{file_name}"

# cargar el archivo en un dataframe

df_datos = pd.read_csv(file_path)

# mostrar las primeras 5 filas
print(df_datos.head())