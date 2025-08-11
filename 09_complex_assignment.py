# COMPLEX DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Create a complex number and find its conjugate
print("SOLVED EXAMPLE:")
print("Create a complex number and find its conjugate")
z = 3 + 4j
conjugate = z.conjugate()
magnitude = abs(z)
print(f"Complex number: {z}")
print(f"Conjugate: {conjugate}")
print(f"Magnitude: {magnitude}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create complex number 5 + 3j
print("Question 1: Create complex number 5 + 3j")
N=complex(5,3)
print(N)

# Question 2: Find the real part of complex number 7 - 2j
print("\nQuestion 2: Find the real part of complex number 7 - 2j")
N=(7 - 2j)
real_part=N.real
print(real_part)


# Question 3: Find the imaginary part of complex number 4 + 6j
print("\nQuestion 3: Find the imaginary part of complex number 4 + 6j")
N=(4 + 6j)
M=N.imag
print(M)


# Question 4: Add two complex numbers: (3 + 2j) and (1 + 4j)
print("\nQuestion 4: Add two complex numbers: (3 + 2j) and (1 + 4j)")
N=(3 + 2j)
M=(1 + 4j)
L=N+M
print(L)

# Question 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)
print("\nQuestion 5: Multiply two complex numbers: (2 + 3j) and (1 + 2j)")
N=(2 + 3j)
M=(1 + 2j)
L=N*M
print(L)

# Question 6: Find the magnitude of complex number 6 + 8j
print("\nQuestion 6: Find the magnitude of complex number 6 + 8j")
N=(6 + 8j)
M=abs(N)
print(M)

# Question 7: Find the conjugate of complex number 5 - 7j
print("\nQuestion 7: Find the conjugate of complex number 5 - 7j")
N=( 5 - 7j)
M=N.conjugate
print(M)

# Question 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)
print("\nQuestion 8: Subtract complex numbers: (10 + 5j) - (3 + 2j)")
N=(10 + 5j)
M=(3 + 2j)
L=N-M
print(L)

# Question 9: Divide complex numbers: (8 + 6j) / (2 + 1j)
print("\nQuestion 9: Divide complex numbers: (8 + 6j) / (2 + 1j)")
N=(8 + 6j)
M=(2 + 1j)
L=N/M
print(L)


# Question 10: Find the phase angle of complex number 1 + 1j
print("\nQuestion 10: Find the phase angle of complex number 1 + 1j")
import cmath
z = 1 + 1j
angle = cmath.phase(z)
print(f"Phase angle in radians:", angle)


