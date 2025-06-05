#AGGLOMERATIVE CLUSTER NON USATO NEI DOCUMENTI

# import pandas as pd
# from sklearn.impute import SimpleImputer, KNNImputer
# from sklearn.experimental import enable_iterative_imputer  # noqa
# from sklearn.impute import IterativeImputer
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import AgglomerativeClustering
# from sklearn.metrics import (
#     confusion_matrix,
#     silhouette_score,
#     accuracy_score,
#     precision_score
# )
#
# # 1. Caricamento dataset
# df = pd.read_csv("Excel/Clustering.csv")
# X = df.drop(columns=["Has_Diagnostics"])
# y = df["Has_Diagnostics"]
#
# # 2. Imputatori
# imputers = {
#     # Sostituisce ogni valore mancante con la media aritmetica della colonna
#     "Mean":    SimpleImputer(strategy="mean"),
#     # Sostituisce ogni valore mancante con la mediana (valore centrale) della colonna
#     "Median":  SimpleImputer(strategy="median"),
#     # KNN: media dei k=5 vicini per riga
#     "KNN":     KNNImputer(n_neighbors=5),
#     # MICE: imputazione iterativa
#     "MICE":    IterativeImputer(max_iter=10, random_state=42)
# }
#
# # 3. Griglia di iperparametri per AgglomerativeClustering
# linkages = ['ward', 'complete', 'average', 'single']
# # per ogni linkage, definiamo i metrici ammessi
# valid_metrics = {
#     'ward':     ['euclidean'],                    # ward richiede euclidea
#     'complete': ['euclidean', 'manhattan', 'cosine'],
#     'average':  ['euclidean', 'manhattan', 'cosine'],
#     'single':   ['euclidean', 'manhattan', 'cosine']
# }
#
# # 4. Funzione di valutazione
# def evaluate_agglomerative(imputer_name, imputer, n_clusters, linkage, metric):
#     # a) Imputazione dei valori mancanti
#     X_imp = imputer.fit_transform(X)
#     # b) Standardizzazione
#     X_scaled = StandardScaler().fit_transform(X_imp)
#     # c) Clustering gerarchico agglomerativo
#     agg = AgglomerativeClustering(
#         n_clusters=n_clusters,
#         linkage=linkage,
#         metric=metric
#     )
#     clusters = agg.fit_predict(X_scaled)
#     # d) Calcolo delle metriche
#     sil   = silhouette_score(X_scaled, clusters)
#     cm    = confusion_matrix(y, clusters)
#     acc   = accuracy_score(y, clusters)
#     prec  = precision_score(y, clusters, zero_division=0)
#     return sil, cm, acc, prec
#
# # 5. Loop su imputatori, linkage e metric
# results = []
# for imp_name, imp in imputers.items():
#     for linkage in linkages:
#         for metric in valid_metrics[linkage]:
#             # fissiamo sempre n_clusters=2
#             sil, cm, acc, prec = evaluate_agglomerative(
#                 imp_name, imp,
#                 n_clusters=2,
#                 linkage=linkage,
#                 metric=metric
#             )
#             results.append({
#                 'Imputer': imp_name,
#                 'Linkage': linkage,
#                 'Metric':  metric,
#                 'Silhouette': sil,
#                 'Accuracy':   acc,
#                 'Precision':  prec,
#                 'ConfusionMatrix': cm
#             })
#             print(f"{imp_name} | linkage={linkage}, metric={metric} "
#                   f"-> silhouette={sil:.3f}, accuracy={acc:.3f}, precision={prec:.3f}")
#             print(cm)
#####################################################################################################
#MEANSHIFT NON USATO NEI DOCUMENTI

