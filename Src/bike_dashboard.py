import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

# Preprocess data
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

day_df.rename(columns={
    'cnt': 'total_count',
    'temp': 'temperature',
    'hum': 'humidity',
    'windspeed': 'wind_speed',
    'weekday': 'is_weekday',
    'workingday': 'is_workingday',
    'weathersit': 'weather_condition'
}, inplace=True)

hour_df.rename(columns={
    'cnt': 'total_count',
    'temp': 'temperature',
    'hum': 'humidity',
    'windspeed': 'wind_speed',
    'weekday': 'is_weekday',
    'workingday': 'is_workingday',
    'weathersit': 'weather_condition'
}, inplace=True)

weather_mapping = {
    1: 'Clear, Few clouds, Partly cloudy',
    2: 'Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist',
    3: 'Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds',
    4: 'Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog'
}

day_df['weather_condition'] = day_df['weather_condition'].map(weather_mapping)

hour_df['is_weekend'] = hour_df['is_weekday'].apply(lambda x: 'Weekend' if x in [0, 6] else 'Weekday')
weekday_data = hour_df[hour_df['is_weekend'] == 'Weekday'].groupby('hr')['total_count'].mean()
weekend_data = hour_df[hour_df['is_weekend'] == 'Weekend'].groupby('hr')['total_count'].mean()

# UBAH NILAI SUHU KE NILAI AKTUAL (SEBELUM DIBAGI 41 SEPERTI DI DATASET)
day_df['temperature_actual'] = day_df['temperature'] * 41

# Streamlit app
st.title("Bike Rental Analysis")

# Scatter plot
st.subheader("Pengaruh Suhu terhadap Jumlah Penyewa")
fig1, ax1 = plt.subplots(figsize=(12, 6))
workingday_data = day_df[day_df['is_workingday'] == 1]
holiday_data = day_df[day_df['is_workingday'] == 0]
sns.scatterplot(x='temperature_actual', y='total_count', data=workingday_data, label='Hari Kerja', color='blue', ax=ax1)
sns.scatterplot(x='temperature_actual', y='total_count', data=holiday_data, label='Hari Libur', color='orange', ax=ax1)
ax1.set_title('Pengaruh Suhu terhadap Jumlah Penyewa', fontsize=14)
ax1.set_xlabel('Suhu (°C)', fontsize=12)
ax1.set_ylabel('Jumlah Penyewa', fontsize=12)
ax1.legend(title='Kategori', fontsize=10, title_fontsize=12)
ax1.grid(alpha=0.3)
st.pyplot(fig1)

# Bar chart
st.subheader("Jumlah Penyewa Berdasarkan Kondisi Cuaca")
fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.barplot(x='weather_condition', y='total_count', data=day_df, hue='is_workingday', ax=ax2)
ax2.set_title('Rata-rata Jumlah Penyewa Berdasarkan Kondisi Cuaca', fontsize=14)
ax2.set_xlabel('Kondisi Cuaca', fontsize=12)
ax2.set_ylabel('Jumlah Penyewa', fontsize=12)
ax2.legend(title='Hari (0: Libur, 1: Kerja)', title_fontsize=12, fontsize=10)
ax2.tick_params(axis='x', labelsize=6)
ax2.tick_params(axis='y', labelsize=6)
ax2.grid(alpha=0.3)
st.pyplot(fig2)

# Line plot with weekend/weekday filter
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam")
selected_category = st.radio("Pilih Kategori:", ('Weekday', 'Weekend'))

if selected_category == 'Weekday':
    plot_data = weekday_data
else:
    plot_data = weekend_data

fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.plot(plot_data.index, plot_data.values, label=selected_category, color='orange', marker='o')
ax3.set_title(f'Pola Penyewaan Sepeda Berdasarkan Jam pada {selected_category}', fontsize=14)
ax3.set_xlabel('Jam', fontsize=12)
ax3.set_ylabel('Rata-rata Jumlah Penyewa', fontsize=12)
ax3.legend(title='Kategori', fontsize=10, title_fontsize=12)
ax3.grid(alpha=0.5)
st.pyplot(fig3)
