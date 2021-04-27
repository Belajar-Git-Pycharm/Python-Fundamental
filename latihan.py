mobil = []
mobil.append('mercedes_benz')
mobil.append('audi')
mobil.append('bmw')
mobil.append('range_rover')
mobil.append('ferrari')
mobil.append('toyota')
mobil.append('honda')
mobil.append('suzuki')
mobil.append('nissan')
mobil.append('mazda')


for a in mobil :
    print(f'saya jual {a}')

print('\n')

for a in range(0, len(mobil)) :
    print(f'{a+1}. saya jual mobil {mobil[a]}')

print('\n')
print('berikut daftar mobil eropa yang jadi favorit :')
mercedes_benz = {
    'e_class' : ['w124', 'w210', 'w211', 'w212'],
    'c_class' : ['w202', 'w203', 'w204', 'w205'],
    's_class' : ['w220', 'w221', 'w222', 'w223']
}
bmw = {
    'seri3' : ['e30', 'e36', 'e46'],
    'seri5' : ['e34', 'e39'],
    'seri7' : ['e38']
}

print(f"mercedes benz {mercedes_benz['e_class'][1]}, dan bmw {bmw['seri3'][2]}")
print(f"\nbmw {bmw['seri3'][0]}, {bmw['seri5'][1]}")

