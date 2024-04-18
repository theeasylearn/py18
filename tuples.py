#concept of tuples

states = ('Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal')
print(states)
#print 1st five states 
print(states[0:5])
#print 1st state
print(states[0])
#print all the state from 5th position onwards
print(states[5:])

# states[0] = 'AP' #it can not change list
print("Position of Gujarat in tuple")
print(states.index("Gujarat"))
print("count of Gujarat in tuple")
print(states.count("Gujarat"))
print('Good bye..')