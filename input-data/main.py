# input user 

# data yang diinputkan pasti string
data = input('Masukkan data:')
print('data:', data, 'tipe data:', type(data))

# jika kita ingin mengubah data gunakan operator casting
data_int = int(input('Masukkan data:'))
print('data:', data_int, 'tipe data:', type(data_int))

data_float = float(input('Masukkan data:'))
print('data:', data_float, 'tipe data:', type(data_float))

data_boolean = bool(int(input('Masukkan data:')))
print('data:', data_boolean, 'tipe data:', type(data_boolean))