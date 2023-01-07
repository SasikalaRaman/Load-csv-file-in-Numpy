#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np #N-dimensional array package
import matplotlib.pyplot as plt #data visualization


# In[16]:


arr=np.loadtxt("gdp_growth.csv", delimiter=',',usecols=np.arange(0,66) ,unpack=True,dtype= str) #load the csv file in Numpy library


# In[17]:


display(arr) #diplay the dataset in csv


# In[18]:


x=arr[:,0]# irrtate the value from 0th row
print(x)


# In[19]:


x=x[4:66] # it show the value from 4 to 66in axis=1 in 0throw axis=0
print(x) # print the x value


# In[20]:


y=[1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,171,18,19,20,21,22,23,24,25,26,272,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]


# In[21]:


print(y) # print the y value


# In[22]:



plt.xlabel("x-axis")# Specify X axis label
plt.ylabel("y-axis")# Specify Y axis labels
plt.plot(x,y)# Plot points on graph paper
plt.show()# Show the plot


# In[ ]:




