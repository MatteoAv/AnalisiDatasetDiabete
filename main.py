import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from datetime import datetime


#FORMATTAZIONE DELLA TABELLA MOSTRATA DA TERMINALE
############################################################################################
# mostra tutte le colonne
pd.set_option('display.max_columns', None)
# allarga la “larghezza” massima della console (in caratteri)
pd.set_option('display.width', 1000)
# opzionale: non troncare i contenuti delle singole celle
pd.set_option('display.max_colwidth', None)
############################################################################################


# LEGENDA STATISTICHE
############################################################################################
# mean = MEDIA
# std = DEVIAZIONE STANDARD
# min = VALORE MINIMO
# 25% = PRIMO QUARTILE: il punto sotto cui si trova il 25% dei dati
# 50% = MEDIANA / SECONDO QUARTILE
# 75% = TERZO QUARTILE
# max = VALORE MASSIMO
############################################################################################

#SETTARE I RISULTATI DA TERMINALE CON SOLO 2 CIFRE DECIMALI
# pd.set_option('display.float_format', '{:.2f}'.format)


#DEFINIZIONE DATASET
############################################################################################
# df = pd.read_csv("Excel/Biochemical_parameters.csv")
# df = pd.read_csv("Excel/Diagnostics.csv")
# df = pd.read_csv("Excel/Glucose_measurements.csv")
# df = pd.read_csv("Excel/Patient_info.csv")
############################################################################################


#CREAZIONE GRAFICO SULLE PRIME 22 DIAGNOSI CON PIU PAZIENTI AFFETTI
############################################################################################
# # Raggruppa per la colonna 'Description' e conta il numero di pazienti in ogni gruppo
# df = pd.read_csv("Excel/Diagnostics.csv")
# grouped = df.groupby('Description').size()
#
# # Ordina i dati in ordine decrescente
# top_22_descriptions = grouped.sort_values(ascending=False).head(22)
#
# fig, ax = plt.subplots(figsize=(12,8))
#
# # disegna il barplot
# sns.barplot(
#     x=top_22_descriptions.index,
#     y=top_22_descriptions.values,
#     hue=top_22_descriptions.index,
#     palette="viridis",
#     legend=False,
#     ax=ax
# )
#
# # prendi le etichette originali, applica wrapping ogni 15 caratteri
# wrapped = top_22_descriptions.index.to_series().str.wrap(55)
#
# # impostale sull'asse x, con rotazione
# ax.set_xticklabels(wrapped, rotation=45, ha='right')
# ax.set_ylabel('Numero di pazienti', fontsize=16)
# ax.set_xlabel('')  # niente label orizzontale
#
# plt.tight_layout()
# plt.show()
#
#
# # Stampa le prime 22 descrizioni con il numero di pazienti
# print(top_22_descriptions)
# print()
############################################################################################


#STAMPA DELLE STATISTICHE DEL DATASET
############################################################################################
# print()
# print('numero di righe e colonne')
# print(df.shape)
# print()
# print('tipi e missing')
# print(df.info())
# print()
# print('statistiche numeriche di base')
# print(df.describe()) #viene eseguito solo sulle colonne numeriche es:int64
############################################################################################


#MERGE DELLE TABELLE Diagnostics.csv E Biochemical_parameters.csv E STAMPA DELLE STATISTICHE E
#DEI PAZIENTI CHE HANNO UNO SPECIFICA COMPLICAZIONE (Other and unspecified hyperlipidemia)
############################################################################################
# diagnostics_df = pd.read_csv("Excel/Diagnostics.csv")
# biochemical_df = pd.read_csv("Excel/Biochemical_parameters.csv")
# # pivot dei parametri
# bio_wide = biochemical_df.pivot_table(
#     index="Patient_ID",
#     columns="Name",
#     values="Value",
#     aggfunc="mean"
# ).reset_index()
#
# # merge wide
# merged_wide = pd.merge(
#     diagnostics_df,
#     bio_wide,
#     on="Patient_ID",
#     how="left"
# )
#
# #PRINT STATISTICHE
# # print()
# # print('numero di righe e colonne')
# # print(merged_wide.shape)
# # print()
# # print('tipi e missing')
# # print(merged_wide.info())
# # print()
# # print('statistiche numeriche di base')
# # print(merged_wide.describe()) #viene eseguito solo sulle colonne numeriche es:int64
# # print()
#
#
# # filtri solo le righe con Description == 'Other and unspecified hyperlipidemia'
# subset = merged_wide[ merged_wide['Description'] == 'Other and unspecified hyperlipidemia' ]
#
#
# #PRINT DI QUANTI VALORI NULLI HA OGNI COLONNA DELLA TABELLA
# nan_mask = subset.isna()
# nan_count = nan_mask.sum()
# print(nan_count)
#
# #PRINT LISTA PAZIENTI CON QUESTA COMPLICAZIONE (Other and unspecified hyperlipidemia)
# print(subset)
############################################################################################


#STAMPA DI SESSO E ETA DEI PAZIENTI AFFETTI DA UNA CERTA COMPLICAZIONE
############################################################################################
diagnostics_df = pd.read_csv("Excel/Diagnostics.csv")
patient_df = pd.read_csv("Excel/Patient_info.csv")

#Merge dei dataset su Patient_ID
merged = pd.merge(
    diagnostics_df,
    patient_df,
    on="Patient_ID",
    how="left"
)

# STAMPA DEI CODICI CHE HANNO COME DESCRIZIONE DELLA PATOLOGIA "Unspecified acquired hypothyroidism", "Unspecified essential hypertension"
# df_hp = merged[merged["Description"] == "Other and unspecified hyperlipidemia"].copy()
#
# print(df_hp["Code"].tolist())
# print("Codici unici:", df_hp["Code"].unique())
# print(df_hp[["Patient_ID","Code"]])


df_hp = merged[merged["Code"] == "272.4"].copy()

#calcola l'età (anno corrente 2025)
df_hp["Età"] = 2025 - df_hp["Birth_year"]

#Grafico distribuzione del sesso

light_blue = "#ADD8E6"   # “lightblue”
light_red  = "#FFB6C1"   # “lightpink”

# Conta e ordina (per sicurezza) i due valori
counts = df_hp["Sex"].value_counts()

# Definisci un dizionario di colori
color_map = {"M": light_blue, "F": light_red}
colors = [color_map[label] for label in counts.index]

# Pie‐chart con colori personalizzati
plt.figure(figsize=(6,6))
counts.plot.pie(
    colors=colors,
    autopct="%1.1f%%",
    startangle=90,
    legend=False
)
plt.ylabel("")
plt.title("")
plt.axis("equal")
plt.tight_layout()
plt.show()

#Grafico distribuzione dell'età
plt.figure(figsize=(8,5))
sns.kdeplot(
    data=df_hp,
    x="Età",
    fill=True,        # area sotto la curva colorata
    alpha=0.4,        # trasparenza
    linewidth=2
)
plt.title("")
plt.xlabel("Età")
plt.ylabel("Densità stimata")
plt.tight_layout()
plt.show()

#Istogramma con numero di pazienti per etá
plt.figure(figsize=(8,5))
sns.histplot(
    data=df_hp,
    x="Età",
    bins=10,          # numero di barre (regola a piacere)
    stat="count",     # indica di mostrare conteggi anziché densità
    discrete=False    # False di default: barre continue
)
plt.xlabel("Età")
plt.ylabel("Numero di pazienti")
plt.tight_layout()
plt.show()
############################################################################################




