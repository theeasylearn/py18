#create dictionary 
python = {"name":"Introduction to python","duration":90,"fees":7500.99,"isCertified":True}
print(python)

#access specific value. to access specific value we have to use key
print(python['name'])

#change 
python['name'] = "Basic of python"
print(python)

#delete specific value
del python['name']

print(python)
del python 
