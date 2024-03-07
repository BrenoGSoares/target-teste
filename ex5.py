# 5

word = list(str(input()))
new_word = []
for letter in range(len(word) - 1, -1, -1):
    new_word.append(word[letter])
print("".join(new_word))
