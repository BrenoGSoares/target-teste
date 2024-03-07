# 2
# 0, 1 // a, b
def fib(number):
    if number == 0:
        return True
    a, b = 0, 1
    fibo = b
    while fibo < number:
        fibo = a + b
        a, b = b, fibo

    return fibo == number


num = int(input())
if fib(num):
    print(f"{num} está presente na sequência")
else:
    print(f"{num} não está presente na sequência")

# 5

word = list(str(input()))
new_word = []
for letter in range(len(word) - 1, -1, -1):
    new_word.append(word[letter])
print("".join(new_word))
