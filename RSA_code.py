import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception("Modular inverse does not exist")
    return x % phi

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_keys():
    p = q = 0
    while not is_prime(p):
        p = random.randint(100, 300)
    while not is_prime(q) or q == p:
        q = random.randint(100, 300)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

if __name__ == "__main__":
    print("RSA Encryption/Decryption System")
    
    message = input("Enter a message to encrypt: ")

    public_key, private_key = generate_keys()
    print("\nPublic Key:", public_key)
    print("Private Key:", private_key)

    encrypted_msg = encrypt(message, public_key)
    print("\nEncrypted Message:", encrypted_msg)

    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Decrypted Message:", decrypted_msg)
