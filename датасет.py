#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[6]:


game = pd.read_csv("C:\\Users\\user\\Documents\\датасет\\vgsales.csv")


# In[7]:


game.head()


# In[8]:


#Посмотрел топ датасета


# In[9]:


game.tail()


# In[ ]:


#Посмотрел конец датасета


# In[27]:


game[game.Platform=="PC"]


# In[ ]:


#Игрушки на ПК


# In[11]:


game[game.Publisher=="Activision"]


# In[ ]:


#Игрульки активижн


# In[12]:


game.Global_Sales.sum()


# In[ ]:


#Деняк взрослых детей потрачено


# In[14]:


game.NA_Sales.sum()


# In[15]:


game.EU_Sales.sum()


# In[16]:


game.JP_Sales.sum()


# In[17]:


game.Other_Sales.sum()


# In[ ]:


#Китайцы поработят мир и игрульки!!!


# In[28]:


game.describe().round(2)


# In[ ]:


#срезовые значения


# In[30]:


game["Platform"].value_counts()


# In[ ]:


#кол-во игр по платформам


# In[33]:


game.groupby('Year')['Name'].count()


# In[ ]:


#сколько вышло по годам


# In[42]:


data = game.query("2012 <= Year <= 2016")
data.pivot_table(index='Year', columns = 'Platform', values='Global_Sales', aggfunc='sum').plot(grid=True, figsize=(15, 7))



# In[ ]:


#грфафик общих продаж игр на разных платформах


# In[43]:


game.groupby(['Platform'])['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'].sum()


# In[ ]:


#Продажи по платформам


# In[45]:


game.pivot_table(index='Genre', values='Global_Sales', aggfunc='median').plot(grid=True, figsize=(12, 5))


# In[ ]:


#популярность жанров за все время


# In[ ]:


#Я устал. 

