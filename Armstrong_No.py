n = int(input("Enter num:"))
ans = 0
count = 0
n1 = n
org = n
while n > 0:
    count += 1
    n //= 10
while n1 > 0:
    digit = n1 % 10  # Corrected this line
    p = digit ** count
    ans += p
    n1 //= 10
if ans == org:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
