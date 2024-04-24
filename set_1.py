#create set 
fruits = {"apple","banana","pinapple"}

print(fruits)

fruits.add("graps")
fruits.add("kiwi")

print(fruits)
fruits.add("graps")
print(fruits)

fruits.remove("graps")
print(fruits)

set1 = {10,20,30,40,50}
set2 = {40,50,60,70,80}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)

print(union)
print(intersection)
print(difference)

