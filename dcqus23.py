d={'a':2,'b':34,'c':56,'d':65,'e':536,'f':10,'g':100}
max=0
smax=0
thmax=0
m=0
s=0
t=0
for i in d.keys():
    if d[i]>max:
        thmax=smax
        t=s
        smax=max
        s=m
        max=d[i]
        m=i   
    if d[i] !=max and d[i]>smax:
        thmax=smax 
        t=s
        smax=d[i]
        s=i
    if d[i]!=max and d[i] !=smax and d[i]>thmax:
        thmax=d[i]
        t=i
print(m,s,t)