# operasi logika atau boolean
# NOT, OR, AND, XOR

# 1. NOT
print ('=====NOT=====')
a = True
c = not a
print ('data a:', a)
print ('data c:', c)

a = False
c = not a
print ('data a:', a)
print ('data c:', c)

# 2. OR / jika salah satu true maka hasil akan true
print ('=====OR=====')
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)

# 3. AND / jika salah satu false maka hasil akan false
print ('=====AND=====')
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

a = True
b = False
c = a and b
print(a, 'and', b, '=', c)

a = False
b = True
c = a and b
print(a, 'and', b, '=', c)

a = False
b = False
c = a and b
print(a, 'and', b, '=', c)

# 4. XOR / akan true jika salah satu true, sisanya false
print ('=====XOR=====')
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
