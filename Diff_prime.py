'''
Problem Statement:

In the enchanted land of Numeria, Alice is on a quest to find the legendary
Prime Key to unlock the ancient Vault of Secrets. The vault's guardian, an
ancient sphinx, presents a multi-step puzzle that Alice must solve to obtain the
Prime Key.

The puzzle consists of multiple levels, each requiring Alice to solve a different
challenge involving prime numbers. To progress through each level, Alice must
perform the following tasks:

Level 1: Find the smallest prime number larger than a given integer N.

Level 2: Calculate the sum of all prime numbers between N and the smallest
prime number larger than N.

Level 3: Determine if the product of the smallest prime number larger than N
and the next immediate prime number is also a prime.

To complete the puzzle and retrieve the Prime Key, Alice must solve these
challenges in sequence for a given integer N.

Your task is to write a function that takes an integer N and returns a tuple
containing the following:

- The smallest prime number larger than N (Level 1 result).
- The sum of all prime numbers between N and the smallest prime number
larger than N (Level 2 result).
- A boolean indicating whether the product of the smallest prime number
larger than N and the next immediate prime number is prime (Level 3 result).
Help Alice navigate through the levels, solve the puzzle, and obtain the Prime
Key to unlock the Vault of Secrets

'''


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
       if n%i == 0:
          return False
    return True
n = int(input("Enter N:"))
res=is_prime(n)
if res == True:
    print("Yes")
else:
    print("No")
k=n+1
l=[]
while True:
    res=is_prime(k)
    if res==True:
        l.append(k)
        break
    else:
        k += 1
sum=0
for i in range(n+1,k):
    sum += i
l.append(sum)

p1=k
k=p1+1
while True:
    res=is_prime(k)
    if res==True:
        p2=k
        break
    else:
        k += 1
p3=p1*p2
res=is_prime(p3)
if res==True:
    l.append(False)
else:
    l.append(True)
a=tuple(l)
print(a)