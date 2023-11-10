# latihan konversi satuan temperature

# program konversi ke satuan lain 
print("\nProgram Konversi Temperature")
celcius = float(input('Masukkan dalam suhu celcius: '))

print("suhu adalah",celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print('suhu reamur:', reamur, 'Reamur')

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('suhu fahrenheit:', fahrenheit, 'Fahrenheit')

# fahrenheit ke kelvin
fk = ((fahrenheit - 32) * (5/9) + 273.15)
print('fahrenheit ke kelvin:', fk, 'Kelvin') 

# kelvin
kelvin = celcius + 273
print('suhu kelvin:', kelvin, 'Kelvin')

# kelvin ke fahrenheit
kf = ((kelvin - 273) * (9/5) + 32)
print('kelvin ke fahrenheit:', kf, 'Fahrenheit')

