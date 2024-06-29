# Submission Submission Akhir : Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Institut Jaya Jaya, sebuah institusi pendidikan yang didirikan pada tahun 2000, telah memiliki reputasi yang baik dalam menghasilkan lulusan berkualitas. Namun, institut ini menghadapi tantangan besar dengan tingginya jumlah siswa yang tidak menyelesaikan pendidikan mereka, atau yang dikenal dengan istilah "dropout". Tingginya tingkat dropout ini menjadi masalah serius bagi setiap institusi pendidikan karena dapat mempengaruhi reputasi dan masa depan para siswa.


Untuk mengatasi masalah ini, Institut Jaya Jaya bertujuan untuk mengidentifikasi siswa yang berisiko mengalami dropout sedini mungkin agar mereka dapat diberikan bimbingan dan dukungan khusus. Mereka telah menyediakan dataset kinerja siswa dan meminta pembuatan dashboard untuk membantu memahami dan memonitor kinerja siswa dengan mudah.

## Permasalahan Bisnis
1. Tingginya Tingkat Dropout: Masalah bisnis utama adalah tingginya tingkat dropout di kalangan siswa. Jumlah siswa yang tidak menyelesaikan pendidikan mereka ini mempengaruhi reputasi institut dan berdampak negatif pada masa depan para siswa yang dropout.

2. Kurangnya Sistem Deteksi Dini: Institut Jaya Jaya tidak memiliki cara yang efektif untuk mendeteksi siswa yang berisiko mengalami dropout. Tanpa sistem deteksi dini, sulit bagi institut untuk memberikan intervensi tepat waktu yang dapat mencegah siswa dari dropout.

3. Pemantauan Kinerja Siswa yang Tidak Efektif: Institut juga menghadapi kesulitan dalam memantau kinerja siswa secara menyeluruh. Tanpa alat pemantauan yang efisien, staf institut kesulitan mengidentifikasi tren atau pola yang mungkin mengindikasikan risiko dropout, sehingga tidak dapat mengambil tindakan preventif yang diperlukan.

## Cakupan Proyek

### Tujuan Proyek
1. Meningkatkan Pemantauan Kinerja Siswa: Membuat dashboard interaktif yang memudahkan staf institusi dalam memantau kinerja siswa secara real-time dan mengidentifikasi masalah potensial lebih awal.
2. Menyediakan Wawasan Berbasis Data: Menggunakan analisis data dan model prediktif untuk memberikan wawasan yang dapat membantu dalam pengambilan keputusan yang lebih baik terkait bimbingan dan dukungan siswa.

### Langkah-Langkah Proyek

1. Download Data
2. Eksplorasi dan Pembersihan Data
3. Analisis Data
4. Membuat model machine learning
5. Pengembangan Dashboard Bisnis
6. Pengembangan prototype aplikasi

## Persiapan

Sumber data : https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

### Setup Environment - Anaconda:

1. conda create --name main-ds python=3.9
2. conda activate main-ds
3. pip install -r requirements.txt

### Setup Environment - Shell/Terminal:
1. mkdir proyek_analisis_data
2. cd proyek_analisis_data
3. pipenv install
4. pipenv shell
5. pip install -r requirements.txt

### Setup Environment - Metabase:
1. docker pull metabase/metabase:v0.46.4
2. docker run -p 3000:3000 --name metabase metabase/metabase
3. http://localhost:3000/setup

### Setup Environtment - Streamlit:
1. streamlit run streamlit.py

## Business Dashboard

dashboard : https://public.tableau.com/views/Dashboard_17183339366460/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link

1. Dari beasiswa : Siswa yang tidak memiliki beasiswa cenderung lebih banyak yang dropout dibandingkan dengan siswa yang memiliki beasiswa
2. Dari update tuition : Tuition up to date berhubungan positif dengan tingkat kelulusan siswa. Siswa dengan biaya yang tidak terkini cenderung lebih banyak yang dropout.
3. Dari displaced : Siswa yang displaced dan yang tidak displaced memiliki pola yang serupa dalam hal kelulusan, tetapi siswa yang tidak displaced sedikit lebih banyak yang masih terdaftar daripada yang dropout.
4. Dari admission grade : Mahasiswa yang lulus cenderung memiliki nilai penerimaan yang lebih tinggi dan lebih merata dibandingkan dengan mahasiswa yang dropout atau masih terdaftar.
5. Dari marital status : Mahasiswa yang masih single cenderung lebih banyak yang lulus dibandingkan dengan yang dropout atau masih terdaftar.
6. dari debtor : Mahasiswa yang memiliki utang lebih berisiko untuk dropout dibandingkan dengan yang tidak memiliki utang.

## Streamlit

Streamlit : https://fauzan.streamlit.app/

## Conclusion

Institut Jaya Jaya menghadapi tantangan signifikan terkait tingginya tingkat dropout di kalangan siswa. Untuk mengatasi masalah ini, diperlukan pemahaman yang mendalam mengenai faktor-faktor yang berkontribusi terhadap risiko dropout dan pengembangan alat yang dapat membantu pemantauan dan intervensi dini.

Analisis data menunjukkan bahwa beberapa faktor berpengaruh terhadap kelulusan dan dropout mahasiswa:

