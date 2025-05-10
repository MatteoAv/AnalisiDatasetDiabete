import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
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

#CREAZIONE GRAFICO CHE MOSTRA LA DISTRIBUZIONE DI COMPLICAZIONI, SESSO ED ETA SU TUTTI I PAZIENTI
############################################################################################
# # 1) Caricamento
# diagnostics_df = pd.read_csv("Excel/Diagnostics.csv")
# patient_df     = pd.read_csv("Excel/Patient_info.csv")
#
# # 2) Costruisci il flag "has complication" ONE‑ROW‑PER‑PATIENT
# diagnostics_df["Has_complication"] = diagnostics_df["Description"].notna()
# complication_flag = (
#     diagnostics_df
#     .groupby("Patient_ID")["Has_complication"]
#     .any()
#     .reset_index()
# )
#
# # 3) Merge: UNA riga per paziente
# merged = pd.merge(
#     patient_df,
#     complication_flag,
#     on="Patient_ID",
#     how="left"
# )
# # i pazienti senza diagnosi avranno NaN → False
# merged["Has_complication"] = (
#     merged["Has_complication"]
#       .astype("boolean")      # diventa BooleanDtype (nullable)
#       .fillna(False)          # i NaN diventano False, senza warning
# )
# merged["Complicanza"] = merged["Has_complication"].map({True:"Sì", False:"No"})
#
# # verifica
# assert len(merged) == 736, f"Righe in merged = {len(merged)} (attesi 736)"
#
# # 4) Calcola età e fasce
# merged["Eta"] = 2025 - merged["Birth_year"]
# bins   = [0,20,30,40,50,60,70,80,90,120]
# labels = ['0-20','21-30','31-40','41-50','51-60','61-70','71-80','81-90','91+']
# merged["Eta_bin"] = pd.cut(merged["Eta"], bins=bins, labels=labels, right=True)
#
# # 5) Tabella di contingenza
# table = (
#     merged
#     .groupby(["Eta_bin","Sex","Complicanza"], observed=True)
#     .size()
#     .unstack(fill_value=0)
# )
#
# # 6) Estrai M e F e reindicizza tutte le fasce
# table_M = table.xs("M", level="Sex").reindex(labels, fill_value=0)
# table_F = table.xs("F", level="Sex").reindex(labels, fill_value=0)
#
# # 7) Prepara i vettori per il plot
# x      = np.arange(len(labels))
# width  = 0.35
# no_M   = table_M["No"];   yes_M = table_M["Sì"]
# no_F   = table_F["No"];   yes_F = table_F["Sì"]
#
# colors = {
#     'M_no':  '#ADD8E6',  # lightblue
#     'M_yes': '#4682B4',  # steelblue
#     'F_no':  '#FFB6C1',  # lightpink
#     'F_yes': '#FF69B4',  # hotpink
# }
#
# # 8) Disegna il bar‑chart impilato
# fig, ax = plt.subplots(figsize=(10,6))
#
# bars_M_no  = ax.bar(x - width/2, no_M,  width, label='Maschi senza complicanze', color=colors['M_no'])
# bars_M_yes = ax.bar(x - width/2, yes_M, width, bottom=no_M, label='Maschi con complicanze',    color=colors['M_yes'])
# bars_F_no  = ax.bar(x + width/2, no_F,  width, label='Femmine senza complicanze', color=colors['F_no'])
# bars_F_yes = ax.bar(x + width/2, yes_F, width, bottom=no_F, label='Femmine con complicanze',    color=colors['F_yes'])
#
# # 9) Annotazioni dei valori dentro le barre
# def annotate_bars(bars):
#     for bar in bars:
#         h = bar.get_height()
#         if h>0:
#             ax.annotate(f'{int(h)}',
#                         xy=(bar.get_x()+bar.get_width()/2, bar.get_y()+h/2),
#                         ha='center', va='center', fontsize=8)
#
# for grp in (bars_M_no, bars_M_yes, bars_F_no, bars_F_yes):
#     annotate_bars(grp)
#
# # 10) Etichette e stile
# ax.set_xticks(x)
# ax.set_xticklabels(labels, rotation=45)
# ax.set_xlabel("Fascia d'età")
# ax.set_ylabel("Numero pazienti")
# ax.legend(title="Legenda")
#
# plt.tight_layout()
# plt.show()
############################################################################################

