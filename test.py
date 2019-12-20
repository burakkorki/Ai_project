a = [("6", 'TOM'), ("1", 'HOWIE'), ("2", 'AKIND'), ("3", 'HANKS'), ("4", 'AYE')]

a = sorted(a,reverse=False)
print(a)

for i in range(0,len(a)):
    print(a[i][0])