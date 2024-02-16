# operator bitwise

# bitwise -> operasi masing-masing bit
# int -> 2 = 00000010 (2^1)
# int -> 1 = 00000001 (2^0)

a = 9 
b = 5

# operator bitwise OR (|)
c = a | b
print('========== OR ===========')
print('nilai : ', a, 'binary : ', format(a, '08b'))
print('nilai : ', b, 'binary : ', format(b, '08b'))
print('nilai : ', c, 'binary : ', format(c, '08b'))

# operator bitwise AND (&)
c = a & b
print('========== AND ===========')
print('nilai : ', a, 'binary : ', format(a, '08b'))
print('nilai : ', b, 'binary : ', format(b, '08b'))
print('nilai : ', c, 'binary : ', format(c, '08b'))

# operator bitwise XOR (^)
c = a ^ b
print('========== XOR ===========')
print('nilai : ', a, 'binary : ', format(a, '08b'))
print('nilai : ', b, 'binary : ', format(b, '08b'))
print('nilai : ', c, 'binary : ', format(c, '08b'))

# operator bitwise NOT (~)
c = ~a
print('========== NOT ===========')
print('nilai : ', a, 'binary : ', format(a, '08b'))
print('nilai : ', c, 'binary : ', format(c, '08b'))
d = 0b0000001001
e = 0b1111111111
print('nilai : ', e^d, 'binary : ', format(e^d, '08b'))

# shifting

# shift right (>>)
c = a >> 1
print('========== SHIFT RIGHT ===========')
print('nilai : ', a, 'binary : ', format(a, '08b'))
print('nilai : ', c, 'binary : ', format(c, '08b'))

# shift left (<<)
c = a << 1
print('========== SHIFT LEFT ===========')
print('nilai : ', a, 'binary : ', format(a, '08b'))
print('nilai : ', c, 'binary : ', format(c, '08b'))