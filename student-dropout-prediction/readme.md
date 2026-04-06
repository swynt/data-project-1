# 🎓 Proyek Data Science: Prediksi Dropout Mahasiswa

## Business Understanding

Jaya Jaya Institute merupakan institusi pendidikan tinggi yang telah menghasilkan banyak lulusan berkualitas. Namun, institusi ini menghadapi tantangan berupa tingginya jumlah mahasiswa yang tidak menyelesaikan studi (dropout).

Tingginya angka dropout dapat berdampak pada:

* Menurunnya reputasi institusi
* Inefisiensi biaya operasional
* Rendahnya tingkat kelulusan mahasiswa

Oleh karena itu, diperlukan pendekatan berbasis data untuk memahami penyebab utama dropout serta membantu institusi dalam mengambil keputusan yang tepat.

---

### Permasalahan Bisnis

Beberapa permasalahan utama yang dihadapi:

* Tingginya jumlah mahasiswa yang dropout
* Kurangnya pemahaman mengenai faktor penyebab dropout
* Tidak adanya tools monitoring performa mahasiswa secara menyeluruh
* Kesulitan dalam mengidentifikasi mahasiswa yang berisiko dropout sejak dini

---

### Cakupan Proyek

Proyek ini mencakup:

1. **Analisis Data Mahasiswa**
   Memahami karakteristik mahasiswa dari sisi akademik, demografi, dan finansial.

2. **Exploratory Data Analysis (EDA)**
   Mengidentifikasi pola dan hubungan antara performa mahasiswa dengan status dropout.

3. **Pembuatan Dashboard**
   Mengembangkan dashboard interaktif menggunakan Looker Studio untuk memonitor performa mahasiswa.

4. **Model Prediksi Dropout**
   Membangun model machine learning untuk memprediksi kemungkinan mahasiswa dropout.

---

### Persiapan

**Sumber Data:**
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

---

### Setup Environment

**Python Version:** 3.10

#### Instalasi Dependencies

```bash
pip install -r requirements.txt
```

---

### Cara Menjalankan Aplikasi

Untuk menjalankan aplikasi prediksi:

```bash
streamlit run app.py
```

Aplikasi akan menampilkan form input data mahasiswa dan memberikan hasil prediksi risiko dropout.

---

## Business Dashboard

Dashboard dibuat menggunakan Looker Studio untuk membantu pihak institusi dalam memahami performa mahasiswa secara visual.

🔗 Link Dashboard:
https://lookerstudio.google.com/reporting/20a1b3e8-0954-4b6e-933f-70524f6ed434

Dashboard ini menampilkan berbagai informasi penting seperti distribusi mahasiswa, tingkat dropout, serta faktor-faktor yang mempengaruhi performa mahasiswa.

---

### Penjelasan Visualisasi

* **Dropout Rate (KPI)**
  Menampilkan persentase mahasiswa yang dropout dari total mahasiswa. Digunakan sebagai indikator utama kondisi institusi.

* **Distribusi Status Mahasiswa**
  Menunjukkan perbandingan antara mahasiswa yang dropout, masih terdaftar (enrolled), dan lulus.

* **Performa Akademik (Nilai)**
  Menunjukkan bahwa mahasiswa dengan nilai rendah cenderung memiliki risiko dropout lebih tinggi.

* **Jumlah Mata Kuliah Disetujui**
  Mahasiswa dengan jumlah mata kuliah lulus yang sedikit memiliki kemungkinan dropout lebih tinggi.

* **Status Pembayaran Tuition**
  Mahasiswa yang memiliki kendala pembayaran lebih rentan mengalami dropout.

* **Distribusi Usia Mahasiswa**
  Membantu melihat pola dropout berdasarkan kelompok usia.

Melalui dashboard ini, pihak institusi dapat dengan mudah memahami kondisi mahasiswa dan mengambil tindakan yang tepat.

---

## Deployment (Aplikasi Prediksi)

Aplikasi prediksi dibuat menggunakan Streamlit dan dapat diakses secara online.

🔗 Link Aplikasi:
https://data-project-1-eyz5rxbw2z7o8kqvfdjrtz.streamlit.app/

Fitur utama:

* Input data mahasiswa
* Prediksi risiko dropout
* Informasi tingkat probabilitas dropout
* Insight sederhana untuk membantu pengambilan keputusan

---

## Model Performance

Model yang digunakan adalah Logistic Regression.

Hasil evaluasi menunjukkan:
- Accuracy: 86% (baik)
- Model mampu mengidentifikasi mahasiswa yang berisiko dropout dengan baik

Model ini cukup stabil dan dapat digunakan sebagai dasar sistem early warning.

Model dipilih karena memiliki keseimbangan antara performa dan interpretabilitas, sehingga mudah dipahami oleh pihak non-teknis.

---

## Conclusion

Berdasarkan hasil analisis, terdapat beberapa faktor utama yang mempengaruhi kemungkinan mahasiswa dropout:

1. **Performa Akademik**
   Mahasiswa dengan nilai rendah memiliki risiko dropout lebih tinggi.

2. **Jumlah Mata Kuliah yang Diselesaikan**
   Semakin sedikit mata kuliah yang lulus, semakin tinggi risiko dropout.

3. **Kondisi Finansial**
   Mahasiswa dengan kendala pembayaran tuition cenderung lebih rentan dropout.

4. **Kondisi Awal Mahasiswa**
   Admission grade dapat menjadi indikator awal performa akademik mahasiswa.

Secara keseluruhan, performa akademik dan kondisi finansial merupakan faktor utama yang mempengaruhi dropout.

Pendekatan berbasis data ini terbukti mampu membantu institusi dalam mengidentifikasi risiko sejak dini.

Hasil ini juga konsisten dengan analisis data sebelumnya (EDA), di mana faktor akademik dan finansial terbukti menjadi indikator utama dropout.

---

## Rekomendasi Action Items

Berikut beberapa langkah yang dapat dilakukan oleh institusi:

* Membangun sistem **early warning** untuk mendeteksi mahasiswa berisiko
* Memberikan perhatian khusus pada mahasiswa dengan nilai rendah
* Menyediakan dukungan finansial atau skema pembayaran fleksibel
* Mengadakan program mentoring dan bimbingan akademik
* Melakukan monitoring intensif pada semester awal

Dengan implementasi strategi ini, diharapkan angka dropout dapat ditekan dan tingkat kelulusan meningkat.

---

## Catatan

* Dashboard dapat diakses secara publik
* Model telah di-deploy dan dapat digunakan langsung
* Video demo bersifat opsional dan tidak disertakan dalam proyek ini

---

## Author

Cornelius
sw.cornel@gmail.com