# import pandas as pd
# from sklearn.impute import SimpleImputer, KNNImputer
# from sklearn.experimental import enable_iterative_imputer  # noqa
# from sklearn.impute import IterativeImputer
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import MeanShift, estimate_bandwidth
# from sklearn.metrics import (
#     confusion_matrix,
#     silhouette_score,
#     accuracy_score,
#     precision_score
# )
#
# # 1. Caricamento dataset
# df = pd.read_csv("Excel/Clustering.csv")
# X = df.drop(columns=["Has_Diagnostics"])
# y = df["Has_Diagnostics"]
#
# # 2. Imputatori
# imputers = {
#     "Mean":    SimpleImputer(strategy="mean"),
#     "Median":  SimpleImputer(strategy="median"),
#     "KNN":     KNNImputer(n_neighbors=5),
#     "MICE":    IterativeImputer(max_iter=10, random_state=42)
# }
#
# # 3. Funzione di valutazione per Mean Shift
# def evaluate_meanshift(imputer_name, imputer):
#     # a) Imputazione dei valori mancanti
#     X_imp = imputer.fit_transform(X)
#     # b) Standardizzazione
#     X_scaled = StandardScaler().fit_transform(X_imp)
#     meanshift = MeanShift()
#     clusters = meanshift.fit_predict(X_scaled)
#     sil = silhouette_score(X_scaled, clusters)
#     cm = confusion_matrix(y, clusters)
#     acc = accuracy_score(y, clusters)
#     prec = precision_score(y, clusters, average='macro', zero_division=0)
#
#     # -- Analisi cluster vs Has_Diagnostics --
#     df_result = df.copy()
#     df_result['cluster'] = clusters
#     contingency_table = pd.crosstab(df_result['cluster'], df_result['Has_Diagnostics'],
#                                     rownames=['Cluster'], colnames=['Has_Diagnostics'])
#
#     print(f"\nImputer: {imputer_name}")
#     print("Tabella di contingenza tra cluster e complicanze (Has_Diagnostics):")
#     print(contingency_table)
#
#     # Calcolo percentuale di complicanze in ogni cluster
#     percent_complicanze = contingency_table[1] / contingency_table.sum(axis=1) * 100
#     print("\nPercentuale di pazienti con complicanze in ogni cluster:")
#     print(percent_complicanze)
#
#     # Numero pazienti per cluster
#     print("\nNumero di pazienti per cluster:")
#     print(contingency_table.sum(axis=1))
#
#     return sil, cm, acc, prec
#
# # 4. Loop su imputatori per Mean Shift
# results_meanshift = []
# for imp_name, imp in imputers.items():
#     sil, cm, acc, prec = evaluate_meanshift(imp_name, imp)
#     results_meanshift.append({
#         'Imputer': imp_name,
#         'Silhouette': sil,
#         'Accuracy': acc,
#         'Precision': prec,
#         'ConfusionMatrix': cm
#     })
#     print(f"{imp_name} | Mean Shift -> silhouette={sil:.3f}, accuracy={acc:.3f}, precision={prec:.3f}")
#     print(cm)

#####################################################################################################
#DBSCAN NON USATO NEI DOCUMENTI

# import pandas as pd
# import numpy as np
# from sklearn.impute import SimpleImputer, KNNImputer
# from sklearn.experimental import enable_iterative_imputer  # noqa
# from sklearn.impute import IterativeImputer
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import DBSCAN
# from sklearn.metrics import (
#     confusion_matrix,
#     silhouette_score,
#     accuracy_score,
#     precision_score
# )
#
# # 1. Caricamento dataset
# df = pd.read_csv("Excel/Clustering.csv")
# X = df.drop(columns=["Has_Diagnostics"])
# y = df["Has_Diagnostics"]
#
# # 2. Imputatori
# imputers = {
#     "Mean":    SimpleImputer(strategy="mean"),
#     "Median":  SimpleImputer(strategy="median"),
#     "KNN":     KNNImputer(n_neighbors=5),
#     "MICE":    IterativeImputer(max_iter=10, random_state=42)
# }
#
# # 3. Funzione di valutazione
# def evaluate_dbscan(imputer_name, imputer, eps=0.5, min_samples=5):
#     # a) Imputazione
#     X_imp = imputer.fit_transform(X)
#     # b) Standardizzazione
#     X_scaled = StandardScaler().fit_transform(X_imp)
#     # c) DBSCAN
#     dbscan = DBSCAN(eps=eps, min_samples=min_samples)
#     clusters = dbscan.fit_predict(X_scaled)
#
#     # d) Etichette complete (incluso rumore)
#     X_valid = X_scaled
#     y_valid = y
#     clusters_valid = clusters
#
#     # e) Info cluster
#     unique, counts = np.unique(clusters_valid, return_counts=True)
#     cluster_info = dict(zip(unique, counts))
#
#     # f) Valutazione
#     if len(set(clusters_valid)) < 2:
#         sil = np.nan
#         acc = np.nan
#         prec = np.nan
#         cm = np.array([[0, 0], [0, 0]])
#     else:
#         sil = silhouette_score(X_valid, clusters_valid)
#         acc = accuracy_score(y_valid, clusters_valid)
#         prec = precision_score(y_valid, clusters_valid, average="macro", zero_division=0)
#         cm = confusion_matrix(y_valid, clusters_valid)
#
#     return sil, cm, acc, prec, len(set(clusters_valid)), cluster_info
#
# # 4. Loop su eps e imputatori
# eps_values = [1.0, 2.0, 3.0, 5.0, 10.0]
# results = []
#
# for eps in eps_values:
#     print(f"\n========== eps = {eps} ==========")
#     for imp_name, imp in imputers.items():
#         sil, cm, acc, prec, n_clusters, cluster_info = evaluate_dbscan(imp_name, imp, eps=eps, min_samples=3)
#         results.append({
#             'Eps': eps,
#             'Imputer': imp_name,
#             'Silhouette': sil,
#             'Accuracy': acc,
#             'Precision': prec,
#             'ConfusionMatrix': cm,
#             'NumClusters': n_clusters,
#             'ClusterDistribution': cluster_info
#         })
#         print(f"{imp_name} | eps={eps} | n_clusters={n_clusters} -> silhouette={sil:.3f}, accuracy={acc}, precision={prec}")
#         print("Cluster distribution:", cluster_info)
#         print("Confusion Matrix:\n", cm)
#####################################################################################################

