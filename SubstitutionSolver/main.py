import string, sys

### TODO ###
# - Dynamic alphabet support
############


def help(err=None):
    if err: print("ERROR: "+err)
    print("Usage: python3 {sys.argv[0]} [substitution_alphabet]")
    exit()

template_alphabet = string.ascii_uppercase+" "
#template_alphabet = string.ascii_uppercase
substitution_alphabet = ""
try:
    substitution_alphabet = sys.argv[1]
except:
    help("Substitution alphabet not provided.")

if (len(substitution_alphabet) != len(template_alphabet)):
    help("Alphabets are not equal lengths.")


ciphertext = ""
try:
    ciphertext = sys.argv[2]
except:
    pass


# Generate encryption hashmap
encryption_map = {}
decryption_map = {}
for i in range(len(template_alphabet)):
    encryption_map[template_alphabet[i]] = substitution_alphabet[i]
    decryption_map[substitution_alphabet[i]] = template_alphabet[i]
    #print(template_alphabet[i] + " : " + substitution_alphabet[i])

# Calculate decryption permutation
template_increment = 0
dec_list = list(decryption_map)
dec_list.sort()
print("DECRYPTION KEY: " + "".join(decryption_map[x] for x in dec_list))

# Decrypt ciphertext if present
plaintext = ""
if (ciphertext != ""):
    for c1 in ciphertext:
        for c2 in dec_list:
            if c1 == c2:
                plaintext += decryption_map[c2]

print(plaintext)
