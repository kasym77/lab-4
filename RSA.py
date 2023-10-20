import math

word = input("Enter the word ")

ascii_codes = []
ascii_sypher = []
ascii_plain = []

word_s =[]
word_p = []

def is_integer(float_number):
    return float_number.is_integer()

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
while True:
    p = int(input("enter p "))
    q = int(input("enter q "))
    if is_prime(p) and is_prime(q) and p*q > 130:
        break
    print("numbers aren't prime or multiple small than 130")

n = q*p
fi = (p-1)*(q-1)

print(n)
print(fi)
e=1
d=1

for i in range(1,fi):
    if is_prime(i) and fi%i!=0:
        e = i
        print(e)
        break



for i in range(1,1000):
    x = ((i*fi)+1)/e
    if is_prime(x) and is_integer(x):
        d=int(x)
        print(x)
        break


for letter in word:
    ascii_code = ord(letter)
    ascii_codes.append(ascii_code)

print(ascii_codes)


for i in ascii_codes:
    y = (i**e)%n
    ascii_sypher.append(y)
print(ascii_sypher)

for i in ascii_sypher:
    word_s.append(chr(i))
print(word_s)


for i in ascii_sypher:
    y = (i**d)%n
    ascii_plain.append(y)
print(ascii_plain)

for i in ascii_plain:
    word_p.append(chr(i))
print(word_p)