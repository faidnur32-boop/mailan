list_buah = ['Mangga', 'Jambu', 'Jeruk', 'Jambu' ]
print(list_buah)
# hapus item pertama dengan nilai 'Jambu'
list_buah.remove('Jambu')
print(list_buah)

del list_buah[1]
print(list_buah)
del list_buah[0:2]
print(list_buah)

list_buah = ['Mangga', 'Jeruk', 'Zaitun', 'Apel', 'Durian']
print(list_buah)
# urutkan secara acconding
list_buah.sort()
print(list_buah)
# membalikkan posisi item list (tidak harus berurutan)
list_buah.reverse()
print(list_buah)