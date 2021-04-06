#!/usr/bin/env python
# coding: utf-8

# # Indian Tourism Exploratory analysis

# ## Introduction

# In[ ]:


Tourism is the largest service industry in india.Tourism in india is important for the country's economy and is growing rapidly.
India provides the facility to tourists of international origin to understand and experience cultural diversity of the country.
India is a land of beautiful hill stations,parks,temples etc.Here we have done the analysis on the tourism in india.


# ## Import Libraries

# In[5]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# ### Load the data set

# In[4]:


df=pd.read_csv('E:/tourism.csv')
df


# ### to check the dimension

# In[4]:


df.ndim


# ###  to check how many rows and columns

# In[126]:


df.shape


# ### to print fields name

# In[128]:


df.columns


# ### to check the data type of attributes

# In[61]:


df.dtypes


# ### to check the index

# In[60]:


df.index


# ### to view the top 5 records

# In[5]:


df.head(5)


# ### to view the last 5 records

# In[125]:


df.tail(5)


# ### to view any 5 random records

# In[6]:


df.sample(5)


# ### to  print the region as index

# In[93]:


df.set_index(['Region']) 


# ### to check the information

# In[70]:


df.info()


# ### describing the data set

# In[9]:


df.describe()


# ### Descriptive statistics

# In[71]:


df.describe(include='all')


# ### to detect any missing values in the dataset 

# In[72]:



df.isna().sum()


# ## query to extract data from given dataframe

# ### query for extracting the records of places in east

# In[111]:



east_places=df.loc[df['Region']=='East']
east_places


# ### query for extracting the record of places in west region

# In[10]:


west_places=df.loc[df['Region']=='West']
west_places


# ### query for extracting the record of places in North West region

# In[78]:


NW_place=df.loc[df['Region']=='North West']
NW_place


# ### query for extracting the record of places in north east region

# In[80]:


NE_df=df.loc[df['Region']=='North East']
NE_df


# ### query for extracting the record of places in north region

# In[81]:



North_df=df.loc[df['Region']=='North']
North_df


# ### query for extracting the record of places in south region

# In[50]:



south_df=df.loc[df['Region']=='South']
south_df


# ### query for extracting the record of places in south east region

# In[110]:


se_df=df.loc[df['Region']=='South East']
se_df


# ### query for extracting the record of places in south west region

# In[82]:



sw_df=df.loc[df['Region']=='South West']
sw_df


# ### query for extracting the record of hill station in india

# In[114]:



hill_station =df.loc[df['Type']=='Hill Station']
hill_station


# ### query for extracting the record of Zoological Park in india

# In[115]:



zoo_park=df.loc[df['Type']=='Zoological Park']
zoo_park


# ### query for extracting the record of  temple in india

# In[85]:



temple=df.loc[df['Type']=='Temple']
temple


# ### query for extracting the record of  beach in india

# In[86]:


##query for extracting the record of  beach in india###
beach=df.loc[df['Type']=='Beach']
beach


# ### query to extract the record of places whose rating is greater than 9

# In[87]:



df[df['rating'] >9] 


# ### query to extract the record of places whose rating is less than 8

# In[88]:



df[df['rating']<8]


# ### query to extract the record of places whose airport distance is less than or equal to 30 km

# In[89]:



df[df['airport_dist(km)']<=30]


# ### query to extract the record of places whose railway distance is less than or equal to 5 km

# In[90]:



df[df['railway_dist(km)']<=5]


# ### query for extracting the record of places having elevation is 5 m

# In[91]:



elv=df.loc[df['Elevation(m)']==5.0]
elv


# ### query for extracting the record of places having elevation greater than 2000 m.

# In[92]:



elv1=df.loc[df['Elevation(m)']>2000]
elv1


# ### query to extract the unique values from the data set

# ### unique values from name

# In[99]:


unq_name=df.Name.unique()
unq_name


# ### unique values from type

# In[100]:


unq_typ=df.Type.unique()
unq_typ


# ### unique values from region

# In[102]:


unq_Region=df.Region.unique()
unq_Region


