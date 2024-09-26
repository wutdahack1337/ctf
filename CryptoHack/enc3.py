import base64;

cipher_text = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf";
cipher_text = bytes.fromhex(cipher_text);

print(base64.b64encode(cipher_text));