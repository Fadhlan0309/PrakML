# -*- coding: utf-8 -*-
"""Proyek Analisis Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Yw3bGTrM2sYC9qKJPm0biv_X2tqS9lTd

#Proyek Analisis Data: Bike Sharing Dataset
- **Nama:** Muhammad Fadhlandhifan Siregar
- **Email:** fadhlandhifansiregar@gmail.com
- **ID Dicoding:** fadhlan03

# Pertanyaan Analisis
1. Bagaimana pengaruh cuaca terhadap jumlah pengguna sepeda setiap hari?
2. Apakah terdapat perbedaan pola penggunaan sepeda berdasarkan waktu dalam sehari (jam)?

# Import Library
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
!pip install streamlit
import streamlit as st

"""# Import Dataset"""

day_df = pd.read_csv('/content/day.csv')
hour_df = pd.read_csv('/content/hour.csv')

"""# Exploratory Data Analysis (EDA)"""

print(day_df.isnull().sum())
print(hour_df.isnull().sum())

"""# Pertanyaan 1: Pengaruh cuaca terhadap jumlah pengguna sepeda
Visualisasi: Scatter plot untuk menunjukkan hubungan antara cuaca dan jumlah pengguna harian.|
"""

plt.figure(figsize=(10, 6))
sns.boxplot(data=day_df, x='weathersit', y='cnt', palette='coolwarm')
plt.title('Effect of Weather on Daily Bike Usage', fontsize=14)
plt.xlabel('Weather Situation (1: Clear, 2: Misty, 3: Light Snow/Rain)', fontsize=12)
plt.ylabel('Number of Bike Users (Daily)', fontsize=12)
plt.show()

"""Visualisasi di atas menunjukkan distribusi jumlah pengguna sepeda harian berdasarkan kondisi cuaca. Dari plot tersebut, terlihat bahwa:

* Cuaca yang lebih cerah (kategori 1: clear weather) cenderung memiliki jumlah pengguna yang lebih tinggi.

* Jumlah pengguna menurun saat kondisi cuaca memburuk (kategori 2: misty, kategori 3: light snow/rain).

# Pertanyaan 2: Pola penggunaan sepeda berdasarkan waktu dalam sehari
Visualisasi: Line chart yang memperlihatkan pola jumlah pengguna dalam sehari (berdasarkan jam).
"""

plt.figure(figsize=(10, 6))
sns.lineplot(data=hour_df, x='hr', y='cnt', ci=None, marker='o', color='b')
plt.title('Bike Usage Pattern Based on Hour of the Day', fontsize=14)
plt.xlabel('Hour of the Day (0-23)', fontsize=12)
plt.ylabel('Number of Bike Users (Hourly)', fontsize=12)
plt.show()

"""Visualisasi tersebut menunjukkan pola penggunaan sepeda berdasarkan jam dalam sehari. Terlihat bahwa:

* Jumlah pengguna sepeda cenderung meningkat pada jam sibuk pagi (sekitar jam 7-9) dan sore (sekitar jam 17-19), yang kemungkinan besar terkait dengan jam berangkat dan pulang kerja.

* Di luar jam-jam tersebut, terutama pada malam hari, jumlah pengguna sepeda jauh lebih rendah.

#Distribusi Pengguna Sepeda
"""

