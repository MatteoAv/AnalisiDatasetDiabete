import pandas as pd
import matplotlib.pyplot as plt
from pywin.framework.editor.ModuleBrowser import HierListCLBRErrorItem
from scipy.stats import skew, kurtosis
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from datetime import datetime, timedelta
from scipy.stats import mannwhitneyu

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
diagnostics = pd.read_csv("Excel/Diagnostics.csv")

# df = df[(df['Measurement'].notna()) & (df['Measurement'] >= 40) &  (df['Measurement'] <= 500)]
# Pulizia del dataset per eliminare valori di glucosio nulli o fisiologicamente impossibili (comunque non ce ne sono)

# ANALISI TIR
############################################################################################
# # Funzione per calcolare il TIR di un paziente
# def calculate_tir(misurazioni):  # Prende in ingresso l'insieme di misurazioni di un singolo paziente
#     totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
#     righe_valide = misurazioni[(misurazioni['Measurement'] >= 70) & (misurazioni['Measurement'] <= 180)]  # Seleziona solo le righe che nel campo Measurement hanno un valore compreso tra 70 e 180 mg/dL
#     tir = len(righe_valide)/totale * 100  # Calcola il %TIR facendo Misurazioni Valide / Misurazioni Totali
#     return tir
#
# pazienti = df.groupby('Patient_ID')  # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
# tir_by_paziente = pazienti.apply(calculate_tir).reset_index(name='%TIR')  # Calcoliamo il TIR di ogni paziente e creiamo un nuovo dataset con 2 colonne: Patient_ID e %TIR
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
# # Raggruppiamo i valori di %TIR in intervalli (0,1), [1,10), [10,20), ...
# bins = [0, 1] + list(range(10, 110, 10))
# tir_intervals = pd.cut(tir_by_paziente['%TIR'], bins=bins, right=False)
#
# # Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
# pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
# tir_by_paziente['Has_Diagnosis'] = tir_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # Aggiungiamo anche gli intervalli nel dataframe
# tir_by_paziente['Interval'] = tir_intervals
#
# # Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
# conta_per_interval = tir_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
# conta_per_interval = conta_per_interval.sort_index()
#
# # Istogramma con due barre affiancate per ogni intervallo, con etichette
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index = range(len(conta_per_interval))
#
# bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# # Aggiunta delle etichette numeriche sopra ogni barra
# for bars in [bar1, bar2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)
#
#
# plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
# plt.xlabel('%TIR')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
# # Estrai le due serie
# g0 = tir_by_paziente.loc[ tir_by_paziente['Has_Diagnosis']==False, '%TIR']
# g1 = tir_by_paziente.loc[ tir_by_paziente['Has_Diagnosis']==True,  '%TIR']
#
# # Esegui il test two-sided
# u_stat, p_value = mannwhitneyu(g0, g1, alternative='two-sided')
#
# print(f"U-statistic = {u_stat:.2f}")
# print(f"p-value      = {p_value:.4f}")


