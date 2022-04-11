person={"name":"jack","age":20,"gender":"male",4:{"organisation":"navgurukul","place":"dharamsala"}}
print(person["gender"])
x=person.get(4)
print(x)
y=person[4]["place"]
print(y)