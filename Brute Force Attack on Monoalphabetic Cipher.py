import itertools

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(ciphertext, key):
    translation_table = str.maketrans(key, alphabet)
    return ciphertext.translate(translation_table)

def brute_force_attack(ciphertext):
    all_permutations = itertools.permutations(alphabet)
    possible_decryptions = []

    for perm in all_permutations:
        key = ''.join(perm)
        decrypted_text = decrypt(ciphertext, key)
        possible_decryptions.append(decrypted_text)

    return possible_decryptions

encrypted_message = input("Enter the encrypted message: ").upper()

decrypted_texts = brute_force_attack(encrypted_message)

print("\nPossible decrypted texts:")
for i, text in enumerate(decrypted_texts, 1):
    print(f"Option {i}: {text}")
```