# # STATISTICHE DESCRITTIVE
# tir_values = tir_by_paziente['%TIR']
#
# media = tir_values.mean()
# mediana = tir_values.median()
# asimmetria = skew(tir_values)  # skewness
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
#
#
#
# # 1) Converto Measurement_date in datetime
# df['Measurement_date'] = pd.to_datetime(df['Measurement_date'])
#
# # 2) Calcolo la prima data di misurazione per ogni paziente
# first_dates = df.groupby('Patient_ID')['Measurement_date'].min().rename('FirstDate')
# df = df.join(first_dates, on='Patient_ID')
#
# # 3) Seleziono misurazioni entro 3 mesi dalla data iniziale
# df_3m = df[df['Measurement_date'] <= df['FirstDate'] + pd.DateOffset(months=3)]
#
# # 4) Calcolo il TIR sui primi 3 mesi
# pazienti_3m = df_3m.groupby('Patient_ID')
# tir3m_by_paziente = pazienti_3m.apply(calculate_tir).reset_index(name='%TIR_3m')
#
# # 5) Aggiungo il flag di diagnosi
# tir3m_by_paziente['Has_Diagnosis'] = tir3m_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # 6) Creo gli stessi intervalli usati prima su %TIR_3m
# tir3m_by_paziente['Interval'] = pd.cut(tir3m_by_paziente['%TIR_3m'], bins=bins, right=False)
#
# # 7) Raggruppo e conto
# conta_per_interval_3m = tir3m_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0).sort_index()
#
# # 8) Disegno l’istogramma a barre affiancate
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index_3m = range(len(conta_per_interval_3m))
#
# bar1_3m = plt.bar([i - bar_width/2 for i in index_3m], conta_per_interval_3m[False],
#                    width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2_3m = plt.bar([i + bar_width/2 for i in index_3m], conta_per_interval_3m[True],
#                    width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# for bars in (bar1_3m, bar2_3m):
#     for bar in bars:
#         h = bar.get_height()
#         if h > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, h + 0.5, str(int(h)),
#                      ha='center', va='bottom', fontsize=9)
#
# plt.xticks(index_3m, [str(i) for i in conta_per_interval_3m.index], rotation=45)
# plt.xlabel('%TIR_3m')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
# # 9) Statistiche descrittive per %TIR_3m (facoltativo)
# print(tir3m_by_paziente['%TIR_3m'].describe())


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
# bins = [0, 1] + list(range(10, 110, 10))
# tar_intervals = pd.cut(tar_by_paziente['%TAR'], bins=bins, right=False)
# #Notazione [0,10) 0 é incluso ma 10 no
#
# # Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
# pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
# tar_by_paziente['Has_Diagnosis'] = tar_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # Aggiungiamo anche gli intervalli nel dataframe
# tar_by_paziente['Interval'] = tar_intervals
#
# # Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
# conta_per_interval = tar_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
# conta_per_interval = conta_per_interval.sort_index()
#
# # Istogramma con due barre affiancate per ogni intervallo, con etichette
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index = range(len(conta_per_interval))
#
# bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# # Aggiunta delle etichette numeriche sopra ogni barra
# for bars in [bar1, bar2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)
#
#
# plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
# plt.xlabel('%TAR')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
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
#
#
# # Estrai le due serie
# g0 = tar_by_paziente.loc[ tar_by_paziente['Has_Diagnosis']==False, '%TAR']
# g1 = tar_by_paziente.loc[ tar_by_paziente['Has_Diagnosis']==True,  '%TAR']
#
# # Esegui il test two-sided
# u_stat, p_value = mannwhitneyu(g0, g1, alternative='two-sided')
#
# print(f"U-statistic = {u_stat:.2f}")
# print(f"p-value      = {p_value:.4f}")
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
# bins = [0, 1] + list(range(10, 110, 10))
# tar_intervals = pd.cut(tar_by_paziente['%TARLV1'], bins=bins, right=False)
# #Notazione [0,10) 0 é incluso ma 10 no
#
# # Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
# pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
# tar_by_paziente['Has_Diagnosis'] = tar_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # Aggiungiamo anche gli intervalli nel dataframe
# tar_by_paziente['Interval'] = tar_intervals
#
# # Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
# conta_per_interval = tar_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
# conta_per_interval = conta_per_interval.sort_index()
#
#
# # Istogramma con due barre affiancate per ogni intervallo, con etichette
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index = range(len(conta_per_interval))
#
# bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# # Aggiunta delle etichette numeriche sopra ogni barra
# for bars in [bar1, bar2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)
#
#
# plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
# plt.xlabel('%TARLV1')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
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
#
#
# # 1) Converto Measurement_date in datetime
# df['Measurement_date'] = pd.to_datetime(df['Measurement_date'])
#
# # 2) Calcolo la prima data di misurazione per ogni paziente
# first_dates = df.groupby('Patient_ID')['Measurement_date'].min().rename('FirstDate')
# df = df.join(first_dates, on='Patient_ID')
#
# # 3) Seleziono misurazioni entro 3 mesi dalla data iniziale
# df_3m = df[df['Measurement_date'] <= df['FirstDate'] + pd.DateOffset(months=3)]
#
# # 4) Calcolo il TIR sui primi 3 mesi
# pazienti_3m = df_3m.groupby('Patient_ID')
# tar3m_by_paziente = pazienti_3m.apply(calculate_tar).reset_index(name='%TARLV1_3m')
#
# # 5) Aggiungo il flag di diagnosi
# tar3m_by_paziente['Has_Diagnosis'] = tar3m_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # 6) Creo gli stessi intervalli usati prima su %TIR_3m
# tar3m_by_paziente['Interval'] = pd.cut(tar3m_by_paziente['%TARLV1_3m'], bins=bins, right=False)
#
# # 7) Raggruppo e conto
# conta_per_interval_3m = tar3m_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0).sort_index()
#
# # 8) Disegno l’istogramma a barre affiancate
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index_3m = range(len(conta_per_interval_3m))
#
# bar1_3m = plt.bar([i - bar_width/2 for i in index_3m], conta_per_interval_3m[False],
#                    width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2_3m = plt.bar([i + bar_width/2 for i in index_3m], conta_per_interval_3m[True],
#                    width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# for bars in (bar1_3m, bar2_3m):
#     for bar in bars:
#         h = bar.get_height()
#         if h > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, h + 0.5, str(int(h)),
#                      ha='center', va='bottom', fontsize=9)
#
# plt.xticks(index_3m, [str(i) for i in conta_per_interval_3m.index], rotation=45)
# plt.xlabel('%TARLV1_3m')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
# # 9) Statistiche descrittive per %TIR_3m (facoltativo)
# print(tar3m_by_paziente['%TARLV1_3m'].describe())
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
# bins = [0, 1] + list(range(10, 110, 10))
# tar_intervals = pd.cut(tar_by_paziente['%TARLV2'], bins=bins, right=False)
# #Notazione [0,10) 0 é incluso ma 10 no
#
# # Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
# pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
# tar_by_paziente['Has_Diagnosis'] = tar_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # Aggiungiamo anche gli intervalli nel dataframe
# tar_by_paziente['Interval'] = tar_intervals
#
# # Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
# conta_per_interval = tar_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
# conta_per_interval = conta_per_interval.sort_index()
#
# # Istogramma con due barre affiancate per ogni intervallo, con etichette
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index = range(len(conta_per_interval))
#
# bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# # Aggiunta delle etichette numeriche sopra ogni barra
# for bars in [bar1, bar2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)
#
#
# plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
# plt.xlabel('%TARLV2')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
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
#
#
# # 1) Converto Measurement_date in datetime
# df['Measurement_date'] = pd.to_datetime(df['Measurement_date'])
#
# # 2) Calcolo la prima data di misurazione per ogni paziente
# first_dates = df.groupby('Patient_ID')['Measurement_date'].min().rename('FirstDate')
# df = df.join(first_dates, on='Patient_ID')
#
# # 3) Seleziono misurazioni entro 3 mesi dalla data iniziale
# df_3m = df[df['Measurement_date'] <= df['FirstDate'] + pd.DateOffset(months=3)]
#
# # 4) Calcolo il TIR sui primi 3 mesi
# pazienti_3m = df_3m.groupby('Patient_ID')
# tar3m_by_paziente = pazienti_3m.apply(calculate_tar).reset_index(name='%TARLV2_3m')
#
# # 5) Aggiungo il flag di diagnosi
# tar3m_by_paziente['Has_Diagnosis'] = tar3m_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # 6) Creo gli stessi intervalli usati prima su %TIR_3m
# tar3m_by_paziente['Interval'] = pd.cut(tar3m_by_paziente['%TARLV2_3m'], bins=bins, right=False)
#
# # 7) Raggruppo e conto
# conta_per_interval_3m = tar3m_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0).sort_index()
#
# # 8) Disegno l’istogramma a barre affiancate
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index_3m = range(len(conta_per_interval_3m))
#
# bar1_3m = plt.bar([i - bar_width/2 for i in index_3m], conta_per_interval_3m[False],
#                    width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2_3m = plt.bar([i + bar_width/2 for i in index_3m], conta_per_interval_3m[True],
#                    width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# for bars in (bar1_3m, bar2_3m):
#     for bar in bars:
#         h = bar.get_height()
#         if h > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, h + 0.5, str(int(h)),
#                      ha='center', va='bottom', fontsize=9)
#
# plt.xticks(index_3m, [str(i) for i in conta_per_interval_3m.index], rotation=45)
# plt.xlabel('%TARLV2_3m')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
# # 9) Statistiche descrittive per %TIR_3m (facoltativo)
# print(tar3m_by_paziente['%TARLV2_3m'].describe())
############################################################################################


