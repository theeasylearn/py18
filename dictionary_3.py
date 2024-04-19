#create dictionary 
python = {"name":"Introduction to python","duration":90,"fees":7500.99,"isCertified":True}
print(python)

print(python.keys())

print(python.values())

student = ['name','surname','age','gender']

vidhi = dict.fromkeys(student)

print(vidhi)
vidhi['name'] = "Vidhi"
vidhi['gender'] = False
print(vidhi)

print(python.items())

print(python.get("duration"))
print(python['duration'])


print(python.get("trainer","not found"))
# print(python['trainer']) #error