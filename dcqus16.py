dic1 = ["Rash", "Kil", "Varsha"]
dic2= [1, 4, 5]
res = {}
for i in dic1:
    for j in dic2:
        res[i] = j
        dic2.remove(j)
        break  
print(str(res))
