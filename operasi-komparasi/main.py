# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean
# >, <, =>, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari (>)
lebihdari = a > b
print('hasil:', lebihdari)

# kurang dari (<)
kurangdari = b < a
print ('hasil', kurangdari)

# lebih dari samadengan (>=)
lebihdarisamadengan = a >= b
print('hasil:', lebihdarisamadengan)

# lebih dari samadengan (>=)
kurangdarisamadengan = a >= b
print('hasil:', kurangdarisamadengan)

# samadengan (==)
samadengan = a == b
print('hasil:', samadengan)

# tidaksamadengan (!=)
tidaksamadengan = a != b
print('hasil:', tidaksamadengan)

# 'is' sebagai komparasi object indentity / membandingkan objek
x = 5 #ini adalah assignment membuat object
y = 5

print('nilai x =', x,', id =', hex(id(x)))
print('nilai y =', y,', id =', hex(id(y)))

hasil = x is y
print('hasil:',hasil)

# 'is not' 
x = 5 
y = 6

print('nilai x =', x,', id =', hex(id(x)))
print('nilai y =', y,', id =', hex(id(y)))

hasil = x is not y
print('hasil:',hasil)
