# Morgan Browning - SDEV 245
# Module 2: Encrypt/Decrypt Demo
# This shows a basic example of symmetric and asymmetric encryption.

# -------------------------------
# SYMMETRIC ENCRYPTION (Caesar)
# Same key used to encrypt AND decrypt
# -------------------------------

def symmetric_encrypt(message, key):
    result = ""
    for char in message:
        # shift each character forward
        result += chr((ord(char) + key) % 256)
    return result

def symmetric_decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        # shift characters back using same key
        result += chr((ord(char) - key) % 256)
    return result


# -------------------------------
# ASYMMETRIC ENCRYPTION (Simple RSA demo)
# Public key encrypts, private key decrypts
# -------------------------------

# Very small prime numbers (NOT real security)
p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)

# public exponent
e = 7

# find private exponent (d)
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

d = mod_inverse(e, phi)

def rsa_encrypt(message, e, n):
    # encrypt each character as a number
    return [(ord(char) ** e) % n for char in message]

def rsa_decrypt(cipher_list, d, n):
    # convert numbers back to characters
    return ''.join([chr((num ** d) % n) for num in cipher_list])


# -------------------------------
# MAIN PROGRAM
# -------------------------------

message = "hello world"
print("Original message:", message)

# --- Symmetric demo ---
sym_key = 3
sym_encrypted = symmetric_encrypt(message, sym_key)
sym_decrypted = symmetric_decrypt(sym_encrypted, sym_key)

print("\n--- Symmetric Encryption (Caesar shift) ---")
print("Key used:", sym_key)
print("Encrypted:", sym_encrypted)
print("Decrypted:", sym_decrypted)

# --- Asymmetric demo ---
rsa_encrypted = rsa_encrypt(message, e, n)
rsa_decrypted = rsa_decrypt(rsa_encrypted, d, n)

print("\n--- Asymmetric Encryption (RSA demo) ---")
print("Public key (e, n):", (e, n))
print("Private key (d, n):", (d, n))
print("Encrypted:", rsa_encrypted)
print("Decrypted:", rsa_decrypted)
