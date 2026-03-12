import pandas as pd
#Importando archivo desde web
ips=pd.read_csv("https://raw.githubusercontent.com/CesarMCuellarCha/archivosCSV/refs/heads/main/ips.csv")
print(ips.info())
print(ips.head())
print(ips.columns)

