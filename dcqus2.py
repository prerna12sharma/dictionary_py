d='w3resource'
s={}
for i in d:
	if i in s:
		s[i] += 1
	else:
		s[i] = 1
print (s)