import pandas as pd


file_name = "Financial Sample.xlsx"
file_path = f"./samples/{file_name}"

df_datos = pd.read_excel(file_path, sheet_name="Sheet1")

print(df_datos.tail())
