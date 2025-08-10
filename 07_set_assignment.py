# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
N=set(range(10))
print(f"a set of first 10 natural numbers:{N}")

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
N={1, 2, 3, 4, 5}
N.add(11)
print(f"element 11 to set:{N}")

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
N={1, 2, 3, 4, 5, 6}
N.remove(3)
print(f"Remove element 3 from set:{N}")

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
N={1, 2, 3, 4, 5}
M={4, 5, 6, 7, 8}
L=N.intersection(M)
print(f"the intersection of:{L}")

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
N={1, 2, 3, 4, 5}
M={4, 5, 6, 7, 8}
L=N.difference(M)
print(f"difference between:{L}")

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
N={1, 2, 3, 4, 6, 7, 8}
print(5 in N)

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
N={'a', 'b', 'c', 'd', 'e'}
print(len(N))
print(f"the length of set:{N}")

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
N='hello world'
vowels={'a','e','i','o','u'}
vowels_set=set()
for i in N:
    if i in vowels:
        vowels_set.add(i)
print(f"Create a set of vowels from string:{vowels_set}")


# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
N=[1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
M=set(N)
print(f"duplicates from list:{M}")

# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
N={1, 2, 3}
M={1, 2, 3, 4, 5, 6}
L=N.issubset(M)
print(f"subset of:{L}")