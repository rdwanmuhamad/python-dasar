# python bahasa pemrograman interpreted
# source code -> interpreter (python) -> dijalankan terminal
# python dijalankan berdasarkan urutan nya
# baris kosong tidak akan dijalankan
# comment baris yang tidak akan dieksekusi
import time
start_time = time.time()
print("Hello World!")

print("Hello Dunia!")

# ini adalah comment
# comment multil line

"""ini adalah comment"""

# assignment (disimpan ke memori)
a = 10 #a sama dengan 10
print(a)

# kita bisa mengcompile python ke bytecode 
# cara mencompile, buka terminal dan jalankan
# python -m py_compile main.py

for i in range(1, 1000):
    a = 10
print(time.time() - start_time, "detik")


