# ⚒️ Kelompok Kanara - Advanced Subsurface Mapping Tool

**Mata Kuliah:** Pemetaan Bawah Permukaan (IF-B 2025/2026)

Aplikasi ini adalah perangkat lunak berbasis web untuk **visualisasi struktur bawah permukaan** dan **perhitungan cadangan hidrokarbon (volumetrik)** secara interaktif. Dibangun menggunakan Python dan Streamlit, alat ini memungkinkan pengguna untuk memetakan reservoir minyak & gas dari data koordinat sumur dan melakukan estimasi *Gas Initially In Place* (GIIP) serta *Stock Tank Oil Initially In Place* (STOIIP).

---

## 👥 Anggota Kelompok

| Nama | NIM |
| :--- | :--- |
| **Muhammad Ruhul Jadid** | 123230046 |
| **Khatama Putra** | 123230053 |
| **Naurah Rifdah Nur R.** | 123230068 |
| **Gradiva Arya W.** | 123230089 |
| **Brian Zahran Putra** | 123230195 |

---

## 🚀 Fitur Utama

### 1. 📂 Manajemen Data Fleksibel
* **Input Manual:** Masukkan koordinat (X, Y, Z) satu per satu.
* **Batch Upload:** Dukungan upload file CSV dan Excel untuk data banyak sumur sekaligus.
* **Session Management:** Simpan (*backup*) pekerjaan Anda ke file JSON dan muat kembali (*restore*) kapan saja.

### 2. 📊 Analisis Volumetrik Real-Time
* Perhitungan otomatis **Gross Rock Volume** untuk Gas Cap, Oil Zone, dan Total Reservoir.
* Estimasi **STOIIP** (Minyak) dan **GIIP** (Gas) berdasarkan parameter petrofisika yang dapat disesuaikan (Porositas, Saturasi Air, Net-to-Gross, Faktor Volume Formasi).

### 3. 🗺️ Visualisasi Canggih
* **Peta Kontur 2D:** Peta struktur dengan *colormap* 'Jet' untuk identifikasi tinggian dan rendahan.
* **Model 3D Interaktif:** Model permukaan reservoir 3D yang dapat diputar, lengkap dengan bidang kontak fluida (GOC & WOC).
* **Cross-Section (Penampang):** Irisan melintang interaktif untuk melihat profil lapisan reservoir dari samping.

### 4. 📄 Pelaporan & Ekspor
* **PDF Report:** Laporan resmi siap cetak berisi ringkasan parameter dan hasil perhitungan.
* **Excel Report:** Laporan detail termasuk data mentah untuk analisis lebih lanjut.
* **Grid Data (CSV):** Ekspor hasil interpolasi grid untuk digunakan di software lain.
