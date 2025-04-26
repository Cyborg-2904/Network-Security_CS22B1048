Network-Security_Assignment_CS22B1048
RSA Algorithm Implementation 🔐
This project implements the RSA public-key cryptosystem using Python. It's a part of the Network Security course assignment (CS1702) at the National Institute of Technology Puducherry, submitted by Sandeep U (CS22B1050).

📚 Introduction
RSA (Rivest–Shamir–Adleman) is one of the first and most widely-used public-key cryptographic systems. It enables secure communication by allowing public encryption and private decryption.

RSA is based on the computational difficulty of factoring large composite numbers, a challenge known as the factoring problem.

🔑 How RSA Works
Choose two large prime numbers p and q.
Compute:
n = p * q
φ(n) = lcm(p−1, q−1)
Select a public key e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1.
Compute the private key d, where d ≡ e⁻¹ mod φ(n).
Encryption: c ≡ m^e mod n
Decryption: m ≡ c^d mod n
