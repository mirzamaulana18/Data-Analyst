## Prasyarat

Sebelum memulai, pastikan Anda telah menginstal beberapa perangkat lunak berikut:

1. **Python**: Versi 3.7 atau lebih baru.
2. **Visual Studio Code (VS Code)**: Editor kode untuk pengembangan.
3. **Paket Python yang diperlukan**: Streamlit, pandas, seaborn, dan matplotlib.

## Langkah-langkah Menjalankan Dashboard

### 1. Clone atau Unduh Proyek

- Simpan file Python utama dan dataset (`day.csv` dan `hour.csv`) di dalam satu folder proyek.

### 2. Instal Python dan Dependensi

Jika Python belum terinstal, unduh dan instal dari [situs resmi Python](https://www.python.org/).

Setelah Python terinstal, buka terminal di VS Code dan jalankan perintah berikut untuk menginstal dependensi yang diperlukan:

```bash
pip install streamlit pandas seaborn matplotlib
```

### 3. Buka Folder Proyek di VS Code

- Buka VS Code.
- Pilih **File > Open Folder** dan pilih folder tempat file proyek yangs udah diunduh disimpan.

### 4. Jalankan Aplikasi Streamlit

- Pastikan terminal terbuka di VS Code ( Bisa dibuka melalui menu **View > Terminal**).
- Jalankan perintah berikut untuk memulai aplikasi Streamlit:

```bash
streamlit run bike_dashboard.py // ini nama file python untuk streamlitnya
```

Ganti `<nama_file_python>` dengan nama file Python yang berisi kode Streamlit Anda, misalnya:

### 5. Akses Dashboard di Browser

Setelah menjalankan perintah di atas, Streamlit akan memberikan URL lokal, seperti:

```
http://localhost:8501
```

- Klik tautan tersebut, atau salin dan buka di browser Anda untuk melihat dashboard.

### 6. Interaksi dengan Dashboard

Dashboard akan menampilkan:

- Scatter plot pengaruh suhu terhadap jumlah penyewa.
- Bar chart rata-rata jumlah penyewa berdasarkan kondisi cuaca.
- Line plot pola penyewaan sepeda berdasarkan waktu pada hari kerja dan akhir pekan.

### Perhatian

- Pastikan dataset `day.csv` dan `hour.csv` ada di direktori proyek.
- jika ingin menjalankan dicollab tinggal dibuka filenya (pastikan datasetnya diupload ke collab)
