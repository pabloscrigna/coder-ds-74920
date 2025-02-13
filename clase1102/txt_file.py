import pandas as pd

file_name = "Pokemon_data.txt"
file_path = f"./samples/{file_name}" # 34|Pedro|Gonzalez|Calle

df_datos = pd.read_csv(file_path, delimiter="\t")

print(type(df_datos))

print(df_datos.head())