# ANALISI TBR
############################################################################################
# Funzione per calcolare il TBR di un paziente
def calculate_tbr(misurazioni): # Prende in ingresso l'insieme di misurazioni di un singolo paziente
    totale = len(misurazioni)   # Calcola il numero totale di misurazioni del paziente
    righe_valide = misurazioni[(misurazioni['Measurement'] < 70)] # Seleziona solo le righe che nel campo Measurement hanno un valore minore di 70 mg/dL
    tbr = len(righe_valide)/totale * 100 # Calcola il %TBR facendo Misurazioni Valide/Misurazioni Totali
    return tbr

pazienti = df.groupby('Patient_ID') # Dividiamo il dataset per paziente, ogni gruppo contiene le misurazioni di un singolo paziente
tbr_by_paziente = pazienti.apply(calculate_tbr).reset_index(name='%TBR') # Calcoliamo il TBR di ogni paziente e creiamo un nuovo dataset con 2 colonne: Ptient_ID e %TBR
# tbr_by_paziente = tbr_by_paziente.sort_values(by='%TBR', ascending=False)
print(tbr_by_paziente)

# Grafico per la percentuale di ogni paziente
plt.figure(figsize=(14, 6))
plt.bar(tbr_by_paziente['Patient_ID'], tbr_by_paziente['%TBR'], color='skyblue')
plt.xticks([])
plt.ylabel('% Time Below Range (< 70 mg/dL)')
plt.xlabel('Pazienti')
plt.title('')
plt.tight_layout()
plt.show()

# Statistiche descrittive di %TBR
print(tbr_by_paziente['%TBR'].describe())

bins = [0, 1] + list(range(10, 110, 10))
tbr_intervals = pd.cut(tbr_by_paziente['%TBR'], bins=bins, right=False)
#Notazione [0,10) 0 é incluso ma 10 no

# Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
tbr_by_paziente['Has_Diagnosis'] = tbr_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)

