# latihan logika dan  komparasi

# membuat gabungan area rentang dari angka

# ++++++3---------10++++++

inputUser = float(input('Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10 : '))

# ++++++3-------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 : ', isKurangDari)

# -------10+++++
# memeriksa angka lebih dari 10
isLebihdDari = (inputUser > 10)
print('Lebih dari 10 : ', isLebihdDari)

# ++++++3---------10+++++
isCorrect = isKurangDari or isLebihdDari
print('angka yang anda masukkan : ', isCorrect)

# ------3+++++++10------
# kasus irisan

inputUser = float(input('Masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 : '))

# ------3+++++++++++
isLebihdDari = (inputUser > 3)
print('Lebih dari 3 : ', isLebihdDari)

# ++++++++10--------
isKurangDari = (inputUser < 10)
print('Kurang dari 10 : ', isKurangDari)

isCorrect = isKurangDari and isLebihdDari
print('angka yang anda masukkan : ', isCorrect)