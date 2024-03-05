import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

BikeSharing_df = pd.read_csv("hour.csv")

st.header('Bike Sharing Dashboard :bike:')

st.subheader("Grafik peminjaman sepeda setiap bulan")

df_sum = BikeSharing_df.groupby('mnth')['cnt'].agg(['max', 'min', 'mean', 'sum'])
# Buat warna untuk bar yang memiliki nilai paling banyak dan sedikit
colors = ['blue' if (x < max(df_sum['sum']) and x > min(df_sum['sum'])) else 'red' for x in df_sum['sum']]

# Buat plot
plt.figure(figsize=(10, 6))
plt.bar(df_sum.index, df_sum['sum'], color = colors)
plt.xlabel('Bulan')
plt.ylabel('Total peminjam sepeda')

# Gunakan Streamlit untuk menampilkan plot
st.pyplot(plt)

st.subheader("Perbandingan Rata-Rata Temp, Atemp, Hum, dan Windspeed")

df_largest = BikeSharing_df.nlargest(5, 'cnt')[['temp', 'atemp', 'hum', 'windspeed']].mean()
df_smallest = BikeSharing_df.nsmallest(5, 'cnt')[['temp', 'atemp', 'hum', 'windspeed']].mean()

# Gabungkan kedua DataFrame
df_combined = pd.concat([df_largest, df_smallest], axis=1)
df_combined.columns = ['5 Terbesar', '5 Terkecil']

# Buat diagram batang
plt.figure(figsize=(10, 6))
df_combined.plot(kind='bar')
plt.ylabel('Rata-Rata')
plt.xlabel('Variabel')

# Gunakan Streamlit untuk menampilkan plot
st.pyplot(plt)

