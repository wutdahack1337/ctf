cipher_text = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d";

for i in range(0, len(cipher_text), 2):
	num = int(cipher_text[i:i+2], 16);
	print(chr(num), end='');
print();

print(bytes.fromhex(cipher_text));