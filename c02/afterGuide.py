# In [4]: %timeit afterGuide.xorBytes(b1, b2)
# 1.5 µs ± 25.6 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
def xorBytes(a, b):
    if len(a) != len(b):
        raise ValueError('Lenghts should be equal')
    ret = bytearray(len(a))
    for i, v1 in enumerate(a):
        ret[i] = v1 ^ b[i]
    return ret

# In [5]: %timeit afterGuide.xorBytes2(b1, b2)
# 3.31 µs ± 16.5 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
def xorBytes2(a, b):
    if len(a) != len(b):
        raise ValueError('Lenghts should be equal')
    ret = bytearray(len(a))
    for i, v1 in enumerate(a):
        ret[i] = v1 ^ b[i]
    return bytearray(v1 ^ v2 for v1, v2 in zip(a,b))

if __name__ == "__main__":
    b1 = bytearray.fromhex('1c0111001f010100061a024b53535009181c')
    b2 = bytearray.fromhex('686974207468652062756c6c277320657965')
    print(f'{b1=}')
    print(f'{b2=}')
    x1 = xorBytes(b1, b2)
    x2 = xorBytes2(b1, b2)
    print(f'{x1}')
    print(f'{x2}')
