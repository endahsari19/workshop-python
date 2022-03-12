# BAB 7 : I/O
## Input dan Output Pythton 

`Input` (dalam konteks pemrograman) merupakan sebuah data, informasi, atau nilai apa pun yang dikirimkan oleh user kepada komputer untuk diproses lebih lanjut . User melakukan proses input melalui media atau perangkat masukan seperti kibor, mouse, kamera, mikrofon dan lain sebagainya .

`Output` (dalam bahasa Indonesia) merupakan setiap nilai atau data atau informasi yang dikirimkan oleh mesin / komputer kepada user (manusia) setelah tahap pemrosesan tertentu .

Pernyataan ekspresi dan print()fungsi. (Cara ketiga adalah menggunakan write()metode objek file; file keluaran standar dapat dirujuk sebagai sys.stdout.
Ketika Anda tidak membutuhkan output yang mewah tetapi hanya ingin tampilan cepat dari beberapa variabel untuk keperluan debugging, Anda dapat mengonversi nilai apa pun menjadi string dengan fungsi repr()or str().

`Fungsi str()` ini dimaksudkan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr()dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau akan memaksa a SyntaxErrorjika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str()akan mengembalikan nilai yang sama dengan repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi yang berbeda.

`Literal` string terformat (disingkat juga disebut f-string) memungkinkan Anda memasukkan nilai ekspresi Python di dalam string dengan mengawali string denganforFdan menulis ekspresi sebagai {expression}.

Secara umum output bisa berupa teks, gambar, suara, atau bahkan berupa informasi yang dicetak di atas kertas, dan sebagainya

- Jika ingin menggunakan literal string berformat , mulailah string dengan fatau Fsebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda dapat menulis ekspresi Python antara {dan } karakter yang dapat merujuk ke variabel atau nilai literal.
```python 
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
```
- Metode str.format()string membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan {dan }untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.
```python
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
```
- Terakhir, Anda dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan untuk membuat tata letak apa pun yang dapat Anda bayangkan. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu.

### Literal string
`Literal string terformat` (disingkat juga disebut f-string) memungkinkan Anda memasukkan nilai ekspresi Python di dalam string dengan mengawali string denganforFdan menulis ekspresi sebagai {expression}.

### Format string
`Tanda kurung dan karakter` di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke str.format()metode. Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam str.format()metode.

### Performatan string
`Metode str.rjust()` objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. Ada metode serupa str.ljust()dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda, tetapi itu biasanya lebih baik daripada alternatifnya, yang berbohong tentang nilai. (Jika Anda benar-benar menginginkan pemotongan, Anda selalu dapat menambahkan operasi irisan, seperti pada x.ljust(n)[:n].)

### Performatan string
`Operator % (modulo)` juga dapat digunakan untuk pemformatan string. Mengingat , contoh di diganti dengan nol atau lebih elemen dari . Operasi ini biasa disebut dengan interpolasi string. Sebagai contoh:'string' % values%stringvalues

### Reading and Writing files
`Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan`. mode bisa 'r'ketika file hanya akan dibaca, 'w' untuk hanya menulis (file yang ada dengan nama yang sama akan dihapus), dan 'a'membuka file untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke akhir. 'r+'membuka file untuk membaca dan menulis. Argumen mode adalah opsional; 'r'akan diasumsikan jika dihilangkan.

### Methods of Files object
`Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner)`. size adalah argumen numerik opsional. Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file dua kali lebih besar dari memori mesin Anda. Jika tidak, paling banyak karakter ukuran (dalam mode teks) atau ukuran byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read()akan mengembalikan string kosong ( '').

### Saving structured data with json
`String dapat dengan mudah ditulis dan dibaca dari sebuah file.` Angka membutuhkan sedikit lebih banyak usaha, karena read()metode ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil seperti string '123' dan mengembalikan nilai numeriknya 123. Saat Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar bersarang dan kamus, parsing dan serialisasi dengan tangan menjadi rumit.