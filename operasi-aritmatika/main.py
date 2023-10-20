# operasi aritmatika
a = 10
b = 5

# operasi pertambahan
tambah = a + b
print(tambah)

# operasi pengurangan
kurang = a - b
print(kurang)

# operasi perkalian
kali = a * b
print(kali)

# operasi pembagian
bagi = a / b
print(bagi)

# operasi eksponen (pangkat)
pangkat = a ** b
print(pangkat)

# operasi modulus
mod = a % b
print(mod)

# operasi floar division => kebalikan modulus
floar_div = a // b
print(floar_div)

# prioritas operasi => operational precedence
'''
    1. dalam kurung ()
    2. exponen (pangkat) **
    3. perkalian, pembagian, modulus,  dan floar division * / % //
    4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - z % x // y 
print(x,'**', y, '*', z, '+', x, '/', y, '-', z, '%', x, '//', y, '=', hasil )

hasil = (x + y) * z
print(hasil)