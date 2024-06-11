#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Creating random vector of size 15 having only Integers in the range 1-20. 

import numpy as np
v=np.random.randint(1,20, (15,))

#Reshaping the array to 3 by 5

arr = v.reshape (3,5)
print(arr.shape)
print(arr)

#Replacing the max in each row by 0
row_max = arr.max(axis=1).reshape(-1,1) 
arr= np.where(arr== row_max, 0, arr)
print('\n', arr)


# In[11]:


#Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the shape, type and data type of the array

x= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], np.int32)
print('Shape:', x.shape)
print('Type:', type(x))
print('Data type:',x.dtype)


# In[14]:


# Computing the eigenvalues and right eigenvectors

from numpy import linalg as LA
mat = np.array([[3, -2], [1, 0]], np.int32)
w, v = LA.eig(mat)
print('Eigenvalues:', w)
print('\nRight eigenvectors:\n', v)


# In[15]:


# Computing the sum of the diagonal element

n = np.array([[0, 1, 2], [3, 4, 5]])
res = np.trace(n)
print('Sum of diagonal elements:', res)


# In[16]:


#program to create a new shape to an array without changing its data
m = np.arange(1,7).reshape(3,2)
m = m.reshape(2,3)
m

