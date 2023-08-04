import sys
from get_alpha_code import *


ciphertext = ""
key = ""

try:
	key = sys.argv[1]
	ciphertext = sys.argv[2].replace(" ","")
except:
	print("ERROR: Improper arguments.")
	print("USAGE: python3 {sys.argv[0]} [KEY] [CIPHERTEXT]")
	exit();

d = len(key)


plaintext = ""
for i in range(len(ciphertext)):
	plaintext += chr(((alpha_code(ciphertext[i]) - alpha_code(key[i%d]))%26)+65)

print(plaintext)