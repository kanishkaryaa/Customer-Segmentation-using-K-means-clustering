#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


# In[2]:


# loading the data from a csv file to a Pandas dataframe

customer_data = pd.read_csv('Mall_Customers.csv')


# In[3]:


customer_data.head()


# In[4]:


# finding the number of rows and columns
customer_data.shape


# In[5]:


# getting the information about the dataset
customer_data.info()


# In[6]:


# checking for missing values
customer_data.isnull().sum()


# In[7]:


X = customer_data.iloc[:, [3,4]].values


# In[8]:


print(X)


# In[13]:


# finding wcss value for different number of clusters
wcss = []
   
for i in range(1, 11):
   kmeans = KMeans(n_clusters=i, init='k-means++',random_state=42)
   kmeans.fit(X)
   wcss.append(kmeans.inertia_)


# In[14]:


sns.set()
plt.plot(range(1,11),wcss)
plt.title('The Elbow Point Graph')
plt.xlabel('Number of Clusters')
plt.ylabel("WCSS")
plt.show()


# In[20]:


# Training the k-means clustering model

# Optimum number of clusters

kmeans = KMeans(n_clusters=5, init='k-means++',random_state=0)

# return a label for each data point based on their cluster
Y  = kmeans.fit_predict(X)
print(Y)


# In[30]:


# plotting all the clusters and their centroids

plt.figure(figsize=(8,8))
plt.scatter(X[Y==0,0],X[Y==0,1], s=50, c='green', label = 'Cluster 1')
plt.scatter(X[Y==1,0],X[Y==1,1], s=50, c='red', label = 'Cluster 2')
plt.scatter(X[Y==2,0],X[Y==2,1], s=50, c='yellow', label = 'Cluster 3')
plt.scatter(X[Y==3,0],X[Y==3,1], s=50, c='violet', label = 'Cluster 4')
plt.scatter(X[Y==4,0],X[Y==4,1], s=50, c='blue', label = 'Cluster 5')

#plot the centroids
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c='cyan', label='Centroids')

plt.title("Customer Groups")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()


# In[ ]:




