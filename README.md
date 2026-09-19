Nama : Ahyan Timuardi

NPM : 2506547203

Kelas : PBP D

### Tugas 1

1. Ya, saya menggunakan elemen HTML seperti <section>, dan <article> dalam struktur HTML saya. Selain membantu membuat kode HTML yang saya tulis menjadi lebih readable dan mempermudah Styling CSS, secara spesifik elemen <section> digunakan untuk mengelompokkan fitur yang ada di website saya, seperti pemisahan antara fitur profil dan daftar Achievements yang saya buat. Sementara itu,Elemen <article> digunakan untuk membungkus item-item/entitas konten yang mandiri di dalam suatu <section>. Penerapan struktur <section> dan <> ini juga penting untuk mendukung aksesibilitas screen reader dan mempermudah mesin pencari (SEO) dalam memahami hierarki halaman website.
2. Untuk masalah tata letak, saya punya 3 item yang ditampilkan di desktop secara menyamping menggunakan grid-template-columns: repeat(3, 1fr), ketika viewport dipersempit seperti layar ponsel, 3 item tsb akan ikut menyempit dan gepeng membuat tampilan web menjadi jelek dan sulit dibaca. Solusinya adalah saya menggunakan media query @media (max-width: 600px) untuk membuat 3 item tsb tersusun secara vertikal ke bawah ketika viewport dipersempit menggunakan grid-template-columns: 1fr agar tampilan web tetap bagus dan readable dalam mode mobile.
3. Ya, karena web yang saya buat merupakan static web,semua perubahan content yang ingin saya lakukan di website tsb harus diubah lgsg melalui HTML. Yang artinya, kalau suatu saat saya mau menambah sertifikat lomba baru, mengganti foto profil, atau memperbarui bio, saya harus membuka dan mengubah kodenya secara manual satu per satu. Untuk proyek selanjutnya, Saya ingin web ini punya seperti ruang penyimpan untuk menyimpan content-content yg ada di dalamnya. Sehingga ketika saya ingin menghapus atau menambahkan suatu content ke dalam web saya tidak perlu mengubahnya secara lgsg di HTML.

### AI Disclosure
Menggunakan Gemini untuk memahami konsep dasar dan sintaks HTML semantik serta tata letak CSS, Membantu menemukan elemen HTML semantik dan sintaks CSS yang sesuai dengan tampilan/fitur yang ingin saya buat, Membantu memecahkan masalah khusunya pada tata letak yang menurut saya yang baru belajar agak susah untuk dipelajari.

### Tugas 2
1. 
- Permintaan masuk: Ketika Pengguna mengakses URL misalnya (`/education/`) request tsb pertama kali diterima oleh proyek di 'portofolio/urls.py'
- Routing Proyek: melalui fungsi `include('main.urls')`, request diteruskan ke konfigurasi rute aplikasi pada `main/urls.py`
- Routing Aplikasi: `main/urls.py` mencocokkan path `/education/` dan memanggil view terkait, yaitu fungsi `show_education`
- Logika View dan Pemanggilan model: `show_education` mengambil data riwayat pendidikan dari basis data menggunakan ORM Django (`Education.objects.all()`)
- Penyusunan Context dan Rendering Template: View mengemas data model tersebut ke dalam dictionary `context`, lalu meneruskannya bersama template `education.html` ke fungsi `render()`
- Respons ke browser: Django Template Engine memproses template dan context menjadi berkas HTML dinamis yang utuh, lalu mengembalikannya sebagai `HttpResponse` dengan kode status 200 ke pengguna

2. Menyimpan data di model menerapkan prinsip pemisahan tanggung jawab antara data dan tampilan antarmuka. Keuntungannya anatar lain:
- Kemudahan Pemeliharaan: Jika ingin menambah, mengedit, atau menghapus riwayat pendidikan, kita tidak perlu membongkar struktur kode HTML. Cukup memperbarui data melalui ORM atau panel admin basis data.
- Skalabilitas & Konsistensi: Tampilan HTML menjadi dinamis dan konsisten karena cukup ditulis satu kali menggunakan perulangan DTL (`{% for %}`). Berapa pun banyaknya data yang tersimpan, struktur antarmukanya akan otomatis menyesuaikan tanpa menduplikasi tag HTML secara manual.

