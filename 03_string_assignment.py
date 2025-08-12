# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")



# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
N='racecar'
def is_palindrome_slice(N):
    return text == (-1)
print(f"palindrome_slice:{N}")

# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
import math
N='Python is a great programming language'
M=(len(N))
print(f"Count the number of words:{M}")


# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
N=('hello world')
print(N.title())

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
N=('Data Science')
M=(len(N))
print(f"the length of string:{M}")

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
original_string=('Machine Learning')
modified_string=original_string.replace(('Machine Learning'),('machine learning'))
print(f"Replace all spaces with underscores:{modified_string}")


# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
Srting= "Python Programming Language"
String1 = "Python"
if String1 in Srting:
    print(True)
else:
    print(False)


# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
N='Artificial Intelligence'
first_five_strings = N[5]
print(f"Extract the first 5 characters:{first_five_strings}")


# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
original_string='UPPERCASE'
modified_string=original_string.lower()
print(f"Convert:{modified_string}")

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
srt='Computer Science'
vowels=('a','e','i','o','u')
for i in srt:
    if i not in vowels:
        print(i,end='')


# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")



# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
string1='listen'
string2='silent'
if sorted(string1)==sorted(string2):
    print('anagrams')

# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
N='python programming language'
m=(N.title())
print(m)


# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
N='Hello World'
vowels='aeiou'
count=0
for i in N:
    if i not in vowels:
        count +=1

print(count)


# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
N='Python is a programming language'
M=N.split()
max_word=""
max_len=0


print(count)


# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
N=('Hello, World! How are you?')
import string
for i in N:
    if i not in string.punctuation:
        print(i,end='')


# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
import string
N=('Python')
M=(N.startswith('Python'))
print(M)

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
N='Hello World'
L='o'
M=(N.index(L))
print(M)

# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
N=('apple,banana,orange')
M=('comma')
L=N.split(M)
print(L)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
N=['Python', 'is', 'awesome']
M=

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
# Your code here

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
# Your code here

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
# Your code here

# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
# Your code here

# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
# Your code here

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
# Your code here

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
# Your code here

# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
# Your code here

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
# Your code here

# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
# Your code here

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
# Your code here

# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
# Your code here

# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
# Your code here

# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
# Your code here

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
# Your code here

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
# Your code here

# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
# Your code here

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
# Your code here

# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
# Your code here

# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
# Your code here

# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
# Your code here

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")
# Your code here

# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
# Your code here

# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
# Your code here

# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
# Your code here

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
# Your code here

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")
# Your code here

# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
# Your code here

# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
# Your code here 