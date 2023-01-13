#!/usr/bin/env python
# coding: utf-8

# # Headlines Group Project:
# ### Team: 
# Evangeline Johnson </br> Ajibola Adeyemo </br> Sivamma Mettu </br> Adobea Essien

# In[38]:


import pandas as pd
import numpy as np
from numpy import nan


# In[41]:


apps=pd.read_csv("playstore_apps.csv",index_col='App')


# In[3]:


reviews=pd.read_csv("playstore_reviews.csv",index_col='App')


# In[4]:


reviews2=pd.read_csv("reviews2.csv",index_col='App')
reviews2


# In[5]:


apps.head()


# In[6]:


reviews.head()


# ## Focusing on the data on Playstore Apps. 
# ### Removing Duplicates & Taking a look at the formatting.

# In[7]:


apps.drop_duplicates(keep='first',inplace=True)
apps.head()


# In[8]:


apps.info()


# In[9]:


# category column

apps['Category'].unique()


# In[10]:


apps[apps['Category']=='1.9']


# In[11]:


apps.drop('Life Made WI-Fi Touchscreen Photo Frame',inplace=True)


# In[12]:


apps['Category'].unique()


# In[13]:


apps['Size'].unique()


# In[14]:


apps['Type'].unique()


# In[15]:


apps['Content Rating'].unique()


# In[16]:


apps['Genres'].unique()


# In[17]:


apps['Last Updated'].unique()


# ## Updating Column 'Last Updated' to Date format:

# In[ ]:


apps['Last Updated'] = pd.to_datetime(apps['Last Updated'])


# In[19]:


apps.info()


# In[20]:


apps['Current Ver'].unique()


# In[21]:


apps['Android Ver'].unique()


# In[33]:


apps.rename(columns={'Android Ver' : 'Android_Version', 'Current Ver' : 'Current_Version', 'Content Rating' : 'Content_Rating', 'Last Updated' : 'Last_Updated'}, inplace=True)


# In[35]:


apps.dropna()


# In[36]:


apps.to_csv('cleaned_apps.csv')


# # Reviews Table

# In[25]:


reviews2.drop_duplicates(keep=False,inplace=True)


# In[26]:


reviews2.tail()


# In[27]:


reviews2.info()


# In[28]:


reviews2['Translated_Reviews'].unique()


# In[29]:


reviews2['Sentiment'].unique()


# In[30]:


reviews2['Sentiment_Polarity'].unique()


# In[31]:


reviews2['Sentiment_Subjectivity'].unique()


# In[32]:


reviews2.to_csv('cleaned_reviews2.csv')

