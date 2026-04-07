# Cryptography Notes

## Caesar Cipher
- Simple substitution cipher using a shift
- Encrypts character by character

### Weaknesses:
- Small key space → vulnerable to brute force
- Preserves structure → vulnerable to frequency analysis

---

## Block Ciphers
- Encrypt blocks of plaintext into ciphertext
- Each plaintext character affects multiple ciphertext characters

### Examples:
- DES (56-bit key)
- Triple DES (applies DES three times)
- AES (modern standard, stronger keys)

---

## Secret Key Distribution
- Uses asymmetric encryption

### Key Concepts:
- Public key → used for encryption
- Private key → used for decryption

---

## Affine Cipher

The Affine Cipher is an improvement over the Caesar Cipher by using two keys.

### Formula:
C = (aP + b) mod 26

- `a` = multiplier  
- `b` = shift (offset)  
- `P` = plaintext  
- `C` = ciphertext  

### Key Points:
- Caesar cipher is weak (only 25 possible keys)
- Affine cipher increases complexity using two variables

---

## Decryption & Inverses

To reverse an affine cipher, we need the modular inverse of `a`.

### Finding the inverse:
Find `x` such that:

a · x ≡ 1 (mod 26)

### Brute force method:
- Try values of x from 1 to 25
- Check if (a · x) mod 26 = 1

### Important:
- Not all values of `a` have an inverse
- An inverse exists only if `a` and 26 are coprime (no common factors)

### Example:
- Even numbers and 13 do NOT have inverses mod 26

---

## Cribbing (Known Plaintext Attack)

Cribbing uses known pairs of plaintext and ciphertext to find keys.

### Process:
- Select 2 matching plaintext and ciphertext letters
- Form 2 equations:
  - C₁ = aP₁ + b (mod 26)
  - C₂ = aP₂ + b (mod 26)
- Solve simultaneously to find `a` and `b`

### Tip:
- Subtract equations to eliminate `b`
- Multiply by modular inverse instead of dividing

---

## Frequency Analysis

Used to guess plaintext based on letter frequency.

### Key observations:
- Most common English letters: **E, A, T**
- Common pair: **TH**

### Use case:
- Helps form initial guesses for cribbing

---

## One-Time Pad (OTP)

A theoretically unbreakable cipher when used correctly.

### How it works:
- Sender and receiver share a random key (same length as message)
- Encryption:
  C = (P + K) mod 26

### Key rules:
- Key must be truly random
- Key must be used only once
- Key must be as long as the message

---

## Diffie-Hellman Key Exchange

A method for securely exchanging keys over an insecure channel.

### Setup:
- Public values:
  - Prime number `p`
  - Generator `g` (1 < g < p-1)

### Steps:
1. Alice chooses secret `a`
2. Bob chooses secret `b`

3. Alice computes:
   A = g^a mod p → sends to Bob

4. Bob computes:
   B = g^b mod p → sends to Alice

5. Shared secret:
   - Alice computes: S = B^a mod p
   - Bob computes: S = A^b mod p

👉 Both get the same secret key

---

## Why is it secure?

- An attacker (Eve) knows:
  - g, p, A, B

- But to compute the shared key:
  - She must solve:
    A = g^a mod p

👉 This is computationally hard for large values  
👉 Known as the **discrete logarithm problem**

---

## What I Learned

- Cryptography relies heavily on modular arithmetic
- Security often depends on problems that are easy to compute but hard to reverse
- Practical systems (like Diffie-Hellman) use mathematical properties to secure communicatio
