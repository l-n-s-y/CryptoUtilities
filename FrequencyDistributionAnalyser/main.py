import string, sys

ciphertext = ""
try:
    ciphertext = sys.argv[1]
except:
    print("USAGE: python3 {sys.argv[0]} [ciphertext]")
    exit()

char_distributions = {}
for char in string.ascii_uppercase:
    char_distributions[char] = 0
    for c in ciphertext:
        if c.upper() == char:
            char_distributions[char] += 1

for i in char_distributions:
    if (char_distributions[i] == 0): continue
    print(i + ": " + str(char_distributions[i]) + " - " + str(round((char_distributions[i]/len(ciphertext.replace(" ",""))*100),2))+"%")
