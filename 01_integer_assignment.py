# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
N=[0,1,2,3,4,5,6,7,8,9,10]
sum_10_natural_numbers = sum(N)
print(f"natural number N:{sum_10_natural_numbers}")


# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
N=(156%7)
print(N)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
N=(25)
M =(N*N)
print(f"the square of 25 is :{M}")

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
N=(125)
p=N**(1/3)
print(f"the cube root of 125 is : {p}")

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
N=(1,2,3,4,5)
sum_of_digits=sum(N)
print(f"sum of digit in number 1,2,3,4,5:{N}")


# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
for i in range(97):
 if i/2 == 0:
    print("97 is prime number")
 else:

    print(i,end=',')


# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
N=(8*7*6*5*4*3*2*1)
print(f"the factorial of 8:{N}")

  
# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
N=(15,23,31,42,56)
M=sum(N)
O=(M/5)
print(f"the average of numbers: 15, 23, 31, 42, 56:{O}")

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
import math
N=48
M=36
P=math.gcd(36,48)
print(f"GCD of {P}")

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
M=(1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39)
N=sum(M)
print(f"odd numbers 20:{N}")