df = pd.read_csv("Excel/Glucose_measurements.csv")
df = df[(df['Measurement'].notna()) & (df['Measurement'] >= 40) &  (df['Measurement'] <= 500)]
#Pulizia del dataset per eliminare valori di glucosio nulli o fisiologicamente impossibili (comunque non ce ne sono)

#ANALISI TIR
############################################################################################
# # Funzione per calcolare il TIR di un paziente
# def calculate_tir(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] >= 70) & (misurazioni['Measurement'] <= 180)] # Seleziona solo le righe che nel campo Measurement hanno un valore compreso tra 70 e 180 mg/dL
#     tir = len(righe_valide)/totale * 100 # Calcola il %TIR facendo Misurazioni Valide/Misurazioni Totali
#     return tir
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tir_by_paziente = pazienti.apply(calculate_tir).reset_index(name='%TIR') # Calcoliamo il TIR di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TIR
# # tir_by_paziente = tir_by_paziente.sort_values(by='%TIR', ascending=False)
# print(tir_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tir_by_paziente['Patient_ID'], tir_by_paziente['%TIR'], color='skyblue')
# plt.xticks([])
# plt.ylabel('% Time In Range (70–180 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TIR
# print(tir_by_paziente['%TIR'].describe())
#
# # Raggruppiamo i valori di %TIR in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tir_intervals = pd.cut(tir_by_paziente['%TIR'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tir_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TIR
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='skyblue', edgecolor='black')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TIR')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tir_values = tir_by_paziente['%TIR']
#
# # Statistiche descrittive
# media = tir_values.mean()
# mediana = tir_values.median()
# asimmetria = skew(tir_values) #skewness
# curtosi = kurtosis(tir_values)
#
# tir_arrotondato = tir_values.round()
# moda = tir_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# q1 = tir_values.quantile(0.25)
# q3 = tir_values.quantile(0.75)
# iqr = q3 - q1
# outliers = tir_values[(tir_values < q1 - 1.5 * iqr) | (tir_values > q3 + 1.5 * iqr)]
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################

# ANALISI TAR
############################################################################################
# # Funzione per calcolare il TAR di un paziente
# def calculate_tar(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] > 180)] # Seleziona solo le righe che nel campo Measurement hanno un valore maggiore di 180 mg/dL
#     tar = len(righe_valide)/totale * 100 # Calcola il %TAR facendo Misurazioni Valide/Misurazioni Totali
#     return tar
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tar_by_paziente = pazienti.apply(calculate_tar).reset_index(name='%TAR') # Calcoliamo il TAR di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TAR
# # tar_by_paziente = tar_by_paziente.sort_values(by='%TAR', ascending=False)
# print(tar_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tar_by_paziente['Patient_ID'], tar_by_paziente['%TAR'], color='skyblue')
# plt.xticks([])
# plt.ylabel('% Time Above Range (> 180 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TAR
# print(tar_by_paziente['%TAR'].describe())
#
# # Raggruppiamo i valori di %TAR in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tar_intervals = pd.cut(tar_by_paziente['%TAR'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tar_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TAR
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='skyblue', edgecolor='black')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TAR')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tar_values = tar_by_paziente['%TAR']
#
# # Statistiche descrittive
# media = tar_values.mean()
# mediana = tar_values.median()
# asimmetria = skew(tar_values) #skewness
# curtosi = kurtosis(tar_values)
#
# tar_arrotondato = tar_values.round()
# moda = tar_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# # calcola Q1, Q3 e IQR
# q1 = tar_values.quantile(0.25)
# q3 = tar_values.quantile(0.75)
# iqr = q3 - q1
#
# # soglie per outlier
# lower_thr = q1 - 1.5 * iqr
# upper_thr = q3 + 1.5 * iqr
#
# print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
# print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
# outliers = tar_values[(tar_values < lower_thr) | (tar_values > upper_thr)]
# print("Valori TAR considerati outlier:")
# print(outliers.sort_values().to_list())
#
#
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################


