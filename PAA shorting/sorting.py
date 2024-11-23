import random
import time

# Buat 100 angka acak
X = [random.randint(1, 1000) for _ in range(100)]

# Pseudocode untuk Merge Sort
# fungsi mergeSort(arr):
#     jika panjang arr ≤ 1:
#         kembalikan arr
#     tengah = panjang arr // 2
#     kiri = mergeSort(arr[0:tengah])
#     kanan = mergeSort(arr[tengah:])
#     kembalikan gabungkan(kiri, kanan)
#
# fungsi gabungkan(kiri, kanan):
#     hasil = daftar kosong
#     selama kiri dan kanan tidak kosong:
#         jika elemen pertama kiri ≤ elemen pertama kanan:
#             tambahkan elemen pertama kiri ke hasil
#             hapus elemen pertama dari kiri
#         jika tidak:
#             tambahkan elemen pertama kanan ke hasil
#             hapus elemen pertama dari kanan
#     tambahkan sisa elemen kiri (jika ada) ke hasil
#     tambahkan sisa elemen kanan (jika ada) ke hasil
#     kembalikan hasil

# Pseudocode untuk Bubble Sort
# fungsi bubbleSort(arr):
#     n = panjang arr
#     untuk i dari 0 sampai n-1:
#         untuk j dari 0 sampai n-i-2:
#             jika arr[j] > arr[j+1]:
#                 tukar arr[j] dan arr[j+1]
#     kembalikan arr


# Implementasi Merge Sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    tengah = len(arr) // 2
    kiri = mergeSort(arr[:tengah])
    kanan = mergeSort(arr[tengah:])
    return gabungkan(kiri, kanan)

def gabungkan(kiri, kanan):
    hasil = []
    while kiri and kanan:
        if kiri[0] <= kanan[0]:
            hasil.append(kiri.pop(0))
        else:
            hasil.append(kanan.pop(0))
    hasil.extend(kiri or kanan)
    return hasil


# Implementasi Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Tukar elemen jika tidak urut
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Mengukur waktu komputasi untuk Merge Sort
start_time_merge_sort = time.perf_counter()
data_terurut_merge = mergeSort(X.copy())
end_time_merge_sort = time.perf_counter()
time_complexity_merge = end_time_merge_sort - start_time_merge_sort

# Mengukur waktu komputasi untuk Bubble Sort
start_time_bubble_sort = time.perf_counter()
data_terurut_bubble = bubbleSort(X.copy())
end_time_bubble_sort = time.perf_counter()
time_complexity_bubble = end_time_bubble_sort - start_time_bubble_sort

# Cetak hasil
print("Data Awal:", X)
print("\nData Terurut dengan Merge Sort:", data_terurut_merge)
print("\nData Terurut dengan Bubble Sort:", data_terurut_bubble)

# Cetak waktu komputasi di bagian paling bawah
print("\nWaktu Komputasi:")
print(f"- Merge Sort: {time_complexity_merge:.10f} detik")
print(f"- Bubble Sort: {time_complexity_bubble:.10f} detik")
