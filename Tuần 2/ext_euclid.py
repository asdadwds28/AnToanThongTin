def poly_degree(a):
    if a == 0: return -1
    return a.bit_length() - 1

def poly_divmod(a, b):
    if b == 0: raise ZeroDivisionError("Division by zero")
    q = 0
    r = a
    deg_b = poly_degree(b)
    while True:
        deg_r = poly_degree(r)
        if deg_r < deg_b:
            break
        shift = deg_r - deg_b
        q ^= (1 << shift)
        r ^= (b << shift)
    return q, r

def poly_mul(a, b):
    res = 0
    while b > 0:
        if b & 1:
            res ^= a
        a <<= 1
        b >>= 1
    return res

def ext_euclid_gf2(m, a):
    r1, r2 = m, a
    t1, t2 = 0, 1
    step = 1
    print(f"\n{'='*50}")
    print(f"Tìm nghịch đảo của {a} mod {m}")
    print(f"{'='*50}")
    print(f"Khởi tạo : r1 = {r1}, r2 = {r2}")
    print(f"           t1 = {t1}, t2 = {t2}\n")
    
    while r2 > 0:
        q, r = poly_divmod(r1, r2)
        qt2 = poly_mul(q, t2)
        t = t1 ^ qt2
        
        print(f"--- Bước {step} ---")
        print(f"q  = r1 // r2 = {r1} // {r2} = {q}")
        print(f"r  = r1 % r2  = {r}")
        print(f"t  = t1 ^ (q * t2) = {t1} ^ ({q} * {t2}) = {t1} ^ {qt2} = {t}")
        print(f"-> Cập nhật:")
        print(f"   r1 = {r2}, r2 = {r}")
        print(f"   t1 = {t2}, t2 = {t}\n")
        
        r1, r2 = r2, r
        t1, t2 = t2, t
        step += 1
        
    print(f"Kết luận: Nghịch đảo của {a} là {t1}")
    return t1

if __name__ == "__main__":
    # m(x) = x^10 + x^3 + 1 = 10000001001_2 = 1033_10
    m = 1033
    a = 523
    b = 1015
    
    inv_a = ext_euclid_gf2(m, a)
    inv_b = ext_euclid_gf2(m, b)