# ANALISI TAR LV1
############################################################################################
# # Funzione per calcolare il TARLV1 di un paziente
# def calculate_tar(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] >= 181) & (misurazioni['Measurement'] <= 249)] # Seleziona solo le righe che nel campo Measurement hanno un valore compreso tra 181 e 249 mg/dL
#     tar = len(righe_valide)/totale * 100 # Calcola il %TARLV1 facendo Misurazioni Valide/Misurazioni Totali
#     return tar
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tar_by_paziente = pazienti.apply(calculate_tar).reset_index(name='%TARLV1') # Calcoliamo il TARLV1 di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TARLV1
# # tar_by_paziente = tar_by_paziente.sort_values(by='%TARLV1', ascending=False)
# print(tar_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tar_by_paziente['Patient_ID'], tar_by_paziente['%TARLV1'], color='#ffa07a')
# plt.xticks([])
# plt.ylabel('% Time Above Range LV1 (181 - 249 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TARLV1
# print(tar_by_paziente['%TARLV1'].describe())
#
# # Raggruppiamo i valori di %TARLV1 in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tar_intervals = pd.cut(tar_by_paziente['%TARLV1'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tar_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TARLV1
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='#ffa07a')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TARLV1')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tar_values = tar_by_paziente['%TARLV1']
#
# # Statistiche descrittive
# media = tar_values.mean()
# mediana = tar_values.median()
# asimmetria = skew(tar_values) #skewness
# curtosi = kurtosis(tar_values)
#
# tar_arrotondato = tar_values.round()
# moda = tar_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# # calcola Q1, Q3 e IQR
# q1 = tar_values.quantile(0.25)
# q3 = tar_values.quantile(0.75)
# iqr = q3 - q1
#
# # soglie per outlier
# lower_thr = q1 - 1.5 * iqr
# upper_thr = q3 + 1.5 * iqr
#
# print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
# print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
# outliers = tar_values[(tar_values < lower_thr) | (tar_values > upper_thr)]
# print("Valori TARLV1 considerati outlier:")
# print(outliers.sort_values().to_list())
#
#
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################


# ANALISI TAR LV2
############################################################################################
# # Funzione per calcolare il TARLV2 di un paziente
# def calculate_tar(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] >= 250)] # Seleziona solo le righe che nel campo Measurement hanno un valore maggiore di 250 mg/dL
#     tar = len(righe_valide)/totale * 100 # Calcola il %TARLV2 facendo Misurazioni Valide/Misurazioni Totali
#     return tar
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tar_by_paziente = pazienti.apply(calculate_tar).reset_index(name='%TARLV2') # Calcoliamo il TARLV2 di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TARLV2
# # tar_by_paziente = tar_by_paziente.sort_values(by='%TARLV2', ascending=False)
# print(tar_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tar_by_paziente['Patient_ID'], tar_by_paziente['%TARLV2'], color='#e64100')
# plt.xticks([])
# plt.ylabel('% Time Above Range LV2 (> 249 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TARLV2
# print(tar_by_paziente['%TARLV2'].describe())
#
# # Raggruppiamo i valori di %TARLV2 in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tar_intervals = pd.cut(tar_by_paziente['%TARLV2'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tar_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TARLV2
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='#e64100', edgecolor='black')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TARLV2')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tar_values = tar_by_paziente['%TARLV2']
#
# # Statistiche descrittive
# media = tar_values.mean()
# mediana = tar_values.median()
# asimmetria = skew(tar_values) #skewness
# curtosi = kurtosis(tar_values)
#
# tar_arrotondato = tar_values.round()
# moda = tar_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# # calcola Q1, Q3 e IQR
# q1 = tar_values.quantile(0.25)
# q3 = tar_values.quantile(0.75)
# iqr = q3 - q1
#
# # soglie per outlier
# lower_thr = q1 - 1.5 * iqr
# upper_thr = q3 + 1.5 * iqr
#
# print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
# print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
# outliers = tar_values[(tar_values < lower_thr) | (tar_values > upper_thr)]
# print("Valori TARLV2 considerati outlier:")
# print(outliers.sort_values().to_list())
#
#
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################


