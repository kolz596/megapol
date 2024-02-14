a = [-3,3,384,0,31,8]
for i in range(1,len(a)):
    for j in range(1,len(a)-1):
        if a[i] < a[j]:
            a[j],a[i] = a[i], a[j]
print(a)