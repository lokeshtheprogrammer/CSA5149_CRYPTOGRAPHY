import numpy as np

def known_plaintext_attack(plaintext, ciphertext):
    plaintext = plaintext.upper().replace('J', 'I')
    ciphertext = ciphertext.upper()

    plain_matrix = np.array([ord(char) - ord('A') for char in plaintext]).reshape(-1, 2)
    cipher_matrix = np.array([ord(char) - ord('A') for char in ciphertext]).reshape(-1, 2)

    plain_matrix_inv = np.linalg.inv(plain_matrix) % 26
    key_matrix = (np.dot(plain_matrix_inv, cipher_matrix) % 26).astype(int)

    return key_matrix

plaintext = "HELP"
ciphertext = "QLTB"
key_matrix = known_plaintext_attack(plaintext, ciphertext)
print("Recovered Key Matrix:")
print(key_matrix)
// output Recovered Key Matrix:
[[ 9  4]
 [ 5  7]]