# Aggiungiamo anche gli intervalli nel dataframe
tbr_by_paziente['Interval'] = tbr_intervals

# Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
conta_per_interval = tbr_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
conta_per_interval = conta_per_interval.sort_index()


# Istogramma con due barre affiancate per ogni intervallo, con etichette
plt.figure(figsize=(12, 6))
bar_width = 0.4
index = range(len(conta_per_interval))

bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')

# Aggiunta delle etichette numeriche sopra ogni barra
for bars in [bar1, bar2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)


plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
plt.xlabel('%TBR')
plt.ylabel('Numero di Pazienti')
plt.title('')
plt.legend()
plt.tight_layout()
plt.show()



tbr_values = tbr_by_paziente['%TBR']

# Statistiche descrittive
media = tbr_values.mean()
mediana = tbr_values.median()
asimmetria = skew(tbr_values) #skewness
curtosi = kurtosis(tbr_values)

tar_arrotondato = tbr_values.round()
moda = tar_arrotondato.mode()

# Outlier con metodo IQR (Interquartile Range)
# calcola Q1, Q3 e IQR
q1 = tbr_values.quantile(0.25)
q3 = tbr_values.quantile(0.75)
iqr = q3 - q1

# soglie per outlier
lower_thr = q1 - 1.5 * iqr
upper_thr = q3 + 1.5 * iqr

print(f"Q1 = {q1:.2f}%, Q3 = {q3:.2f}%, IQR = {iqr:.2f}%")
print(f"Soglia inferiore = {lower_thr:.2f}%, soglia superiore = {upper_thr:.2f}%")
outliers = tbr_values[(tbr_values < lower_thr) | (tbr_values > upper_thr)]
print("Valori TBR considerati outlier:")
print(outliers.sort_values().to_list())



# Output
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Asimmetria (skewness): {asimmetria:.2f}")
print(f"Curtosi (kurtosis): {curtosi:.2f}")
print(f"Numero di outlier: {len(outliers)}")
print("Moda:", moda.tolist())

# Estrai le due serie
g0 = tbr_by_paziente.loc[ tbr_by_paziente['Has_Diagnosis']==False, '%TBR']
g1 = tbr_by_paziente.loc[ tbr_by_paziente['Has_Diagnosis']==True,  '%TBR']

# Esegui il test two-sided
u_stat, p_value = mannwhitneyu(g0, g1, alternative='two-sided')

