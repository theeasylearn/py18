#write a program to print 2 digit amount into words 
#input 67
#output six seven

list = ['zero ','one ','two ','three','four ','five ','six ','seven ','eight ','nine']
number = input("Enter number")
number = int(number)

last_reminder = number%10 #7
number=number//10 #6
print(list[number]," ",list[last_reminder])

