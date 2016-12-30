ans = 0
d=[]
for i in objects:
    if i not in d:
        d.append(i)
        ans +=1
print(ans)