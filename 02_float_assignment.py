# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
N=[3.14,2.718,1.618,0.577]
average=(sum (N)/len (N))
print(f"average of:{average} ")


# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
Fahrenheit=[98.6]
celsius=(98.6 - 32 * 9 / 5)
print(f" Celsius of:{celsius}")


# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
N=1000
I=5.5
T=3
interest=(N*(1+I/T)**I*T)
print(f"compound interest:{interest}")


# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
side1=3.5
side2=4.2
hypotenuse=math.sqrt((side1*side1)+(side2*side2))
print(f"hypotenuse of a right triangle:{hypotenuse}")


# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
N=7.8
volume=(4/3*3.14*(N*N*N))
print(f"volume of a sphere:{volume}")


# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
N=3.14159
round=(N,3)
print(f"decimal places:{round}")

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
N=45
M=67
percentage=(45/67)
print(f"the percentage:{percentage}")

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
N=23.456
M=(N*N)
print(f"the square root of:{M}")

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
N=2500
R=6.5
T=2.5
interest=N*(1+R*T)
print(f" simple interest:{interest}")

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
N=45.7
radians=N*(3.14/180)
print(f"degrees to radians:{radians}")