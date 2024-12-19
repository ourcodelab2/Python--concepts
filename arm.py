def is_armstrong(n):
num_str = str(n)
power = len(num_str)
sum_digits = sum(int(digit) ** power for digit in num_str)
return sum_digits == n
n = int(input("Enter a number: "))
if is_armstrong(n):
print(f"{n} is an Armstrong number.")
else:
print(f"{n} is not an Armstrong number.")