1. Status Beasiswa: Mahasiswa yang tidak memiliki beasiswa lebih rentan untuk dropout dibandingkan dengan mereka yang memiliki beasiswa. Ini menunjukkan bahwa beasiswa memberikan dukungan finansial yang penting dan memotivasi siswa untuk menyelesaikan pendidikan mereka.

2. Pembayaran Biaya Kuliah: Mahasiswa dengan pembayaran biaya kuliah yang up-to-date lebih cenderung lulus. Sebaliknya, mereka yang tertinggal dalam pembayaran lebih rentan untuk dropout. Manajemen finansial yang baik tampaknya berkorelasi dengan keberhasilan akademik.

3. Status Perpindahan: Baik siswa yang displaced maupun yang tidak displaced memiliki pola kelulusan yang mirip, tetapi siswa yang tidak displaced sedikit lebih banyak yang masih terdaftar daripada yang dropout. Ini menunjukkan bahwa status perpindahan tidak sepenuhnya menentukan hasil akademik, meskipun dapat mempengaruhi retensi siswa.

4. Nilai Penerimaan: Mahasiswa dengan nilai penerimaan yang lebih tinggi cenderung lulus dibandingkan dengan yang memiliki nilai lebih rendah. Ini menandakan bahwa seleksi masuk yang ketat dapat berkontribusi pada tingkat kelulusan yang lebih tinggi.

5. Status Pernikahan: Mahasiswa yang masih single lebih banyak yang lulus dibandingkan dengan yang dropout atau masih terdaftar. Ini mungkin berkaitan dengan tanggung jawab dan tekanan tambahan yang dihadapi oleh mahasiswa yang sudah menikah.

6. Status Utang: Mahasiswa yang memiliki utang lebih berisiko untuk dropout dibandingkan dengan yang tidak memiliki utang. Utang bisa menjadi beban tambahan yang menghambat kemajuan akademik.

Secara keseluruhan, faktor finansial (seperti status beasiswa, pembayaran biaya kuliah, dan utang), nilai penerimaan, serta status personal (seperti status pernikahan dan perpindahan) memiliki pengaruh signifikan terhadap kelulusan dan dropout mahasiswa. Untuk mengurangi tingkat dropout dan meningkatkan kelulusan, Institut Jaya Jaya harus fokus pada dukungan finansial yang memadai, seleksi masuk yang efektif, serta bimbingan dan dukungan bagi siswa yang berisiko. Pembuatan dashboard interaktif akan membantu memantau kinerja siswa secara real-time dan memungkinkan intervensi tepat waktu bagi siswa yang membutuhkan.


## Rekomendasi

Berdasarkan analisis data terhadap faktor-faktor yang mempengaruhi tingkat kelulusan dan dropout mahasiswa, berikut adalah rekomendasi yang dapat diimplementasikan oleh Institut Jaya Jaya untuk mengurangi tingkat dropout dan meningkatkan kelulusan:

1. Peningkatan Program Beasiswa:

Rekomendasi: Tingkatkan jumlah dan cakupan program beasiswa untuk memberikan dukungan finansial kepada lebih banyak mahasiswa.

Alasan: Siswa yang menerima beasiswa cenderung memiliki tingkat kelulusan yang lebih tinggi dibandingkan dengan yang tidak menerima beasiswa.

2. Monitoring dan Pendampingan Pembayaran Biaya Kuliah:

Rekomendasi: Implementasikan sistem monitoring pembayaran biaya kuliah dan tawarkan rencana pembayaran fleksibel bagi siswa yang mengalami kesulitan finansial.

Alasan: Mahasiswa dengan pembayaran biaya kuliah yang up-to-date memiliki tingkat kelulusan yang lebih tinggi.

3. Dukungan bagi Mahasiswa Displaced:

Rekomendasi: Berikan dukungan khusus, seperti konseling dan bantuan relokasi, untuk siswa yang displaced.

Alasan: Meskipun status perpindahan tidak sepenuhnya menentukan hasil akademik, siswa yang displaced dapat menghadapi tantangan tambahan yang mempengaruhi retensi mereka.

4. Penguatan Seleksi Penerimaan:

Rekomendasi: Perketat proses seleksi penerimaan untuk memastikan bahwa mahasiswa yang diterima memiliki kemampuan akademik yang memadai.

Alasan: Mahasiswa dengan nilai penerimaan yang lebih tinggi cenderung lulus dibandingkan dengan yang memiliki nilai lebih rendah.

5. Dukungan bagi Mahasiswa dengan Status Pernikahan:

Rekomendasi: Sediakan program dukungan untuk mahasiswa yang sudah menikah, seperti fleksibilitas jadwal dan konseling keluarga.

Alasan: Mahasiswa yang masih single cenderung lebih banyak yang lulus dibandingkan dengan yang sudah menikah, yang mungkin menghadapi tanggung jawab dan tekanan tambahan.

6. Manajemen Utang Mahasiswa:

Rekomendasi: Sediakan program manajemen utang dan konseling finansial untuk membantu mahasiswa mengelola utang mereka.

Alasan: Mahasiswa yang memiliki utang lebih berisiko untuk dropout dibandingkan dengan yang tidak memiliki utang.






