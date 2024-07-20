import morsecode

morse = morsecode.morse_dict
text = input("Enter your text to convert into morse code:").upper()
letters = []
code = ""

for letter in text:
    code += morse[letter]

print(code)