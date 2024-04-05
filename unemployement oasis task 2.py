#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


data=pd.read_csv(r"D:\oasis infobyte\Unemployment in India.csv")
data


# In[3]:


data.info()


# In[4]:


data.describe()


# In[5]:


data.isnull().sum()


# In[6]:


data.columns=['States', 'Date', 'Frequency', 'Estimated Unemployement Rate', 'Estimated Employed','Estimated Labour Participation Rate', 'Region']


# In[7]:


data.head()


# In[8]:


plt.title('Indian Unemployement')
sns.histplot(x='Estimated Employed', hue='Region', data=data)
plt.show()


# In[10]:


plt.figure(figsize=(10,8))
plt.title('Indian Unemployement')
sns.histplot(x='Estimated Employed', hue='Region', data=data)
plt.show()

