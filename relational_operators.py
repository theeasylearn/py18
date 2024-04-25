#relational operators & logical operators in python 
a=10
b=20
c=30

print(f"a={a} b={b} c={c}")

#findout whether a and b are same or not 
result = a==b
print(f"{a}=={b} = {result}")

#findout whether a and c are different or not 
result = a!=b
print(f"{a}!={c} = {result}")

#findout whether a is smaller then b or not
result = a<b
print(f"{a}<{c} = {result}")

#findout whether b is greter then c or not
result = b>c
print(f"{b}>{c} = {result}")


#findout whether c is less then or equal to b
result = c<=b
print(f"{c}<={b} = {result}")

#findout whether c is greter then or equal to b
result = c>=b
print(f"{c}>={b} = {result}")

#logical operators
result = a==b and b==c
print(f"{a}=={b} and {b}=={c} = {result}")

result = a!=b and b!=c
print(f"{a}!={b} and {b}!={c} = {result}")


result = a>b and b>c
print(f"{a}>{b} and {b}>{c} = {result}")


result = a>b or b<c
print(f"{a}>{b} and {b}<{c} = {result}")

result = a==a or b==b
print(f"{a}=={a} and {b}=={b} = {result}")

result = a==b or b==c
print(f"{a}=={a} or {b}=={b} = {result}")

result = not (a==b and b==c)
print(f"not {a}=={b} and {b}=={c} = {result}")