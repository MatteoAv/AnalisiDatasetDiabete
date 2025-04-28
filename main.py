import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# mostra tutte le colonne
pd.set_option('display.max_columns', None)
# allarga la “larghezza” massima della console (in caratteri)
pd.set_option('display.width', 1000)
# opzionale: non troncare i contenuti delle singole celle
pd.set_option('display.max_colwidth', None)


# pd.set_option('display.float_format', '{:.2f}'.format)

# df = pd.read_csv("Excel/Biochemical_parameters.csv")
# df = pd.read_csv("Excel/Diagnostics.csv")
# df = pd.read_csv("Excel/Glucose_measurements.csv")
# df = pd.read_csv("Excel/Patient_info.csv")

# LEGENDA STATISTICHE
# mean = MEDIA
# std = DEVIAZIONE STANDARD
# min = VALORE MINIMO
# 25% = PRIMO QUARTILE il punto sotto cui si trova il 25% dei dati
# 50% = MEDIANA / SECONDO QUARTILE
# 75% = TERZO QUARTILE
# max = VALORE MASSIMO

# for index, row in df.iterrows():
#     print(row)
#
#
# print()
# print('numero di righe e colonne')
# print(df.shape)
# print()
# print('tipi e missing')
# print(df.info())
# print()
# print('statistiche numeriche di base')
# print(df.describe()) #viene eseguito solo sulle colonne numeriche es:int64


diagnostics_df = pd.read_csv("Excel/Diagnostics.csv")
biochemical_df = pd.read_csv("Excel/Biochemical_parameters.csv")
# pivot dei parametri
bio_wide = biochemical_df.pivot_table(
    index="Patient_ID",
    columns="Name",
    values="Value",
    aggfunc="mean"
).reset_index()

# merge wide
merged_wide = pd.merge(
    diagnostics_df,
    bio_wide,
    on="Patient_ID",
    how="left"
)

# print()
# print('numero di righe e colonne')
# print(merged_wide.shape)
# print()
# print('tipi e missing')
# print(merged_wide.info())
# print()
# print('statistiche numeriche di base')
# print(merged_wide.describe()) #viene eseguito solo sulle colonne numeriche es:int64


# filtri solo le righe con Description == 'Other and unspecified hyperlipidemia'
subset = merged_wide[ merged_wide['Description'] == 'Other and unspecified hyperlipidemia' ]

# poi le stampi tutte insieme
print(subset)

# for index, row in merged_wide.iterrows():
#     print(row)
