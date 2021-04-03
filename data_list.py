# latihan coding part 4, tipe data list / array / daftar

# tipe data skalar / sederhana

print('penggunaan tipe data skalar / sederhana :')
anak1 = 'pasmina'
anak2 = 'sotsugyou'
anak3 = 'zenryouku'
anak4 = 'shounen'

print(anak1)
print(anak2)
print(anak3)
print(anak4)


# penggunaan spasi / jarak dalam RUN

print('\n') # jarak 2 spasi jika sendiri seperti ini


# tipe data list 1 (penggunaan 'append')

print('data list 1')
anak = []
anak.append('pasmina')
anak.append('sotsugyou')
anak.append('zenryouku')
anak.append('shounen')

print(anak)


# tipe data list 2 (dengan dan tanpa 'append')

print('\ndata list 2') # jarak 1 spasi jika di dalam statement
anak = ['pasmina', 'sotsugyou', 'zenryouku', 'shounen'] # tanpa 'append'
print(anak)
anak.append('wibisono') # dengan 'append' jadi menambah daftar anak yang terakhir ke data list terakhir
print(anak)


# sapa anak ke-2

print('\nmenyapa anak ke-2 :')
print(f'hai {anak[1]}!') # menghitung isi data list di mulai dari angka 0, jadi anak ke-2 adalah urutan 1 bukan 2


# sapa semua anak

print('\nmenyapa semua anak :')

for a in anak :
    print(f'hai {a}!')


# sapa semua anak cara ribet

print('\n')
print('cara sapa anak dengan cara ribet dan penambahan nomor urut di depan :')

# 'len' digunakan saat kita tidak tahu ada berapa jumlah anak karena sudah ditambah dengan 'append'
for a in range(0, len(anak)) :
    print(f'{a+1}. hai {anak[a]}!') # penambahan nomor urut

