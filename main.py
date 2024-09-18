from morse_code import code
print("Welcome to The Morse Code Converter\n")
response = input("Code to convert: \n>").lower()

split = list(response)
converted = []
for letter in split:
    if letter not in code:
        continue
    else:
        coded = code[letter]
        converted.append(coded)
print(f"{''.join(converted)}")

