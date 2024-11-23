# Algoritma 

Siti Nurvatika
F55123009
##### (Pseudocode Marge Sort:)
```
Pseudocode untuk Merge Sort
 fungsi mergeSort(arr):
     jika panjang arr ≤ 1:
         kembalikan arr
     tengah = panjang arr // 2
     kiri = mergeSort(arr[0:tengah])
     kanan = mergeSort(arr[tengah:])
     kembalikan gabungkan(kiri, kanan)

 fungsi gabungkan(kiri, kanan):
     hasil = daftar kosong
     selama kiri dan kanan tidak kosong:
         jika elemen pertama kiri ≤ elemen pertama kanan:
             tambahkan elemen pertama kiri ke hasil
             hapus elemen pertama dari kiri
         jika tidak:
             tambahkan elemen pertama kanan ke hasil
             hapus elemen pertama dari kanan

tambahkan sisa elemen kiri (jika ada) ke hasil
    tambahkan sisa elemen kanan (jika ada) ke hasil
kembalikan hasil
```
#### (Analisis Big O dan Big Theta untuk Merge Sort:)
1. Divide Step (Pembagian):
    a). Pada setiap langkah rekursif, daftar dibagi menjadi dua bagian yang hampir sama besar.
    b). Setiap pembagian mengurangi masalah menjadi submasalah yang lebih kecil.
    c). Proses pembagian ini berlangsung selama log(n) kali karena kita membagi daftar menjadi dua pada setiap langkah rekursif (untuk n elemen, kita membutuhkan log₂n langkah untuk membagi hingga daftar menjadi         bagian-bagian berukuran satu).
2. Conquer Step (Penyatuan):
    a). Setelah daftar dibagi, setiap subdaftar yang lebih kecil disatukan kembali dengan cara mengurutkan elemen-elemen di dalamnya.
    b). Proses penyatuan ini memerlukan O(n) waktu untuk setiap langkah rekursif. Ini terjadi karena kita harus memeriksa dan menggabungkan setiap elemen dari dua bagian (kiri dan kanan) ke dalam hasil yang              terurut.
#### Big O Analysis (Worst-case Time Complexity):
1. Setiap pembagian membutuhkan log(n) langkah (karena pembagian menjadi dua subdaftar).
2. Setiap penggabungan (setelah pembagian) memerlukan O(n) waktu.
    Oleh karena itu, total kompleksitas waktu adalah O(n log n).
#### Big Theta Analysis (Average-case and Best-case Time Complexity):
Karena Merge Sort selalu membagi daftar menjadi dua dan menggabungkan hasilnya, meskipun data sudah terurut atau terbalik, kompleksitas waktu tetap konsisten pada O(n log n).
Big Theta (Θ) menunjukkan kompleksitas waktu dalam semua kondisi (baik terbaik, terburuk, maupun rata-rata) untuk algoritma yang konsisten dalam waktu komputasi.
Karena Merge Sort selalu memerlukan log(n) pembagian dan O(n) waktu untuk setiap penggabungan, kompleksitasnya adalah Θ(n log n).

##### (Pseudocode Bubble Sort:)
```
fungsi bubbleSort(arr):
     n = panjang arr
     untuk i dari 0 sampai n-1:
         untuk j dari 0 sampai n-i-2:
             jika arr[j] > arr[j+1]:
                 tukar arr[j] dan arr[j+1]
     kembalikan arr
  ```
     
#### (Analisis Big O dan Big Theta untuk Bubble Sort:)
1). Big O Analysis (Worst-case Time Complexity):
    a). Pada Bubble Sort, setiap elemen akan dibandingkan dengan elemen lainnya dan dipindahkan jika diperlukan.
    b). Outer Loop berjalan sebanyak n kali.
    c). Inner Loop berjalan sebanyak n-i-1 kali. Untuk iterasi pertama, inner loop akan berjalan n-1 kali, pada iterasi kedua akan berjalan n-2 kali, dan seterusnya.
    d). Worst-case Time Complexity adalah O(n²), karena dalam kasus terburuk, kita perlu membandingkan setiap elemen dengan setiap elemen lainnya (misalnya, jika daftar berurutan dalam urutan terbalik).

2). Big Theta Analysis (Average-case and Best-case Time Complexity):
#### Best-case Time Complexity:
    a). Best-case terjadi ketika daftar sudah terurut, dan kita hanya perlu satu kali melalui array untuk memverifikasi bahwa tidak ada yang perlu dipertukarkan.
    b). Dalam hal ini, jika kita menambahkan pengoptimalan untuk memeriksa apakah ada pertukaran yang dilakukan dalam satu iterasi (sehingga menghentikan proses lebih awal jika tidak ada perubahan), maka         kompleksitas waktu best-case bisa menjadi O(n).
    c). Tanpa pengoptimalan, meskipun data sudah terurut, Bubble Sort tetap akan menjalankan seluruh loop, sehingga tetap O(n²).
#### Average-case Time Complexity:
    Pada rata-rata kasus, setiap elemen akan dibandingkan dengan elemen lainnya beberapa kali. Oleh karena itu, Average-case juga memiliki kompleksitas waktu O(n²).
