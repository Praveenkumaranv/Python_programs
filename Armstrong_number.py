
#get a input from a user
input1=input("Enter the Number to Check\n")
count=len(input1)
number=int(input1) 
number1=number
result=0
i=0

while(i<=count):
    a=number%10         # To break the number
    b=a**count          # Power the Number
    result+=b
    number//=10         # To divide the number
    i+=1

if number1==result:
    print(str(number1) + (" is a Armstrong Number"))
else:
    print(str(number1) + (" is a not a  Armstrong Number"))
    