# ### unique values from rating

# In[119]:


unq_ratng=df.rating.unique()
unq_ratng


# ## Descriptive statistics

# ### to calculate the mean,median,maximum,minimum,variance,standard deviation of the airport distance(km) from the data set
# 

# In[19]:


air_mean=df['airport_dist(km)'].mean()
air_mean


# In[12]:


air_median=df['airport_dist(km)'].median()
air_median


# In[13]:


air_maxm=df['airport_dist(km)'].max()
air_maxm


# In[14]:


air_minm=df['airport_dist(km)'].min()
air_minm


# In[16]:


air_variance=df['airport_dist(km)'].var()
air_variance


# In[35]:


air_sd=df['airport_dist(km)'].std()
air_sd


# In[ ]:





# ### to calculate the mean,median,maximum,minimum,variance,standard deviation of the railway distance(km) from the data set

# In[18]:


rail_mean=df['railway_dist(km)'].mean()
rail_mean


# In[20]:


rail_median=df['railway_dist(km)'].median()
rail_median


# In[21]:


rail_max=df['railway_dist(km)'].max()
rail_max


# In[22]:


rail_min=df['railway_dist(km)'].min()
rail_min


# In[23]:


rail_variance=df['railway_dist(km)'].var()
rail_variance


# In[24]:


rail_SD=df['railway_dist(km)'].std()
rail_SD


# In[ ]:





# ### to calculate the mean,median,maximum,minimum,variance,standard deviation of the Elevation(m) from the data set

# In[25]:


elv_mean=df['Elevation(m)'].mean()
elv_mean


# In[30]:


elv_median=df['Elevation(m)'].median()
elv_median


# In[29]:


elv_max=df['Elevation(m)'].max()
elv_max


# In[28]:


elv_min=df['Elevation(m)'].min()
elv_min


# In[27]:


elv_variance=df['Elevation(m)'].var()
elv_variance


# In[26]:


elv_SD=df['Elevation(m)'].std()
elv_SD


# ### to calculate the mean,median,maximum,minimum,variance,standard deviation of the Rating from the data set

# In[12]:


ra_mean=df['rating'].mean()
ra_mean


# In[13]:


ra_median=df['rating'].median()
ra_median


# In[14]:


ra_max=df['rating'].max()
ra_max


# In[15]:


ra_min=df['rating'].min()
ra_min


# In[16]:


ra_variance=df['rating'].var()
ra_variance


# In[17]:


ra_sd=df['rating'].std()
ra_sd


# In[ ]:





# ## VISUALIZATION

# # plotting the graph

# In[124]:


style.use('ggplot')
bins=[7,7.5,8,8.5,9,9.5,10]
plt.hist(df['rating'],bins,histtype='bar',color='m',rwidth=.6)
plt.xlabel('range')
plt.ylabel('RATINGS')
plt.title('INDIAN TOURISM')
plt.show()


# In[57]:


plt.figure(figsize=(10,12))
sns.barplot(x='rating',
            y='Name',
            data=df)
plt.xlabel('RATING')
plt.ylabel('TOURIST PLACES')
plt.title("TOURISM RATING IN INDIA")
plt.show()


# In[16]:



plt.style.use('seaborn-darkgrid')
x=df['Name']
y=df['airport_dist(km)']
y1=df['railway_dist(km)']

plt.figure(figsize=(10,12))
plt.barh(x,y,label='airport_dist(km)',color='g')
plt.barh(x,y1,label='railway_dist(km)',left=y,color='y')

plt.xlabel('Name of places')
plt.ylabel('distance')
plt.title(' INFORMATION ABOUT TRANSPORTATION')
plt.legend()
plt.show()


# ## Conclusion

# In[ ]:


We have done exploratory analysis on the tourism of india.Analysed and queried to extract the record of places have highest 
rating and lowest rating in india.From Visualization , it is clear that Radhanagar Beach has the highest rating among the tourist 
places in  india.Kufri has the lowest rating based on the analysis .


# ## Reference

# In[ ]:


1. www.kaggle.com

2. https://encyclopedia.com 

