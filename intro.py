#1
for i in range(20, 9, -1):
    print(i)

#2
a = [i for i in range(20, 9, -1)]
print(a)
print("Hello")

#3
for i in range(20, 9, -1):
    if i % 2 == 0:
        print(i)
print("World")

#4
b = [i for i in range(20, 9, -1) if i % 2 == 0]
print(b)

#5
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):          #only need to test from 3 to the square root of n
        if n % i == 0:
            return False
    return True

print is_prime(2) #True
print is_prime(4) #False
print is_prime(7) #True
print is_prime(13) #True

#6