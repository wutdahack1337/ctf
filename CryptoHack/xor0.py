from pwn import *

cipher_text = b"label";
key = 13;

print("crypto{" + "".join(xor(x, key).decode() for x in cipher_text) + "}");