# ANALISI TBR
############################################################################################
# # Funzione per calcolare il TBR di un paziente
# def calculate_tbr(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] < 70)] # Seleziona solo le righe che nel campo Measurement hanno un valore minore di 70 mg/dL
#     tbr = len(righe_valide)/totale * 100 # Calcola il %TBR facendo Misurazioni Valide/Misurazioni Totali
#     return tbr
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tbr_by_paziente = pazienti.apply(calculate_tbr).reset_index(name='%TBR') # Calcoliamo il TBR di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TBR
# # tbr_by_paziente = tbr_by_paziente.sort_values(by='%TBR', ascending=False)
# print(tbr_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tbr_by_paziente['Patient_ID'], tbr_by_paziente['%TBR'], color='skyblue')
# plt.xticks([])
# plt.ylabel('% Time Below Range (< 70 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TBR
# print(tbr_by_paziente['%TBR'].describe())
#
# # Raggruppiamo i valori di %TBR in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tbr_intervals = pd.cut(tbr_by_paziente['%TBR'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tbr_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TBR
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='skyblue', edgecolor='black')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TBR')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tbr_values = tbr_by_paziente['%TBR']
#
# # Statistiche descrittive
# media = tbr_values.mean()
# mediana = tbr_values.median()
# asimmetria = skew(tbr_values) #skewness
# curtosi = kurtosis(tbr_values)
#
# tar_arrotondato = tbr_values.round()
# moda = tar_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# # calcola Q1, Q3 e IQR
# q1 = tbr_values.quantile(0.25)
# q3 = tbr_values.quantile(0.75)
# iqr = q3 - q1
#
# # soglie per outlier
# lower_thr = q1 - 1.5 * iqr
# upper_thr = q3 + 1.5 * iqr
#
# print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
# print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
# outliers = tbr_values[(tbr_values < lower_thr) | (tbr_values > upper_thr)]
# print("Valori TBR considerati outlier:")
# print(outliers.sort_values().to_list())
#
#
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################


# ANALISI TBR LV1
############################################################################################
# # Funzione per calcolare il TBRLV1 di un paziente
# def calculate_tbr(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] >= 54) & (misurazioni['Measurement'] < 70)] # Seleziona solo le righe che nel campo Measurement hanno un valore compreso tra 54 e 70 mg/dL
#     tbr = len(righe_valide)/totale * 100 # Calcola il %TBRLV1 facendo Misurazioni Valide/Misurazioni Totali
#     return tbr
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tbr_by_paziente = pazienti.apply(calculate_tbr).reset_index(name='%TBRLV1') # Calcoliamo il TBRLV1 di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TBRLV1
# # tbr_by_paziente = tbr_by_paziente.sort_values(by='%TBRLV1', ascending=False)
# print(tbr_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tbr_by_paziente['Patient_ID'], tbr_by_paziente['%TBRLV1'], color='#ffa07a')
# plt.xticks([])
# plt.ylabel('% Time Below Range (54 - 70 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TBRLV1
# print(tbr_by_paziente['%TBRLV1'].describe())
#
# # Raggruppiamo i valori di %TBRLV1 in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tbr_intervals = pd.cut(tbr_by_paziente['%TBRLV1'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tbr_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TBRLV1
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='#ffa07a', edgecolor='black')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TBRLV1')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tbr_values = tbr_by_paziente['%TBRLV1']
#
# # Statistiche descrittive
# media = tbr_values.mean()
# mediana = tbr_values.median()
# asimmetria = skew(tbr_values) #skewness
# curtosi = kurtosis(tbr_values)
#
# tar_arrotondato = tbr_values.round()
# moda = tar_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# # calcola Q1, Q3 e IQR
# q1 = tbr_values.quantile(0.25)
# q3 = tbr_values.quantile(0.75)
# iqr = q3 - q1
#
# # soglie per outlier
# lower_thr = q1 - 1.5 * iqr
# upper_thr = q3 + 1.5 * iqr
#
# print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
# print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
# outliers = tbr_values[(tbr_values < lower_thr) | (tbr_values > upper_thr)]
# print("Valori TBRLV1 considerati outlier:")
# print(outliers.sort_values().to_list())
#
#
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################


