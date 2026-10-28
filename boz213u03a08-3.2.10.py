user_word = input("Please enter a word:").upper()

for letter in user_word:
    if letter in "AIUEOÜİÖ" :
        continue
    print(letter)