print(f"U-statistic = {u_stat:.2f}")
print(f"p-value      = {p_value:.4f}")
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
# bins = [0, 1] + list(range(10, 110, 10))
# tbr_intervals = pd.cut(tbr_by_paziente['%TBRLV1'], bins=bins, right=False)
# #Notazione [0,10) 0 é incluso ma 10 no
#
# # Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
# pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
# tbr_by_paziente['Has_Diagnosis'] = tbr_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # Aggiungiamo anche gli intervalli nel dataframe
# tbr_by_paziente['Interval'] = tbr_intervals
#
# # Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
# conta_per_interval = tbr_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
# conta_per_interval = conta_per_interval.sort_index()
#
# # Istogramma con due barre affiancate per ogni intervallo, con etichette
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index = range(len(conta_per_interval))
#
# bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# # Aggiunta delle etichette numeriche sopra ogni barra
# for bars in [bar1, bar2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)
#
#
# plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
# plt.xlabel('%TBRLV1')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
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
#
#
#
# # 1) Converto Measurement_date in datetime
# df['Measurement_date'] = pd.to_datetime(df['Measurement_date'])
#
# # 2) Calcolo la prima data di misurazione per ogni paziente
# first_dates = df.groupby('Patient_ID')['Measurement_date'].min().rename('FirstDate')
# df = df.join(first_dates, on='Patient_ID')
#
# # 3) Seleziono misurazioni entro 3 mesi dalla data iniziale
# df_3m = df[df['Measurement_date'] <= df['FirstDate'] + pd.DateOffset(months=3)]
#
# # 4) Calcolo il TIR sui primi 3 mesi
# pazienti_3m = df_3m.groupby('Patient_ID')
# tbr3m_by_paziente = pazienti_3m.apply(calculate_tbr).reset_index(name='%TBRLV1_3m')
#
# # 5) Aggiungo il flag di diagnosi
# tbr3m_by_paziente['Has_Diagnosis'] = tbr3m_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # 6) Creo gli stessi intervalli usati prima su %TIR_3m
# tbr3m_by_paziente['Interval'] = pd.cut(tbr3m_by_paziente['%TBRLV1_3m'], bins=bins, right=False)
#
# # 7) Raggruppo e conto
# conta_per_interval_3m = tbr3m_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0).sort_index()
#
# # 8) Disegno l’istogramma a barre affiancate
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index_3m = range(len(conta_per_interval_3m))
#
# bar1_3m = plt.bar([i - bar_width/2 for i in index_3m], conta_per_interval_3m[False],
#                    width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2_3m = plt.bar([i + bar_width/2 for i in index_3m], conta_per_interval_3m[True],
#                    width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# for bars in (bar1_3m, bar2_3m):
#     for bar in bars:
#         h = bar.get_height()
#         if h > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, h + 0.5, str(int(h)),
#                      ha='center', va='bottom', fontsize=9)
#
# plt.xticks(index_3m, [str(i) for i in conta_per_interval_3m.index], rotation=45)
# plt.xlabel('%TBRLV1_3m')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
# # 9) Statistiche descrittive per %TIR_3m (facoltativo)
# print(tbr3m_by_paziente['%TBRLV1_3m'].describe())
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
# bins = [0, 1] + list(range(10, 110, 10))
# tbr_intervals = pd.cut(tbr_by_paziente['%TBRLV2'], bins=bins, right=False)
# #Notazione [0,10) 0 é incluso ma 10 no
#
# # Aggiungiamo colonna per sapere se il paziente ha almeno una diagnosi
# pazienti_con_diagnosi = set(diagnostics['Patient_ID'])
# tbr_by_paziente['Has_Diagnosis'] = tbr_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # Aggiungiamo anche gli intervalli nel dataframe
# tbr_by_paziente['Interval'] = tbr_intervals
#
# # Calcoliamo il numero di pazienti CON e SENZA diagnosi per ogni intervallo
# conta_per_interval = tbr_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0)
# conta_per_interval = conta_per_interval.sort_index()
#
# # Istogramma con due barre affiancate per ogni intervallo, con etichette
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index = range(len(conta_per_interval))
#
# bar1 = plt.bar([i - bar_width/2 for i in index], conta_per_interval[False], width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2 = plt.bar([i + bar_width/2 for i in index], conta_per_interval[True], width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# # Aggiunta delle etichette numeriche sopra ogni barra
# for bars in [bar1, bar2]:
#     for bar in bars:
#         height = bar.get_height()
#         if height > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=9)
#
#
# plt.xticks(index, [str(i) for i in conta_per_interval.index], rotation=45)
# plt.xlabel('%TBRLV2')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
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
#
#
#
# # 1) Converto Measurement_date in datetime
# df['Measurement_date'] = pd.to_datetime(df['Measurement_date'])
#
# # 2) Calcolo la prima data di misurazione per ogni paziente
# first_dates = df.groupby('Patient_ID')['Measurement_date'].min().rename('FirstDate')
# df = df.join(first_dates, on='Patient_ID')
#
# # 3) Seleziono misurazioni entro 3 mesi dalla data iniziale
# df_3m = df[df['Measurement_date'] <= df['FirstDate'] + pd.DateOffset(months=3)]
#
# # 4) Calcolo il TIR sui primi 3 mesi
# pazienti_3m = df_3m.groupby('Patient_ID')
# tbr3m_by_paziente = pazienti_3m.apply(calculate_tbr).reset_index(name='%TBRLV2_3m')
#
# # 5) Aggiungo il flag di diagnosi
# tbr3m_by_paziente['Has_Diagnosis'] = tbr3m_by_paziente['Patient_ID'].isin(pazienti_con_diagnosi)
#
# # 6) Creo gli stessi intervalli usati prima su %TIR_3m
# tbr3m_by_paziente['Interval'] = pd.cut(tbr3m_by_paziente['%TBRLV2_3m'], bins=bins, right=False)
#
# # 7) Raggruppo e conto
# conta_per_interval_3m = tbr3m_by_paziente.groupby(['Interval', 'Has_Diagnosis']).size().unstack(fill_value=0).sort_index()
#
# # 8) Disegno l’istogramma a barre affiancate
# plt.figure(figsize=(12, 6))
# bar_width = 0.4
# index_3m = range(len(conta_per_interval_3m))
#
# bar1_3m = plt.bar([i - bar_width/2 for i in index_3m], conta_per_interval_3m[False],
#                    width=bar_width, label='Senza Complicanze', color='skyblue', edgecolor='black')
# bar2_3m = plt.bar([i + bar_width/2 for i in index_3m], conta_per_interval_3m[True],
#                    width=bar_width, label='Con Complicanze', color='lightcoral', edgecolor='black')
#
# for bars in (bar1_3m, bar2_3m):
#     for bar in bars:
#         h = bar.get_height()
#         if h > 0:
#             plt.text(bar.get_x() + bar.get_width()/2, h + 0.5, str(int(h)),
#                      ha='center', va='bottom', fontsize=9)
#
# plt.xticks(index_3m, [str(i) for i in conta_per_interval_3m.index], rotation=45)
# plt.xlabel('%TBRLV2_3m')
# plt.ylabel('Numero di Pazienti')
# plt.title('')
# plt.legend()
# plt.tight_layout()
# plt.show()
#
# # 9) Statistiche descrittive per %TIR_3m (facoltativo)
# print(tbr3m_by_paziente['%TBRLV2_3m'].describe())
############################################################################################


