
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num_str = str(num1) + str(num2) + str(num3)

def armstrong(num1,num2,num3): 
    value1 = num1*num1*num1
    value2 = num2*num2*num2
    value3 = num3*num3*num3
    sum = value1+value2+value3
    return sum
  
if int(num_str) == armstrong(num1,num2,num3):
    print("This is armstrong number")
else:
    print("This is not armstrong number")