my_dict = {'a':50,'b':58, 'c':56,'d':40,'e':100,'f':20}
max=0
smax=0
thmax=0
max1=0
smax2=0
thmax3=0
for i in my_dict:
    if my_dict[i]>max:
        thmax=smax
        thmax3=smax2
        smax=max
        smax2=max1
        max=my_dict[i]
        max1=i
    elif my_dict[i]>smax:
        thmax=smax
        thmax3=smax2
        smax=my_dict[i]
        smax2=i
    elif my_dict[i]>thmax:
        thmax=my_dict[i]
        thmax3=i
print(max,smax,thmax)
print(max1,smax2,thmax3)