#CREAZIONE DATASET CON DATA E VALORE DEI PARAMETRI BIOCHIMICI E NUMERO DI MISURAZIONI DEL GLUCOSIO CON RELATIVO VALORE MEDIO FATTO IN UN INTORNO DI 3 GIORNI DA QUELLA DATA
############################################################################################

# # Carica e prepara i dati
# df_glucose = pd.read_csv("Excel/Glucose_measurements.csv", parse_dates=["Measurement_date"])
# df_bio = pd.read_csv("Excel/Biochemical_parameters.csv", parse_dates=["Reception_date"])
#
# from tqdm import tqdm
#
#
# records = []
#
# # Ottieni i pazienti presenti in entrambi i dataset
# common_patients = set(df_bio['Patient_ID']).intersection(set(df_glucose['Patient_ID']))
#
# # Loop per paziente
# for pid in tqdm(common_patients): #per ogni paziente in comune, mostrando la barra di avanzamento
#     glucose_p = df_glucose[df_glucose['Patient_ID'] == pid].copy() #prendi tutte le righe di glucosio e di parametri biochimici per quel paziente
#     bio_p = df_bio[df_bio['Patient_ID'] == pid].copy()
#
#     # Ordina le misurazioni di glucosio cronologicamente
#     glucose_p.sort_values("Measurement_date", inplace=True)
#
#     #per ogni parametro biochimico del paziente estrae la data ed il valore
#     for _, bio_row in bio_p.iterrows():
#         reception_date = bio_row["Reception_date"]
#         param_name = bio_row["Name"]
#         param_value = bio_row["Value"]
#
#         # Trova misurazioni di glucosio entro ±3 giorni
#         # Costruisce una mask che é TRUE per tutte le righe in glucose_p la cui data é compresa entro 3 giorni da reception_date di bio_p
#         mask = (
#                 (glucose_p["Measurement_date"] >= reception_date - timedelta(days=3)) &
#                 (glucose_p["Measurement_date"] <= reception_date + timedelta(days=3))
#         )
#         #crea un sotto-dataset contenente solo le letture di glucosio che rispettano la mashera, cioe l'intervallo di 3 giorni
#         nearby = glucose_p[mask]
#
#         #se il dataframe creato non é vuoto si aggiungono anche gli altri parametri e si fa l'append di questo a records definito prima
#         if not nearby.empty:
#             records.append({
#                 "Patient_ID": pid,
#                 "Parameter": param_name,
#                 "Parameter_Value": param_value,
#                 "Reception_Date": reception_date,
#                 "Avg_Glucose": nearby["Measurement"].mean(),
#                 "Num_Glucose_Readings": len(nearby)
#             })
#
# # 1) Trasforma records in DataFrame
# df_results = pd.DataFrame(records)
#
# # 2) Salvalo in CSV nella cartella Excel
# output_path = "Excel/glucose_bio_correlated.csv"
# df_results.to_csv(output_path, index=False)
#
# print(f"Saved {len(df_results)} rows to {output_path}")
############################################################################################


