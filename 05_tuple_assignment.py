# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
N=tuple(range(10))
print(f"first 10 natural numbers:{N}")

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
N=(1,2,3,4,5,6,7,8,9,10)
print(len(N))
print(f"the length of tuple:{N}")

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
N=('a', 'b', 'c', 'd', 'e')
x=N[2]
print(f"Access the 3rd element from tuple:{x}")

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
N=(23, 45, 12, 67, 34, 89, 56)
M=max(N)
print(f"the maximum value in tuple:{M}")

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
N=(1, 5, 2, 5, 3, 5, 4, 5, 6)
M=N.count(5)
print(M)

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
N=(19,6.9,"cricket","true")
print(f"a tuple of mixed data types:{N}")


# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
N= ('java', 'python', 'c++', 'javascript')
M=(N.index('python'))
print(f"the index of element 'python' in :{M}")

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
N=(10, 20, 30, 40, 50)
M=(25 in N)
print(f"25 exists in tuple:{M}")

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
N=tuple(range(0,10,2))
print(N)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
N=(15, 23, 31, 42, 56, 78)
M=sum(N)/len(N)
print(f"the average of numbers:{M}")