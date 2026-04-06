# Cryptography notes 
Ciphers Learnt from CS110:
  - Caesar: simple and is just a shift
    * easy and fast to do and encodes character by character
    * keep structure on plaintext, vulnerable to frequency analysis, small key space vulnerable to brute force
  - Block Cipher: block of plaintext encoded into block of ciphertext
    * Each plaintext character contributes to multiple cipher text character
  - 3 important symmetric block ciphers
    * Data Encryption Standard (DES)
      - key is 56 bits
    * Triple DES
      - Improvement on DES, uses 3, 56 bit keys and runs DES 3 times
    * Advanced Encryption Standard (AES)
      - Longer keys, with a similar approach to use successive rounds of computation to mix data
  - Secret Key Distribution
    * We use asymmetric encryption for this
    * 2 keys, Public/Private
    * Public Key encrypts (known to public)
    * Private Key decrpts (only known to receiver)
