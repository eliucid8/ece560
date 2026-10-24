#!/usr/bin/env python3
import base64
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.exceptions import InvalidSignature
import zlib

# TODO: prompt user for key
# TODO rewrite using fernet...

def main():
    if len(sys.argv) < 4:
        print("""Syntax:
    To encrypt: `./duke-crypter -e <input_file> <output_file>`

    To decrypt: `./duke-crypter -d <input_file> <output_file>`""")
        return 

    with open(sys.argv[2], 'rb') as f:
        message = f.read()

        password = input("Enter password: ").encode("utf-8")
        salt = "Tyler K. Bletsch".encode("ascii")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1_200_000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        encryptor = Fernet(key)

        if sys.argv[1] == "-e":
            message_encrypted = encryptor.encrypt(message)
            message_compressed = zlib.compress(message_encrypted, level=9)

            # print(f"Secret Key: {key.hex()}")
            # print(f"Public Initialization Vector: {initialization_vector.hex()}")
            # print(f"Encrypted Message: {message_encrypted.hex()}")
            with open(sys.argv[3], 'wb') as out:
                _ = out.write(message_compressed)
            return 

        elif sys.argv[1] == "-d":
            message_decompressed = zlib.decompress(message)
            try: 
                message_decrypted = encryptor.decrypt(message_decompressed)
            except Exception as e:
                with open(sys.argv[3], 'w') as out:
                    _ = out.write("")
                print(f"{e}: key does not match signature")
                sys.exit(1)

            # print(f"Decrypted Message: {message_decrypted.decode()}")

            with open(sys.argv[3], 'wb') as out:
                _ = out.write(message_decrypted)
            return

if __name__ == "__main__":
    main()


