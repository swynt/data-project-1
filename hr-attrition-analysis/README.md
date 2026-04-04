# Proyek Pertama: Menyelesaikan Permasalahan Human Resources (HR)

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang memiliki lebih dari 1000 karyawan. Namun, perusahaan menghadapi tantangan dalam mengelola sumber daya manusia, khususnya terkait tingginya attrition rate (tingkat karyawan keluar) yang mencapai lebih dari 10%.

Tingginya attrition rate dapat berdampak pada meningkatnya biaya rekrutmen dan pelatihan karyawan baru, menurunnya produktivitas tim, serta terganggunya stabilitas operasional perusahaan. Jika kondisi ini terus berlanjut, perusahaan berisiko mengalami penurunan kinerja dalam jangka panjang.

Oleh karena itu, diperlukan analisis berbasis data untuk memahami faktor-faktor yang menyebabkan attrition serta membantu perusahaan dalam mengambil keputusan strategis untuk meningkatkan retensi karyawan.

---

### Permasalahan Bisnis

Perusahaan menghadapi beberapa permasalahan utama terkait attrition karyawan:

- Tingginya attrition rate yang berdampak pada biaya operasional dan produktivitas  
- Kurangnya pemahaman mengenai faktor-faktor utama yang menyebabkan karyawan resign  
- Tidak adanya tools monitoring yang memudahkan HR dalam menganalisis attrition secara berkala  
- Kesulitan dalam mengidentifikasi karyawan yang berisiko tinggi untuk keluar  

---

### Cakupan Proyek

Cakupan proyek ini meliputi:

1. **Data Understanding dan Data Cleaning**  
   Mengidentifikasi struktur data, menangani missing values, serta membersihkan data agar siap digunakan.

2. **Exploratory Data Analysis (EDA)**  
   Melakukan analisis univariate, bivariate, dan multivariate untuk memahami hubungan antara attrition dengan berbagai faktor seperti overtime, salary, tenure, dan job role.

3. **Pembuatan Business Dashboard**  
   Membuat dashboard interaktif menggunakan Looker Studio untuk memvisualisasikan faktor-faktor yang mempengaruhi attrition.

4. **Machine Learning Modeling**  
   Membangun model klasifikasi menggunakan Random Forest untuk memprediksi kemungkinan attrition karyawan.

---

### Persiapan

**Sumber data:**  
Dicoding Dataset
https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

---

### Setup Environment

#### Instalasi Package via Requirements.txt

pip install -r requirements.txt

---

#### Setup Environment - Anaconda

conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

---

#### Setup Environment - Shell/Terminal

pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt

---

### Cara Menjalankan Script Prediksi

Pastikan file `model.pkl` berada dalam direktori yang sama dengan `prediction.py`.
Untuk menjalankan prediksi, gunakan perintah berikut:
python prediction.py

Script ini akan menggunakan model yang telah dilatih untuk melakukan prediksi terhadap sample data yang telah ditentukan di dalam script.

---

## Business Dashboard

Dashboard dibuat menggunakan Looker Studio untuk membantu tim HR dalam memonitor attrition secara visual dan interaktif.

Dashboard dapat diakses melalui link berikut:  
https://lookerstudio.google.com/reporting/fca980ac-37be-4c1e-aeac-0f8ab284a8a1

Dashboard ini memungkinkan HR untuk melakukan monitoring secara real-time, mengidentifikasi pola attrition, serta mendukung pengambilan keputusan berbasis data dalam meningkatkan retensi karyawan.

### Penjelasan Visualisasi

* **Attrition Rate (KPI)**
  Menampilkan persentase total karyawan yang keluar dari perusahaan. KPI ini digunakan sebagai indikator utama untuk memantau tingkat attrition secara keseluruhan.

* **Attrition by Overtime**
  Visualisasi ini menunjukkan bahwa karyawan yang bekerja lembur memiliki tingkat attrition yang lebih tinggi dibandingkan yang tidak lembur. Hal ini mengindikasikan bahwa beban kerja berlebih menjadi salah satu faktor utama yang mempengaruhi keputusan karyawan untuk resign.

* **Attrition by Salary**
  Visualisasi ini memperlihatkan bahwa karyawan dengan tingkat gaji yang lebih rendah memiliki tingkat attrition yang lebih tinggi. Insight ini membantu perusahaan dalam mengevaluasi dan menyesuaikan strategi kompensasi.

* **Attrition by Tenure**
  Visualisasi ini menunjukkan bahwa karyawan dengan masa kerja pendek, khususnya pada 0–2 tahun pertama, memiliki risiko attrition paling tinggi. Hal ini menekankan pentingnya program onboarding dan adaptasi di awal masa kerja.

* **Attrition by Job Role**
  Visualisasi ini membantu mengidentifikasi job role dengan tingkat attrition tertinggi, seperti posisi di bidang sales. Informasi ini dapat digunakan untuk merancang strategi retensi yang lebih spesifik berdasarkan peran pekerjaan.

* **Filter Department**
  Fitur ini memungkinkan HR untuk melakukan analisis yang lebih mendalam berdasarkan departemen tertentu, sehingga strategi yang diambil dapat lebih tepat sasaran.

Melalui dashboard ini, tim HR dapat dengan cepat mengidentifikasi faktor utama penyebab attrition serta mengambil tindakan strategis untuk meningkatkan retensi karyawan.

---

## Conclusion

Berdasarkan hasil analisis data, terdapat beberapa faktor utama yang mempengaruhi tingginya attrition rate di perusahaan:

1. **Overtime**  
   Karyawan yang bekerja lembur memiliki tingkat attrition yang jauh lebih tinggi (~32%) dibandingkan karyawan yang tidak lembur (~11%).

2. **Kompensasi (Salary)**  
   Karyawan dengan pendapatan lebih rendah cenderung memiliki tingkat attrition yang lebih tinggi.

3. **Masa Kerja (Tenure)**  
   Karyawan dengan masa kerja pendek (<5 tahun), terutama 0–2 tahun pertama, memiliki risiko attrition paling tinggi.

4. **Job Role**  
   Terdapat perbedaan attrition antar job role, di mana beberapa posisi seperti Sales Representative memiliki tingkat attrition lebih tinggi.

Selain itu, model machine learning menggunakan Random Forest menunjukkan bahwa faktor seperti overtime, monthly income, dan years at company memiliki pengaruh besar dalam memprediksi attrition.

Secara keseluruhan, **beban kerja, kompensasi, dan masa kerja awal** menjadi faktor utama yang mempengaruhi keputusan karyawan untuk keluar.

Dengan demikian, seluruh permasalahan bisnis yang telah diidentifikasi pada awal proyek berhasil dijawab melalui analisis data, visualisasi dashboard, serta model prediksi yang telah dibangun.

---

### Rekomendasi Action Items

Berikut beberapa rekomendasi yang dapat dilakukan oleh perusahaan:

- Mengurangi overtime dengan mengatur distribusi beban kerja secara lebih optimal  
- Meninjau dan menyesuaikan struktur gaji, terutama pada posisi dengan attrition tinggi  
- Memperkuat program onboarding dan mentoring untuk karyawan baru  
- Melakukan monitoring khusus pada karyawan di 1–2 tahun pertama  
- Meningkatkan employee engagement melalui survei kepuasan dan pengembangan career path  