3. Perbedaan `makemigrations` dan `migrate` adalah:
- `makemigrations` berfungsi untuk mendeteksi perubahan pada model kode Python dan menyusun berkas instruksi cetak biru migrasi baru di folder `migrations/`. Perintah ini belum mengubah struktur tabel di dalam basis data nyata
- Sementara itu `migrate` berfungsi untuk mengeksekusi berkas migrasi yang sudah dibuat tersebut secara nyata ke dalam basis data lokal sehingga skema tabel diperbarui sesuai definisi model

### AI Disclosure
Menggunakan gemini ketika mengalami kendala selama pengerjaan seperti menanyakan syntax dan memahami suatu baris kode secara lebih dalam. Mostly saya mengikuti tutorial 2.

### Tugas 3
1. Menggunakan ModelForm memberikan beberapa kelebihan daripada membuat form HTML secara manual diantaranya:
- Mencegah Redundansi Kode: ketika kita menggunakan form HTML manual kita harus mengetik tag <input>, menentukan atribut type, name, batasan panjang (maxlength), hingga placeholder satu per satu di file template. Jika nanti ada field baru di database, kita harus mengedit model dan template HTML secara terpisah. Sementara itu ketika kita menggunakan ModelForm kita cukup mendefinisikan daftar field di forms.py (fields = [...]), Django akan otomatis membangkitkan semua elemen input yang sesuai dengan skema model basis data.
- Validasi yang lebih aman: Ketika kita menggunakan form HTMl manual, validasi HTML biasa (seperti atribut required) sangat mudah diakali oleh user lewat Inspect Element. Karena itu, kita terpaksa menulis logika pengecekan manual yang panjang di views.py (misal mengecek apakah teks kosong, apakah format angka valid, dll.). Sementara itu ketika kita menggunakan ModelForm kita cukup memanggil method form.is_valid() dan Django akan langsung memvalidasi datanya.
- Kemudahan menyimpan dan mempebarui data: Pada ModelForm jika kita ingin menambahkan data cukup jalankan form.save() atau jika ingin memperbarui data cukup tambahkan parameter instance=objek, lalu jalankan form.save() lagi. Semenetra itu jika kita ingin menamabah atau memperbarui data menggunakan Form HTML manual kita harus mengambil data satu per satu (request.POST.get('title'), dsb.) lalu memanggil perintah Model.objects.create(...) atau mencari objek lama untuk di-assign secara manual.

2. JSON lebih disukai karena beberapa alasan, seperti:
- Kemudahan Penggunaan: JSON lebih mudah dibaca manusia dan diolah mesin karena strukturnya sederhana. XML, meskipun lebih terstruktur, sering dianggap terlalu panjang dan rumit untuk aplikasi sederhana.
- Efisiensi ukuran dan kecepatan: Karena JSON tidak menggunakan tag penutup, ukuran file JSON lebih kecil dibanding XML.
Hasil studi Mozilla Developer Network (2024) menunjukkan bahwa parsing JSON rata-rata 35% lebih cepat daripada XML dalam proses komunikasi API.
- Dukungan terhadap berbagai Tipe Data: JSON secara alami mendukung berbagai tipe data seperti angka, string, boolean, array, dan objek. Sementara XML memperlakukan semua isi elemen sebagai teks, sehingga pengembang perlu melakukan konversi manual ke tipe data lain.

3. Alur yang terjadi ketika menggunakan fungsi view untuk mengembalikan data dalam bentuk JSON diawali ketika aplikasi klien mengakses endpoint API yang sudah didaftarkan. DI server, fungsi view menerima permintaan tsb dan menarik baris-baris rekaman yang dibutuhkan dari basis data melalui perantara Django ORM. Setelah data diambil, kumpulan objek model tersebut diproses oleh fungsi serialisasi milik Django (serializers.serialize('json', ...)) untuk diterjemahkan menjadi teks berformat JSON. Teks JSON ini kemudian dibungkus ke dalam objek HTTPResponse lengkap dengan content-type=application/json, lalu dikirimkan kembali lewat jaringan internet ke peramban atau klien yang memintanya. Proses serialisasi diperlukan karena data yang masih berwujud objek bahasa Python murni tidak bisa dipahami, dibaca, ataupun dikirim secara langsung melalui protokol komunikasi web ke pihak luar. Melalui serialisasi, objek Python yang kompleks diubah menjadi format teks standar dan universal seperti JSON, sehingga data tersebut dapat diterima, diparsing, serta diolah dengan mudah.

### AI Disclosure
Menggunakan gemini untuk membantu saya dalam membuat file html baru yang diperlukan seperti education_delete_modal.html, education_form.html, dan education_edit_form.html untuk menyesuaikannya dengan style.css yang sudah ada. Selebihnya saya mengikuti tutorial 3.