# ANALISI TBR LV2
############################################################################################
# # Funzione per calcolare il TBRLV2 di un paziente
# def calculate_tbr(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] < 54)] # Seleziona solo le righe che nel campo Measurement hanno un valore minore di 54 mg/dL
#     tbr = len(righe_valide)/totale * 100 # Calcola il %TBRLV2 facendo Misurazioni Valide/Misurazioni Totali
#     return tbr
#
# pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tbr_by_paziente = pazienti.apply(calculate_tbr).reset_index(name='%TBRLV2') # Calcoliamo il TBRLV2 di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TBRLV2
# # tbr_by_paziente = tbr_by_paziente.sort_values(by='%TBRLV2', ascending=False)
# print(tbr_by_paziente)
#
# # Grafico per la percentuale di ogni paziente
# plt.figure(figsize=(14, 6))
# plt.bar(tbr_by_paziente['Patient_ID'], tbr_by_paziente['%TBRLV2'], color='#e64100')
# plt.xticks([])
# plt.ylabel('% Time Below Range (< 54 mg/dL)')
# plt.xlabel('Pazienti')
# plt.title('')
# plt.tight_layout()
# plt.show()
#
# # Statistiche descrittive di %TBRLV2
# print(tbr_by_paziente['%TBRLV2'].describe())
#
# # Raggruppiamo i valori di %TBRLV2 in intervalli di 5% (es. 0-5%, 5-10%, ..., 95-100%)
# tbr_intervals = pd.cut(tbr_by_paziente['%TBRLV2'], bins=range(0, 110, 10), right=False)  #Notazione [0,10) 0 é incluso ma 10 no
#
# # Conteggio dei pazienti per ciascun intervallo
# pazienti_per_interval = tbr_intervals.value_counts().sort_index()
#
# print(pazienti_per_interval)
#
# # Istogramma del numero di pazienti per ciascun intervallo di %TBRLV2
# plt.figure(figsize=(10, 6))
# bars = pazienti_per_interval.plot(kind='bar', color='#e64100', edgecolor='black')
#
# for bar in bars.patches:
#     height = bar.get_height()  # Otteniamo l'altezza della barra (numero di pazienti)
#     bar.set_edgecolor('black')  # Impostiamo il bordo della barra
#     bar.set_linewidth(1)  # Impostiamo lo spessore del bordo
#     plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, int(height),
#              ha='center', va='bottom', fontsize=10, color='black')
#
# plt.title('')
# plt.xlabel('%TBRLV2')
# plt.ylabel('Numero di Pazienti')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
#
#
# tbr_values = tbr_by_paziente['%TBRLV2']
#
# # Statistiche descrittive
# media = tbr_values.mean()
# mediana = tbr_values.median()
# asimmetria = skew(tbr_values) #skewness
# curtosi = kurtosis(tbr_values)
#
# tar_arrotondato = tbr_values.round()
# moda = tar_arrotondato.mode()
#
# # Outlier con metodo IQR (Interquartile Range)
# # calcola Q1, Q3 e IQR
# q1 = tbr_values.quantile(0.25)
# q3 = tbr_values.quantile(0.75)
# iqr = q3 - q1
#
# # soglie per outlier
# lower_thr = q1 - 1.5 * iqr
# upper_thr = q3 + 1.5 * iqr
#
# print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
# print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
# outliers = tbr_values[(tbr_values < lower_thr) | (tbr_values > upper_thr)]
# print("Valori TBRLV2 considerati outlier:")
# print(outliers.sort_values().to_list())
#
#
#
# # Output
# print(f"Media: {media:.2f}")
# print(f"Mediana: {mediana:.2f}")
# print(f"Asimmetria (skewness): {asimmetria:.2f}")
# print(f"Curtosi (kurtosis): {curtosi:.2f}")
# print(f"Numero di outlier: {len(outliers)}")
# print("Moda:", moda.tolist())
############################################################################################