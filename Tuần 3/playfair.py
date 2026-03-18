import string

def generate_playfair_square(key):
    key = "".join([c.upper() for c in key if c.isalpha()])
    key = key.replace("J", "I")
    seen = set()
    square = []
    # Kết hợp key và bảng chữ cái, loại bỏ J
    for c in key + string.ascii_uppercase:
        if c not in seen and c != "J":
            seen.add(c)
            square.append(c)
    return [square[i * 5 : (i + 1) * 5] for i in range(5)]

def prepare_text(text):
    text = "".join([c.upper() for c in text if c.isalpha()])
    text = text.replace("J", "I")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        # Kiểm tra nếu còn ký tự tiếp theo
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2
        else:
            # Nếu chỉ còn 1 ký tự cuối
            result += a + "X"
            i += 1
    return result

def find_position(square, char):
    for i, row in enumerate(square):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    square = generate_playfair_square(key)
    text = prepare_text(plaintext)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = find_position(square, a)
        r2, c2 = find_position(square, b)
        if r1 == r2:  # Cùng hàng: dịch phải
            result += square[r1][(c1 + 1) % 5] + square[r2][(c2 + 1) % 5]
        elif c1 == c2:  # Cùng cột: dịch xuống
            result += square[(r1 + 1) % 5][c1] + square[(r2 + 1) % 5][c2]
        else:  # Hình chữ nhật: tráo đổi cột
            result += square[r1][c2] + square[r2][c1]
    return result

def playfair_decrypt(ciphertext, key):
    square = generate_playfair_square(key)
    result = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        r1, c1 = find_position(square, a)
        r2, c2 = find_position(square, b)
        if r1 == r2:  # Cùng hàng: dịch trái
            result += square[r1][(c1 - 1) % 5] + square[r2][(c2 - 1) % 5]
        elif c1 == c2:  # Cùng cột: dịch lên
            result += square[(r1 - 1) % 5][c1] + square[(r2 - 1) % 5][c2]
        else:
            result += square[r1][c2] + square[r2][c1]
    return result

if __name__ == "__main__":
    key = "MONARCHY"
    plaintext = "doyouliketostudyACRYPTOGRAPHYCOURSE "

    encrypted = playfair_encrypt(plaintext, key)
    decrypted = playfair_decrypt(encrypted, key)
    
    print(f"Key : {key}")
    print(f"Plaintext : {plaintext}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")