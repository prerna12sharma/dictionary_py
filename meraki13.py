dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
max=0
smax=0
thmax=0
max1=0
smax2=0
thmax3=0
for i in dict.keys():
    if dict[i]>max:
        thmax=smax
        thmax3=smax2
        smax=max
        smax2=max1
        max=dict[i]
        max1=i   
    if dict[i] !=max and dict[i]>smax:
        thmax=smax 
        thmax3=smax2
        smax=dict[i]
        smax2=i
    if dict[i]!=max and dict[i] !=smax and dict[i]>thmax:
        thmax=dict[i]
        thmax3=i
print(max,max1,smax,smax2,thmax,thmax3)