#SCATTERPLOT - RELAZIONE TRA VALORI DI GLUCOSIO E VALORI DELLE ANALISI FATTE
############################################################################################
# df2 = pd.read_csv("Excel/glucose_bio_correlated.csv", parse_dates=["Reception_Date"])
# diagnostics = pd.read_csv("Excel/Diagnostics.csv")
#
# max_param_value = df2["Parameter_Value"].max()  #Valore massimo
# row_max_param = df2.loc[df2["Parameter_Value"].idxmax()] #Indice di riga del valore massimo, .loc estrae l'intera riga
#
# max_avg_glucose = df2["Avg_Glucose"].max()
# row_max_gluc = df2.loc[df2["Avg_Glucose"].idxmax()]
#
# #Stampa dei valori massimi e relativi indici di riga
# print(f"Massimo Parameter_Value: {max_param_value}")
# print("Record corrispondente:")
# print(row_max_param)
# print(f"\nMassimo Avg_Glucose: {max_avg_glucose}")
# print("Record corrispondente:")
# print(row_max_gluc)
#
# # trasforma la colonna Patient_ID di diagnostics in un insieme e crea una nuova colonna di booleani
# # se il paziente preso in considerazione si trova nel dataset diagnostics allora la nuova colonna Has_Diagnosis diventa True, altrimenti False
# diagnosed_patients = set(diagnostics["Patient_ID"])
# df2["Has_Diagnosis"] = df2["Patient_ID"].isin(diagnosed_patients)
#
# #Preparazione diagrammi, n indica il numero di diagrammi da stampare (17), e poi vengono messe righe e colonne
# params = df2["Parameter"].unique()
# n = len(params)
# cols = 4
# rows = (n + cols - 1) // cols
#
# #Calcoliamo minimi e massimi dei valori che dobbiamo rappresentare sugli scatterplot, in modo che nelle 3 rappresentazioni differenti
# #l'asse delle scisse e quella delle ordinate abbia sempre gli stessi valori
# limits = {}
# for param in params:
#     sub = df2[df2["Parameter"] == param]
#     x_min, x_max = sub["Parameter_Value"].min(), sub["Parameter_Value"].max()
#     y_min, y_max = sub["Avg_Glucose"].min(), sub["Avg_Glucose"].max()
#     x_pad = (x_max - x_min) * 0.05
#     y_pad = (y_max - y_min) * 0.05
#     limits[param] = {
#         "xlim": (x_min - x_pad, x_max + x_pad),
#         "ylim": (y_min - y_pad, y_max + y_pad)
#     }
#
# #Funzione di plot per gruppi, con limiti fissi
# def plot_group(df_subset, title, blue=True, red=True):
#     fig, axes = plt.subplots(rows, cols, figsize=(cols*4, rows*3))
#     axes = axes.flatten()
#     for ax, param in zip(axes, params):
#         sub = df_subset[df_subset["Parameter"] == param]
#         if blue:
#             ax.scatter(
#                 sub[~sub["Has_Diagnosis"]]["Parameter_Value"], #Seleziona solo le righe di sub con pazienti senza complicanze
#                 sub[~sub["Has_Diagnosis"]]["Avg_Glucose"],
#                 facecolors='none', edgecolors='blue', marker='o',
#                 linewidths=1, label='No Complicanze'
#             )
#         if red:
#             ax.scatter(
#                 sub[sub["Has_Diagnosis"]]["Parameter_Value"], #Seleziona solo le righe di sub con pazienti con complicanze
#                 sub[sub["Has_Diagnosis"]]["Avg_Glucose"],
#                 facecolors='none', edgecolors='red', marker='o',
#                 linewidths=1, label='Con Complicanze'
#             )
#         # Applica limiti calcolati
#         ax.set_xlim(limits[param]["xlim"])
#         ax.set_ylim(limits[param]["ylim"])
#         ax.set_title(param, fontsize=8)
#         ax.set_xlabel("Param value", fontsize=6)
#         ax.set_ylabel("Avg Glucose", fontsize=6)
#         ax.legend(fontsize=6)
#     # Nascondi assi in eccesso
#     for ax in axes[n:]:
#         ax.set_visible(False)
#     fig.suptitle(title, fontsize=12, y=1.02)
#     plt.tight_layout()
#     return fig
#
# #Figura 1: combinato blu+rosso
# plot_group(df2, "Tutti i pazienti: Con e Senza complicanze", blue=True, red=True)
#
# #Figura 2: solo CON diagnosi (rosso)
# plot_group(df2, "Solo pazienti CON complicanze", blue=False, red=True)
#
# #Figura 3: solo SENZA diagnosi (blu)
# plot_group(df2, "Solo pazienti SENZA complicanze", blue=True, red=False)
#
# plt.show()
#
# #BOXPLOT - RELAZIONE TRA VALORI DI GLUCOSIO E VALORI DELLE ANALISI FATTE
# ############################################################################################
# params = df2["Parameter"].unique()
# n = len(params)
#
# cols = 4
# rows = (n + cols - 1) // cols
#
# fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4))
# axes = axes.flatten()
#
# for i, param in enumerate(params):
#     sub = df2[df2["Parameter"] == param]
#     data_to_plot = [
#         sub[sub["Has_Diagnosis"] == False]["Parameter_Value"],
#         sub[sub["Has_Diagnosis"] == True]["Parameter_Value"]
#     ]
#     axes[i].boxplot(
#         data_to_plot,
#         tick_labels=["Senza", "Con"],
#         patch_artist=True,
#         boxprops=dict(facecolor='lightblue'),
#         medianprops=dict(color='red')
#     )
#     axes[i].set_title(param, fontsize=9)
#     axes[i].set_ylabel("Valore parametro", fontsize=8)
#
# # Nasconde eventuali assi vuoti
# for ax in axes[n:]:
#     ax.set_visible(False)
#
# fig.suptitle(
#     "Boxplot per ciascun parametro biochimico (Con vs Senza complicanze)",
#     fontsize=14, y=1.02
# )
#
# # Regola lo spacing verticale
# fig.subplots_adjust(hspace=0.6)
#
# # Assicura lo stesso comportamento del secondo blocco
# plt.tight_layout()
#
# plt.show()
#
#
#
#
#
# #BOX PLOT SESSO
# ########################################
# # 1) Leggi il file con le informazioni di sesso
# patient_info = pd.read_csv("Excel/Patient_info.csv")  # contiene Patient_ID e Sex (M/F)
#
# # 2) Fai il merge con df2
# df2 = df2.merge(patient_info[['Patient_ID', 'Sex']], on='Patient_ID', how='left')
#
# # 3) Mappa M/F in etichette italiane
# df2['Sex_label'] = df2['Sex'].map({'M': 'Maschio', 'F': 'Femmina'})
#
# # 4) Prepara parametri e dimensioni della griglia
# params = df2["Parameter"].unique()
# n = len(params)
# cols = 4
# rows = (n + cols - 1) // cols
#
# # 5) Definisci l'ordine dei gruppi e le etichette
# group_combinations = [
#     ("Maschio", False),
#     ("Maschio", True),
#     ("Femmina", False),
#     ("Femmina", True),
# ]
# tick_labels = ["M-Senza", "M-Con", "F-Senza", "F-Con"]
#
# # 6) Crea la figura e gli assi
# fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 4))
# axes = axes.flatten()
#
# # 7) Per ciascun parametro, disegna il boxplot con 4 gruppi
# for i, param in enumerate(params):
#     sub = df2[df2["Parameter"] == param]
#     data_to_plot = [
#         sub[(sub["Sex_label"] == sex) & (sub["Has_Diagnosis"] == diag)]["Parameter_Value"]
#         for sex, diag in group_combinations
#     ]
#     axes[i].boxplot(
#         data_to_plot,
#         tick_labels=tick_labels,
#         patch_artist=True,
#         boxprops=dict(facecolor='lightblue'),
#         medianprops=dict(color='red')
#     )
#     axes[i].set_title(param, fontsize=9)
#     axes[i].set_ylabel("Valore parametro", fontsize=8)
#     # Ruota le etichette se servono
#     axes[i].tick_params(axis='x', rotation=45, labelsize=7)
#
# # 8) Nascondi eventuali assi vuoti
# for ax in axes[n:]:
#     ax.set_visible(False)
#
# # 9) Titolo e spacing verticale
# fig.suptitle(
#     "Boxplot per ciascun parametro biochimico\nMaschi vs Femmine, Senza vs Con complicanze",
#     fontsize=14, y=1.02
# )
# fig.subplots_adjust(hspace=0.8, top=0.92)
#
# # 10) Mostra
# plt.tight_layout()
# plt.show()
#
# #BOX PLOT ETA
# ########################################
# # --- 1) Calcola l'età al 2025 basandoti sul Birth_year ---
# current_year = 2025
# patient_info['Age'] = current_year - patient_info['Birth_year']
#
# # --- 2) Definisci le fasce d'età ---
# bins = [0, 30, 50, 70, 120]
# labels = ['<30', '30–49', '50–69', '≥70']
# patient_info['Age_group'] = pd.cut(
#     patient_info['Age'],
#     bins=bins,
#     labels=labels,
#     right=False
# )
#
# # --- 3) Associa le fasce d'età a df2 (merge se non già fatto) ---
# df2 = df2.merge(
#     patient_info[['Patient_ID', 'Age_group']],
#     on='Patient_ID',
#     how='left'
# )
#
# # --- 4) Prepara parametri e dimensioni della griglia ---
# params = df2["Parameter"].unique()
# n = len(params)
# cols = 4
# rows = (n + cols - 1) // cols
#
# # --- 5) Prepara le combinazioni Age × Diagnosi e le relative etichette ---
# group_combinations = [
#     (age, diag)
#     for age in labels
#     for diag in [False, True]
# ]
# tick_labels = [
#     f"{age}-{'Con' if diag else 'Senza'}"
#     for age, diag in group_combinations
# ]
#
# # --- 6) Crea la figura e gli assi ---
# fig, axes = plt.subplots(rows, cols, figsize=(cols * 6, rows * 5))
# axes = axes.flatten()
#
# # --- 7) Disegna i boxplot per ciascun parametro e ciascuna combinazione ---
# for i, param in enumerate(params):
#     sub = df2[df2["Parameter"] == param]
#     data_to_plot = [
#         sub[
#             (sub["Age_group"] == age) &
#             (sub["Has_Diagnosis"] == diag)
#         ]["Parameter_Value"]
#         for age, diag in group_combinations
#     ]
#     axes[i].boxplot(
#         data_to_plot,
#         tick_labels=tick_labels,
#         patch_artist=True,
#         boxprops=dict(facecolor='lightblue'),
#         medianprops=dict(color='red')
#     )
#     axes[i].set_title(param, fontsize=10)
#     axes[i].set_ylabel("Valore parametro", fontsize=9)
#     axes[i].tick_params(axis='x', rotation=45, labelsize=7)
#
# # --- 8) Nascondi eventuali assi vuoti ---
# for ax in axes[n:]:
#     ax.set_visible(False)
#
# # --- 9) Titolo e layout ---
# fig.suptitle(
#     "Boxplot per ciascun parametro biochimico\n"
#     "suddivisi per fasce d'età e complicanze",
#     fontsize=16, y=1.02
# )
# fig.subplots_adjust(hspace=0.8, top=0.92)
# plt.tight_layout()
#
# # --- 10) Mostra la figura ---
# plt.show()

############################################################################################