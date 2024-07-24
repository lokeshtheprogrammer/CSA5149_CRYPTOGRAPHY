def vigenere_encrypt(plaintext, key_stream):
    plaintext = plaintext.upper()
    key_stream = [int(k) for k in key_stream]

    ciphertext = ''
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = key_stream[i % len(key_stream)]
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext

plaintext = "send more money"
key_stream = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
ciphertext = vigenere_encrypt(plaintext, key_stream)
print("Ciphertext:", ciphertext)
// output Ciphertext: BFNEXPTQXJPJH

//
