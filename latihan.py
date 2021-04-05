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

