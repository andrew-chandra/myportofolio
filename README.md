-e "Nama : Andrew Chandra Halim\nNPM : 2506656431\nKelas : PBP B" 

### Tugas 1

1. Pada Tutorial 1 saya fully bergantung pada template yang sudah disiapkan, namun pada saat mengerjakan Tugas 1, saya mencoba menyisipkan elemen article dan ul, li. Elemen-elemen tersebut membantu web saya supaya lebih enak dilihat, saya juga menggunakan article pada bagian "Experiences" agar lebih variatif (walaupun jadi kurang konsisten, tapi lumayan buat eksperimen).
2. Menurut saya, bagian yang lumayan rumit adalah penempatan layout keempat section tersebut, namun setelah mengenal flexbox, hal tersebut menjadi lebih mudah dikerjakan.
3. Karena web portofolionya masih static, kita harus edit HTML-nya secara manual jika suatu hari ada update, fungsionalitas dinamis yang ingin saya implementasikan adalah database, agar lebih fleksibel jika ada update di kemudian hari.

### AI DISCLOSURE
Pada saat mengerjakan Tutorial dan Tugas 1 ini, saya menggunakan LLM jenis Gemini Pro, saya menggunakan Gemini untuk bertanya mengenai branching yang baik, mengecek apakah kode kerangka HTML saya sudah mengikuti best practice, serta mencari ide layout CSS (dalam kasus ini Gemini merekomendasikan saya untuk menggunakan border).

1.
<!-- Prompt: <!-- <section class="experiences" id="bground">
            <div class="experiences container">
                <div class="Skills">

                </div>
                <div class="Experience">

                </div>
                <div class="Education">

                </div>
                <div class="Projects">

                </div>
            </div>
        </section><section class="experiences" id="bground">
            <div class="experiences container">
                <div class="Skills">

                </div>
                <div class="Experience">

                </div>
                <div class="Education">

                </div>
                <div class="Projects">

                </div>
            </div>
        </section> -->
gini oke ga -->

G:
Hapus Duplikasi ID: Atribut id (seperti id="bground") bersifat unik dan tidak boleh digunakan lebih dari satu kali dalam satu halaman HTML. Di kodemu, seluruh <section> tercetak dua kali secara identik. Hapus salah satu blok <section> tersebut.

Gunakan Huruf Kecil untuk Class: Walaupun tidak menyebabkan error, standar penamaan class di HTML dan CSS sebaiknya menggunakan huruf kecil semua (contoh: class="skills" bukan class="Skills"). Ini akan mencegah kebingungan saat kamu menulis kode CSS nanti.

Terapkan Elemen Semantik Lanjutan: Pertanyaan reflektif Tugas 1 menyinggung tentang penggunaan elemen semantik HTML5. Daripada membiarkan div kosong, gunakan heading (<h2>, <h3>) dan elemen seperti <ul>, <li>, atau <article> untuk membungkus konten di dalamnya.

Penuhi Syarat 3 Item Konten: Tugasmu mensyaratkan minimal satu section baru harus memiliki 3 item. Kamu bisa mendata bahasa pemrograman seperti Java, Python, dan assembly di bagian keterampilan, atau memasukkan rancangan CRC cards sistem ride-hailing BurhanAntar ke dalam bagian proyek.

2.
Prompt: ul li article itu apa bedanya sama div

G:
<!--<div> (Division): Ini adalah kontainer generik yang sama sekali tidak memiliki makna. Ibarat kardus polos kosong. Kamu menggunakan <div> murni untuk membungkus sekumpulan elemen demi kemudahan mengatur tata letak (layout) menggunakan CSS, misalnya saat ingin menerapkan Flexbox atau Grid.

<ul> (Unordered List) dan <li> (List Item): Keduanya adalah pasangan tidak terpisahkan untuk membuat daftar berpoin (bullet points). <ul> berfungsi sebagai bingkai keseluruhan daftar, sedangkan <li> adalah tiap-tiap baris itemnya. Tag ini sangat tepat digunakan untuk mendata poin-poin terstruktur, seperti mendaftar bahasa pemrograman (Java, Python) di bagian Skills.

<article>: Elemen ini mendefinisikan sebuah blok konten utuh dan mandiri yang maknanya tetap jelas meskipun dicabut dari halaman tersebut. Ibarat sebuah kartu berita, postingan blog, atau ulasan produk. Dalam konteks portofoliomu, tag ini sangat cocok untuk membungkus rincian satu karya spesifik (misalnya, satu <article> khusus untuk mendeskripsikan proyek BurhanAntar).

Jika kamu hanya menggunakan <div> di mana-mana (sering disebut div soup), kodenya tetap bisa dibuat cantik dengan CSS, tetapi browser akan melihatnya sebagai tumpukan kotak tanpa arti.

Menggunakan elemen semantik seperti <article>, <ul>, dan <li> tidak hanya membuat kodemu lebih rapi dan profesional, tetapi juga langsung membantumu menjawab pertanyaan reflektif Tugas 1 mengenai pentingnya elemen semantik HTML5. -->


### TUGAS 2
1. Diawali dengan URL yang diketik di browser, kemudian server akan meneruskan request tersebut. File urls.py proyek akan mencocokan url yang diketik dan melempar kita ke page aplikasi yang sesuai, sedangkan urls.py aplikasi menerima url lalu melempar kita ke bagian view. File views.py berisi rangkuman data dalam bentuk model, data tsb berbentuk context yang bisa digunakan oleh template, models.py berurusan dengan data yang digunakan dalam portofolio, data tersebut akan dioper ke view, dan template menerima data dari view, lalu dirender ke browser.

2. Jika data tidak disimpan pada models, maka tiap ada perubahan kita harus melakukan perubahan pada file HTML secara manual dan harus deploy ulang. Sedangkan dengan menggunakan model, perubahan data bisa dimodifikasi dengan lebih instan melalui django admin. Models juga memungkinkan kita untuk menampilkan banyak data menggunakan loop sehingga apabila datanya banyak, kita tidak harus ketik satu satu.

3. makemigrations dilakukan untuk melihat perubahan pada file models.py, saya menyadari bahwa command tersebut bisa mendeteksi perubahan pada object class maupun atributnya, namun command ini tidak bersangkutan langsung dengan database. Sedangkan migrate biasanya dilakukan setelah makemigrations sebagai bentuk eksekusi supaya data yang kita buat bisa dikaitkan ke database. contohnya pada kasus yang saya kerjakan pada tugas 2 ini, saya menambahkan field kesanpesan pada class Education yang saya define, agar perubahannya bisa terwujud saya harus mengetik 2 command tsb (makemigrations dan migrate)

### AI DISCLOSURE
Saya menggunakan Gemini Pro sebagai troubleshooter saya ketika stuck, seperti gagal deploy dan minor fix ketika saya salah create instance (harusnya di education malah di experience), Gemini membantu saya untuk remove object yang saya buat melalui shell. Saya juga bertanya ke gemini cara untuk fix flexbox yang melebar setelah objek tsb di remove (ada perubahan pada file css dimana boxnya saya bagi rata agar tampilannya lebih rapi.)
Untuk kerangka dan logika website saya purely mengerjakan sendiri!! (karena mengikuti arahan dari tutorial sebelumnya juga).

link gemini: https://share.gemini.google/T2QZ6cqiCuvD