import time, base64, hmac, hashlib, requests, json

#BTCTURK API Servisine Bağlanıyoruz.

base = "https://graph-api.btcturk.com"
method = "/v1/ohlcs?pair=AVAX_TRY"
uri = base+method

result = requests.get(url=uri)
result = result.json()
print(json.dumps(result, indent=2))

#Gün değişkenini liste olarak çekiyoruz.

time=[]
for item in result:
    time.append(item["time"])
time 

#Gün değişkeni unix time olarak kayıtlı. Bunu normal tarihe dönüştürüyoruz.Panda bilgisayarınızda yüklü değilse yükleyin.

import pandas as pd
time=pd.to_datetime(time, unit='s')
time

#Günlük hacim değişkenini liste olarak çekiyoruz.

volume=[]
for item in result:
    volume.append(item["volume"])
volume 

#Günlük fiyat değişkenini liste olarak çekiyoruz.

average=[]
for item in result:
    average.append(item["average"])
average 

#Listeleri toplayıp bir DataFrame yapıyoruz.

df = pd.DataFrame(zip(volume, average, time), columns = ['Hacim', 'Fiyat', 'Gun'])

# İki y eksenli bir grafik çiziyoruz.


#Create combo chart
#Kaynak: https://towardsdatascience.com/combo-charts-with-seaborn-and-python-2bc911a08950

fig, ax1 = plt.subplots(figsize=(10,6))
color = 'tab:green'
#bar plot creation
ax1.set_title('BTCTURK AVAX Hacim ve Fiyat (05/2021-07/2021)', fontsize=16)
ax1.set_xlabel('Gun', fontsize=16)
ax1.set_ylabel('Hacim', fontsize=16,color=color)
ax1 = sns.lineplot(x='Gun', y='Hacim', data = df,  sort=False, color=color)
ax1.tick_params(axis='y', color=color)
#specify we want to share the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
#line plot creation
ax2.set_ylabel('Fiyat Bilgisi', fontsize=16,color=color)
ax2 = sns.lineplot(x='Gun', y='Fiyat', data = df, sort=False, color=color)
ax2.tick_params(axis='y')
#show plot
plt.show()

