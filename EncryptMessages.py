import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

def encrypt(key, plaintext):
    # convert the key to bytes
    key = key.encode()

    # create a Cipher object using the key and the AES algorithm in ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    # create an encryptor using the Cipher object
    encryptor = cipher.encryptor()

    # pad the plaintext to a multiple of 16 bytes
    padder = padding.PKCS7(128).padder()
    plaintext_padded = padder.update(plaintext.encode()) + padder.finalize()

    # encrypt the padded plaintext
    ciphertext = encryptor.update(plaintext_padded) + encryptor.finalize()

    # encode the ciphertext as base64
    ciphertext_base64 = base64.b64encode(ciphertext)

    return ciphertext_base64

def decrypt(key, ciphertext_base64):
    # convert the key to bytes
    key = key.encode()

    # decode the base64-encoded ciphertext
    ciphertext = base64.b64decode(ciphertext_base64)

    # create a Cipher object using the key and the AES algorithm in ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())

    # create a decryptor using the Cipher object
    decryptor = cipher.decryptor()

    # decrypt the ciphertext
    plaintext_padded = decryptor.update(ciphertext) + decryptor.finalize()

    # unpad the decrypted plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(plaintext_padded) + unpadder.finalize()

    return plaintext.decode()

# define a key and a plaintext message
key = "my secret key"
plaintext = "Hello, world!"

# encrypt the plaintext
ciphertext_base64 = encrypt(key, plaintext)
print("Ciphertext (base64-encoded):", ciphertext_base64)

# decrypt the ciphertext
decrypted_plaintext = decrypt(key, ciphertext_base64)
print("Decrypted plaintext:", decrypted_plaintext)
