#!/usr/bin/env python
# coding: utf-8

# # Headlines Group Project:
# ### Team: 
# Evangeline Johnson </br> Ajibola Adeyemo </br> Sivamma Mettu </br> Adobea Essien

# In[59]:


import pandas as pd
import numpy as np
from numpy import nan


# In[60]:


apps=pd.read_csv("playstore_apps.csv",index_col='App')


# In[61]:


reviews=pd.read_csv("playstore_reviews.csv",index_col='App')


# In[62]:


reviews2=pd.read_csv("reviews2.csv",index_col='App')
reviews2


# In[63]:


apps.head()


# In[64]:


reviews.head()


# ## Focusing on the data on Playstore Apps. 
# ### Removing Duplicates & Taking a look at the formatting.

# In[65]:


apps.drop_duplicates(keep='first',inplace=True)
apps.head()


# In[66]:


apps.info()


# In[67]:


# category column

apps['Category'].unique()


# In[68]:


apps[apps['Category']=='1.9']


# In[69]:


apps.drop('Life Made WI-Fi Touchscreen Photo Frame',inplace=True)


# In[70]:


apps['Category'].unique()


# In[71]:


apps['Size'].unique()


# In[75]:


apps['Type'].unique()


# In[76]:


apps['Content Rating'].unique()


# In[77]:


apps['Genres'].unique()


# In[78]:


apps['Last Updated'].unique()


# ## Updating Column 'Last Updated' to Date format:

# In[ ]:


apps['Last Updated'] = pd.to_datetime(apps['Last Updated'])


# In[80]:


apps.info()


# In[81]:


apps['Current Ver'].unique()


# In[82]:


apps['Android Ver'].unique()


# In[83]:


apps.rename(columns={'Android Ver' : 'Android_Version', 'Current Ver' : 'Current_Version'}, inplace=True)


# In[84]:


apps.head()


# In[85]:


# apps.to_csv('cleaned_apps.csv')


# # Reviews Table

# In[97]:


reviews2.drop_duplicates(keep=False,inplace=True)


# In[96]:


reviews2.tail()


# In[88]:


reviews2.info()


# In[89]:


reviews2['Translated_Reviews'].unique()


# In[90]:


reviews2['Sentiment'].unique()


# In[91]:


reviews2['Sentiment_Polarity'].unique()


# In[92]:


reviews2['Sentiment_Subjectivity'].unique()


# In[94]:


reviews2.to_csv('cleaned_reviews2.csv')