plt.figure(figsize=(10, 6))
sns.histplot(day_df['casual'], color='blue', kde=True, label='Casual Users', bins=30)
sns.histplot(day_df['registered'], color='green', kde=True, label='Registered Users', bins=30)
plt.title('Distribution of Casual vs Registered Bike Users', fontsize=14)
plt.xlabel('Number of Users', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.show()

"""Visualisasi distribusi pengguna sepeda, baik untuk pengguna kasual maupun terdaftar, memberikan beberapa insight penting:

* Pengguna Terdaftar (Registered): Secara umum, pengguna terdaftar memiliki distribusi yang lebih tinggi dibandingkan dengan pengguna kasual. Ini menunjukkan bahwa layanan berbagi sepeda lebih banyak digunakan oleh mereka yang mendaftar secara reguler (misalnya, pekerja harian atau pelanggan jangka panjang).

* Pengguna Kasual (Casual): Pengguna kasual lebih sedikit dan distribusinya lebih tersebar. Hal ini bisa mengindikasikan bahwa pengguna kasual mungkin lebih banyak memanfaatkan sepeda pada waktu-waktu tertentu (seperti akhir pekan atau liburan).

# Insight
Layanan berbagi sepeda lebih banyak menarik pengguna terdaftar secara konsisten, tetapi tetap memiliki pengguna kasual yang dapat memanfaatkan sepeda dalam kondisi tertentu.

#Korelasi Antar Variabel
"""

day_numeric_df = day_df.drop(columns=['dteday'])
plt.figure(figsize=(12, 8))
corr_matrix = day_numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Variables (Day Data)', fontsize=14)
plt.show()

"""* Suhu (temp) dan Jumlah Pengguna (cnt): Ada korelasi positif antara suhu dan jumlah pengguna sepeda, yang berarti jumlah pengguna cenderung meningkat ketika suhu lebih hangat. Ini logis karena cuaca yang lebih baik biasanya mendorong lebih banyak orang untuk menggunakan sepeda.

* Kelembaban (hum) dan Jumlah Pengguna (cnt): Korelasi antara kelembaban dan jumlah pengguna negatif, yang menunjukkan bahwa kondisi kelembaban yang lebih tinggi dapat mengurangi penggunaan sepeda. Kelembaban yang tinggi mungkin membuat berkendara menjadi tidak nyaman.

* Kecepatan Angin (windspeed) dan Jumlah Pengguna (cnt): Ada sedikit korelasi negatif, yang menunjukkan bahwa kecepatan angin yang tinggi sedikit mengurangi jumlah pengguna sepeda.

# Insight
Faktor-faktor cuaca seperti suhu, kelembaban, dan kecepatan angin berpengaruh terhadap jumlah pengguna sepeda. Cuaca yang lebih baik (hangat, kelembaban rendah, angin rendah) cenderung meningkatkan penggunaan.

# Boxplot : Pengaruh hari kerja
"""

plt.figure(figsize=(10, 6))
sns.boxplot(data=day_df, x='workingday', y='cnt', palette='Set3')
plt.title('Pengaruh hari kerja', fontsize=14)
plt.xlabel('Hari kerja(0: Tidak kerja, 1: Kerja)', fontsize=12)
plt.ylabel('Pengguna Sepeda (Per Hari)', fontsize=12)
plt.show()

"""# Boxplot: Pengaruh hari libur terhadap jumlah pengguna sepeda"""

plt.figure(figsize=(10, 6))
sns.boxplot(data=day_df, x='holiday', y='cnt', palette='Set2')
plt.title('Pengaruh hari libur', fontsize=14)
plt.xlabel('Holiday (0: Non-holiday, 1: Holiday)', fontsize=12)
plt.ylabel('Pengguna Sepeda (Per Hari)', fontsize=12)
plt.show()

"""* Hari Kerja (workingday): Pada visualisasi boxplot, kita dapat melihat bahwa pada hari kerja jumlah pengguna sepeda cenderung lebih tinggi. Ini mungkin karena orang menggunakan sepeda untuk bepergian ke tempat kerja atau sekolah.

* Hari Libur (holiday): Jumlah pengguna sepeda cenderung lebih rendah pada hari libur, yang kemungkinan karena sebagian besar orang tidak melakukan perjalanan rutin pada hari libur dan lebih memilih transportasi lain.

# Insight
Penggunaan sepeda meningkat pada hari kerja dibandingkan dengan hari libur. Ini menunjukkan bahwa berbagi sepeda lebih banyak dimanfaatkan untuk kegiatan sehari-hari seperti pergi ke kantor atau sekolah, dan lebih sedikit digunakan untuk kegiatan rekreasi pada hari libur.

# Kesimpulan
* Pertanyaan 1: Cuaca yang cerah cenderung meningkatkan jumlah pengguna sepeda, sementara cuaca yang lebih buruk mengurangi penggunaan.

* Pertanyaan 2: Pola penggunaan sepeda menunjukkan puncak pada jam sibuk pagi dan sore, dengan penggunaan yang lebih rendah di luar jam-jam tersebut.
"""

