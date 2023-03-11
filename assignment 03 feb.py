#!/usr/bin/env python
# coding: utf-8

# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.

# In[ ]:


# def keyword is used to create a function


# In[6]:



def find_odd_numbs():
    l1 = []
    for i in range(0,26):
        if i % 2 != 0:
            l1.append(i)
    return (l1)


# In[7]:


my_list =find_odd_numbs()
print(my_list)


# In[8]:


def odd_numb():
    l1 =[]
    for i in range(0,26):
        if i % 2 !=0:
            l1.append(i)
    return l1


# In[9]:


odd_numb()


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.

# The term "args" is short for "arguments" and refers to non-keyword arguments that are passed to a function. These arguments are stored in a tuple and can be accessed using index notation within the function.
# The term "*kwargs" stands for "keyword arguments" and refers to named arguments that are passed to a function. These arguments are stored in a dictionary and can be accessed using their key names within the function.

# In[ ]:


def simple_args_example(*args):
    for i in mateen:
        print(i)


# In[ ]:


simple_args_example(1,2,3,4,5,6,7)


# In[10]:


def display_info(name,age,**kwargs):
    print(f"name of employe is:{name}")
    print(f"age of employe is:{age}")
    for key,value in kwargs.items():
        print(f"{key.capitalize()}:{value}")
        
display_info("abdul",22,city = "bijapur",occupation ="engineer")


# ## Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].

# # In Python, an iterator is an object that enables you to traverse a container, such as a list or a dictionary, and access its individual elements one at a time. Iterators are implemented using the iterator protocol, which requires that an object has a __iter__ method that returns the iterator object itself and a __next__ method that returns the next value in the sequence.

# # The method used to initialize the iterator object is __iter__, and the method used to retrieve the next value in the sequence is __next__.
# 
# # The __iter__ method should return the iterator object itself, typically self, while the __next__ method should return the next item in the sequence, or raise the StopIteration exception if there are no more items left to iterate over.

# In[1]:


l=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
l1=iter(l)
for i in range(5): 
    print(next(l1))


# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
# function.

# In Python, a generator function is a type of function that returns an iterator object which can be used to iterate over a sequence of values. The difference between a generator function and a regular function is that a generator function uses the yield keyword instead of the return keyword to produce a series of values one at a time.
# When a generator function is called, it does not actually execute any code, but instead creates a generator object that can be used to control the execution of the function. Each time the yield keyword is encountered in the function, the current value is returned and the function is suspended. The next time the generator object is called, execution resumes from the point where it was suspended and continues until the next yield statement is encountered.

# In[25]:


def countdown(n):
    while n >=0:
        yield (n)
        n -=1


# In[26]:


for i in countdown(5):
    print(i)


# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.

# In[5]:


def isprime(num):
    l1 =[]
    for i in range(0,1000):
        if i % 2 !=0:
            l1.append(i)
            i +=1
    return l1


# In[6]:


l1


# In[35]:


def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
    
def primegenerator(n):
    num =2
    while n:
        if isprime(num):
            yield num
            n-=1
        num+=1
    return


# In[1]:


it =primegenerator(10)
for e in it:
    print(e,end='')


# Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

# In[8]:


def create_fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(n-2):
        c =a+b
        a = b
        b = c
        print(c)
print(create_fibonacci(10))


# In[ ]:


a= 0
b= 1
count =0
while count <=10:
    print(a)
    c =a+b
    a =b
    b =c
    count +=1
  
    


# Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[ ]:


string ='pwskills'
character =[char for char in string]
print(character)


# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

# In[ ]:


def checking_palindrom(word):
    reversed_word =word[::-1]
    if reversed_word ==word:
        print(f"{word} is palindrom")
    return (f"{word} is not palindrome")

    


# In[ ]:


checking_palindrom("icici")
checking_palindrom("aman")


# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.

# In[ ]:


odd_numbers =[num for num in range(0,100) if num % 2 !=0 ] 
print(odd_numbers)


# In[ ]:




