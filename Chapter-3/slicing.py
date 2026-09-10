str=("GulabJamun")
firsthalf= str[0:5]
secondhalf= str[ : 5]
therd=str[5:7]
print(firsthalf)
print(secondhalf)
print(therd)

#question- write a programm that take your favourite food name as input and prints
#1-the middle 3 charecter
#2-the last 2 charecter

str = input("Enter the value")
mid=len(str)//2
output=str[mid-1:mid+1]
print(output)

output2=str[-2:]
print(output2)

