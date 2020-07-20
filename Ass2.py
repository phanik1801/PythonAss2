#!/usr/bin/env python
# coding: utf-8

# In[5]:


num=float(input("Enter num: "))
if num>0:
    print("number is positive")
elif num==0:
    print("number is Zero")
else:
    print("number is negative")


# In[17]:


num=float(input("Enter num: "))
if (num%2)==0:
    print("Number is Even")
else:
    print("Number is Odd")


# In[19]:


year=int(input("Enter the year: "))
if(year%4)==0:
    if(year%100)==0:
        if(year%400)==0:
            print(year,"is a Leap Year")
        else:
            print(year,"is not Leap Year")
    else:
        print(year,"is a Leap Year")
else:
    print(year,"is not Leap Year")


# In[21]:


a=float(input('Enter first number= '))
b=float(input('Enter second number= '))
c=float(input('Enter third number= '))
if(a>b)and(a>c):
    largest=a
elif(b>a)and(b>c):
    largest=b
else:
    largest=c
print('Largest number is',largest)


# In[26]:


num = int(input("Enter a number: "))
product=1
if (num<0):
    print("Factorial for number less than 0 is not possible")
elif(num==0):
    print("Factorial of Zero is 1")
else:
    for i in range(num):
        product=product*(i+1)
    print("Factorial of num:",product)


# 
