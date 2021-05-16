"""
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = KEY VALUE PAIR
dictionary = kamus
"""

kamus = {}
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['mother'] = 'ibu'

print(kamus)
print(kamus['ayah'])
print(kamus['ibu'])
print(kamus['mother'])

# eksekusi searah (dari kiri ke kanan), tidak bisa sebaliknya (dari kanan ke kiri)

data_dari_server_gojek = {
    'tanggal' : '2021-04-06',
    'driver_list' : [
        {'nama': 'Eko', 'jarak': 10, 'status': 'ojek'},
        {'nama': 'Dwi', 'jarak': 30, 'status': 'gofood'},
        {'nama': 'Tri', 'jarak': 100, 'status': 'gosend'},
        {'nama': 'Catur', 'jarak': 1000, 'status': 'available'}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}, {data_dari_server_gojek['tanggal']}")
print(f"Driver #2 {data_dari_server_gojek['driver_list'][1]}")
print(f"Driver #3 {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")

print(f"\nJarak driver terdekat {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
print(f"\nJarak driver terjauh {data_dari_server_gojek['driver_list'][3]['jarak']} meter, "
      f"status : {data_dari_server_gojek['driver_list'][3]['status']}, "
      f"nama : {data_dari_server_gojek['driver_list'][3]['nama']}")

