import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
# diagnostics_df = pd.read_csv("Excel/Diagnostics.csv")
# patient_df = pd.read_csv("Excel/Patient_info.csv")
#
# #Merge dei dataset su Patient_ID
# merged = pd.merge(
#     diagnostics_df,
#     patient_df,
#     on="Patient_ID",
#     how="left"
# )
#
# # STAMPA DEI CODICI CHE HANNO COME DESCRIZIONE DELLA PATOLOGIA "Unspecified acquired hypothyroidism", "Unspecified essential hypertension"
# # df_hp = merged[merged["Description"] == "Other and unspecified hyperlipidemia"].copy()
# #
# # print(df_hp["Code"].tolist())
# # print("Codici unici:", df_hp["Code"].unique())
# # print(df_hp[["Patient_ID","Code"]])
#
#
# df_hp = merged[merged["Code"] == "272.4"].copy()
#
# #calcola l'età (anno corrente 2025)
# df_hp["Età"] = 2025 - df_hp["Birth_year"]
#
# #Grafico distribuzione del sesso
#
# light_blue = "#ADD8E6"   # “lightblue”
# light_red  = "#FFB6C1"   # “lightpink”
#
# # Conta e ordina (per sicurezza) i due valori
# counts = df_hp["Sex"].value_counts()
#
# # Definisci un dizionario di colori
# color_map = {"M": light_blue, "F": light_red}
# colors = [color_map[label] for label in counts.index]
#
# # Pie‐chart con colori personalizzati
# plt.figure(figsize=(6,6))
# counts.plot.pie(
#     colors=colors,
#     autopct="%1.1f%%",
#     startangle=90,
#     legend=False
# )
# plt.ylabel("")
# plt.title("")
# plt.axis("equal")
# plt.tight_layout()
# plt.show()
#
# #Grafico distribuzione dell'età
# plt.figure(figsize=(8,5))
# sns.kdeplot(
#     data=df_hp,
#     x="Età",
#     fill=True,        # area sotto la curva colorata
#     alpha=0.4,        # trasparenza
#     linewidth=2
# )
# plt.title("")
# plt.xlabel("Età")
# plt.ylabel("Densità stimata")
# plt.tight_layout()
# plt.show()
#
# #Istogramma con numero di pazienti per etá
# plt.figure(figsize=(8,5))
# sns.histplot(
#     data=df_hp,
#     x="Età",
#     bins=10,          # numero di barre (regola a piacere)
#     stat="count",     # indica di mostrare conteggi anziché densità
#     discrete=False    # False di default: barre continue
# )
# plt.xlabel("Età")
# plt.ylabel("Numero di pazienti")
# plt.tight_layout()
# plt.show()
############################################################################################

#NUOVO GRAFICO
############################################################################################
# 1) Caricamento
diagnostics_df = pd.read_csv("Excel/Diagnostics.csv")
patient_df     = pd.read_csv("Excel/Patient_info.csv")

# 2) Costruisci il flag "has complication" ONE‑ROW‑PER‑PATIENT
diagnostics_df["Has_complication"] = diagnostics_df["Description"].notna()
complication_flag = (
    diagnostics_df
    .groupby("Patient_ID")["Has_complication"]
    .any()
    .reset_index()
)

# 3) Merge: UNA riga per paziente
merged = pd.merge(
    patient_df,
    complication_flag,
    on="Patient_ID",
    how="left"
)
# i pazienti senza diagnosi avranno NaN → False
merged["Has_complication"] = (
    merged["Has_complication"]
      .astype("boolean")      # diventa BooleanDtype (nullable)
      .fillna(False)          # i NaN diventano False, senza warning
)
merged["Complicanza"] = merged["Has_complication"].map({True:"Sì", False:"No"})

# verifica
assert len(merged) == 736, f"Righe in merged = {len(merged)} (attesi 736)"

# 4) Calcola età e fasce
merged["Eta"] = 2025 - merged["Birth_year"]
bins   = [0,20,30,40,50,60,70,80,90,120]
labels = ['0-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91+']
merged["Eta_bin"] = pd.cut(merged["Eta"], bins=bins, labels=labels, right=True)

# 5) Tabella di contingenza
table = (
    merged
    .groupby(["Eta_bin","Sex","Complicanza"], observed=True)
    .size()
    .unstack(fill_value=0)
)

# 6) Estrai M e F e reindicizza tutte le fasce
table_M = table.xs("M", level="Sex").reindex(labels, fill_value=0)
table_F = table.xs("F", level="Sex").reindex(labels, fill_value=0)

# 7) Prepara i vettori per il plot
x      = np.arange(len(labels))
width  = 0.35
no_M   = table_M["No"];   yes_M = table_M["Sì"]
no_F   = table_F["No"];   yes_F = table_F["Sì"]

colors = {
    'M_no':  '#ADD8E6',  # lightblue
    'M_yes': '#4682B4',  # steelblue
    'F_no':  '#FFB6C1',  # lightpink
    'F_yes': '#FF69B4',  # hotpink
}

# 8) Disegna il bar‑chart impilato
fig, ax = plt.subplots(figsize=(10,6))

bars_M_no  = ax.bar(x - width/2, no_M,  width, label='Maschi senza complicanze', color=colors['M_no'])
bars_M_yes = ax.bar(x - width/2, yes_M, width, bottom=no_M, label='Maschi con complicanze',    color=colors['M_yes'])
bars_F_no  = ax.bar(x + width/2, no_F,  width, label='Femmine senza complicanze', color=colors['F_no'])
bars_F_yes = ax.bar(x + width/2, yes_F, width, bottom=no_F, label='Femmine con complicanze',    color=colors['F_yes'])

# 9) Annotazioni dei valori dentro le barre
def annotate_bars(bars):
    for bar in bars:
        h = bar.get_height()
        if h>0:
            ax.annotate(f'{int(h)}',
                        xy=(bar.get_x()+bar.get_width()/2, bar.get_y()+h/2),
                        ha='center', va='center', fontsize=8)

for grp in (bars_M_no, bars_M_yes, bars_F_no, bars_F_yes):
    annotate_bars(grp)

# 10) Etichette e stile
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.set_xlabel("Fascia d'età")
ax.set_ylabel("Numero pazienti")
ax.legend(title="Legenda")

plt.tight_layout()
plt.show()


############################################################################################


