dic="MISSISSIPPI"
s={}
for i in dic:
	if i in s:
		s[i] += 1
	else:
		s[i] = 1
print (s)