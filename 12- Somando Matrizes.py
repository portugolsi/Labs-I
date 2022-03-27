m1 = [[],[],[]]
m2 = [[],[],[]]
m3 = [[],[],[]]

for matriz in m1:
    for linha in range(0,3):
        a = int(input().strip())
        matriz.append(a)
for matriz in m2:
    for linha in range(0,3):
        a = int(input().strip())
        matriz.append(a)
for matriz in range(0,3):
    for lista in range(0,3):
        m3[matriz].append(m1[matriz][lista]+m2[matriz][lista])


print(m1)
print(m2)
for lista in m3:
    print(lista)