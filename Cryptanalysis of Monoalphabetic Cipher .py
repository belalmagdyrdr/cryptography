from collections import Counter


def frequency_analysis(ciphertext):
    ciphertext = ciphertext.upper().replace(" ", "")
    freq_count = Counter(ciphertext)
    return freq_count.most_common()


def suggest_decryption(frequency_count):
    english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    decryption_map = {}
    

    for i, (char, _) in enumerate(frequency_count):
        if i < len(english_freq):
            decryption_map[char] = english_freq[i]
    
    return decryption_map


def decrypt_with_map(ciphertext, decryption_map):
    return ''.join(decryption_map.get(char, char) for char in ciphertext)

if __name__ == "__main__":
    ciphertext = input("Enter the encrypted text: ")
    

    frequency_count = frequency_analysis(ciphertext)
    print("Frequency Analysis:", frequency_count)
    

    decryption_map = suggest_decryption(frequency_count)
    print("Suggested Decryption Map:", decryption_map)
    

    decrypted_text = decrypt_with_map(ciphertext, decryption_map)
    print("Most Likely Decrypted Text:", decrypted_text)

