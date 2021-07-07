import time, base64, hmac, hashlib, requests, json
liste=["AVAX","BTC","ETH"]
i = 0
while i < 3:
    base = "https://graph-api.btcturk.com"
    method = "/v1/ohlcs?pair="
    uri = base+method +liste[i]+"_TRY"
    tmp= requests.get(url=uri)
    liste[i] = tmp.json()
    i += 1
    
#Tüm hacim bilgilerini çekelim.   
    
avax_volume=[]
for item in liste[0]:
    avax_volume.append(item["volume"])
avax_volume    

btc_volume=[]
for item in liste[1]:
    btc_volume.append(item["volume"])
btc_volume 

eth_volume=[]
for item in liste[2]:
    eth_volume.append(item["volume"])
eth_volume 

#Tüm fiyat bilgilerini çekelim.   

avax_price=[]
for item in liste[0]:
    avax_price.append(item["average"])
    
btc_price=[]
for item in liste[1]:
    btc_price.append(item["average"])
    
eth_price=[]
for item in liste[2]:
    eth_price.append(item["average"]) 
    
#Tüm gün bilgilerini çekelim.   
 
avax_time=[]
for item in liste[0]:
    avax_time.append(item["time"])
    
btc_time=[]
for item in liste[1]:
    btc_time.append(item["time"])
    
eth_time=[]
for item in liste[2]:
    eth_time.append(item["time"])  
    
#Unixtime dan date e dönelim.

import pandas as pd
avax_time=pd.to_datetime(avax_time, unit='s')
btc_time=pd.to_datetime(btc_time, unit='s')
eth_time=pd.to_datetime(eth_time, unit='s')

#Listler DataFrame olsun.  
avax_df = pd.DataFrame(zip(avax_volume, avax_price, avax_time), columns = ['Hacim', 'Fiyat', 'Gun'])
btc_df = pd.DataFrame(zip(btc_volume, btc_price, btc_time), columns = ['Hacim', 'Fiyat', 'Gun'])
eth_df = pd.DataFrame(zip(eth_volume, eth_price, eth_time), columns = ['Hacim', 'Fiyat', 'Gun'])

#Seaborn ve matplotlib kurma zamanı.

    pip install seaborn

    pip install matplotlib

#Seaborn ve matplotlib kütüphanelerini çağıralım.

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#AVAX Grafiğimizi çizdirelim.

fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
#bar plot creation
ax1.set_title('BTCTURK AVAX Hacim ve Fiyat (05/2021–07/2021)', fontsize=16)
ax1.set_xlabel('Gun', fontsize=16)
ax1.set_ylabel('Hacim', fontsize=16,color=color)
ax1 = sns.lineplot(x='Gun', y='Hacim', data = avax_df, sort=False, color=color)
ax1.tick_params(axis='y', color=color)
#specify we want to share the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
#line plot creation
ax2.set_ylabel('Fiyat Bilgisi', fontsize=16,color=color)
ax2 = sns.lineplot(x='Gun', y='Fiyat', data = avax_df, sort=False, color=color)
ax2.tick_params(axis='y')
#show plot
#plt.figure(figsize=(15,8))
plt.show()

#BTC Grafiğimizi çizdirelim

fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
#bar plot creation
ax1.set_title('BTCTURK BTC Hacim ve Fiyat (2014-2021)', fontsize=16)
ax1.set_xlabel('Gun', fontsize=16)
ax1.set_ylabel('Hacim', fontsize=16,color=color)
ax1 = sns.lineplot(x='Gun', y='Hacim', data = btc_df, sort=False, color=color)
ax1.tick_params(axis='y', color=color)
#specify we want to share the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
#line plot creation
ax2.set_ylabel('Fiyat Bilgisi', fontsize=16,color=color)
ax2 = sns.lineplot(x='Gun', y='Fiyat', data = btc_df, sort=False, color=color)
ax2.tick_params(axis='y')
#show plot
#plt.figure(figsize=(15,8))
plt.show()

#ETH Grafiğimizi çizdirelim

fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
#bar plot creation
ax1.set_title('BTCTURK ETH Hacim ve Fiyat (2018-2021)', fontsize=16)
ax1.set_xlabel('Gun', fontsize=16)
ax1.set_ylabel('Hacim', fontsize=16,color=color)
ax1 = sns.lineplot(x='Gun', y='Hacim', data = eth_df, sort=False, color=color)
ax1.tick_params(axis='y', color=color)
#specify we want to share the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
#line plot creation
ax2.set_ylabel('Fiyat Bilgisi', fontsize=16,color=color)
ax2 = sns.lineplot(x='Gun', y='Fiyat', data = eth_df, sort=False, color=color)
ax2.tick_params(axis='y')
#show plot
#plt.figure(figsize=(15,8))
plt.show()
