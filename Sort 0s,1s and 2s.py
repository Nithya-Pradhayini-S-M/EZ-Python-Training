a=[0,2,1,2,0,1]
z=0
f=0
s=0
for i in range(0,len(a)):
    if a[i] == 0:
        z += 1
    elif a[i] == 1:
        f += 1
    else:
        s += 1
j=0
while z>0:
    a[j] = 0
    j += 1
    z -= 1
while f>0:
    a[j] = 1
    j += 1
    f -= 1
while s>0:
    a[j] = 2
    j += 1
    s -= 1
print(a)