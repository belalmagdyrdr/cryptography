def remove_duplicates(keyword):
    keyword = keyword.upper().replace('J', 'I')
    result = []
    for char in keyword:
        if char not in result:
            result.append(char)
    return ''.join(result)

def generate_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = remove_duplicates(keyword)
    for char in alphabet:
        if char not in matrix:
            matrix += char
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def process_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    pairs = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] != text[i+1]:
            pairs.append(text[i:i+2])
            i += 2
        else:
            pairs.append(text[i] + 'X')
            i += 1
    return pairs

def encrypt(plaintext, matrix):
    pairs = process_text(plaintext)
    ciphertext = ''
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]
    return ciphertext

def decrypt(ciphertext, matrix):
    pairs = process_text(ciphertext)
    plaintext = ''
    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    matrix = generate_playfair_matrix(keyword)
    
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(' '.join(row))
    
    choice = input("\nDo you want to encrypt or decrypt? (E/D): ").upper()
    if choice == 'E':
        plaintext = input("Enter the plaintext: ")
        encrypted_text = encrypt(plaintext, matrix)
        print(f"Encrypted Text: {encrypted_text}")
    elif choice == 'D':
        ciphertext = input("Enter the ciphertext: ")
        decrypted_text = decrypt(ciphertext, matrix)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
