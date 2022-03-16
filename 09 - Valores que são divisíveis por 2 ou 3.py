n1 = int(input().strip())
n2 = int(input().strip())
for k in range(n1,n2+1):
    if (k%2==0) or (k%3==0):
        print(k)
