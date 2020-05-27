#!/usr/bin/env python
# coding: utf-8

# In[64]:


import csv
import random
from math import sqrt
from matplotlib import pyplot as plt
import numpy as np


# In[65]:


data = []
#Read data and convert it into array
final_data = [[]]
with open('data clustering.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        data.append(row)

csv_file.close
labels = data.pop(0)
for row in data:
    arr = []
    for i in row:
        arr.append(int(i))
    final_data.append(arr)
final_data.pop(0)
print(final_data)

#plot data
for i in final_data:
    plt.scatter(i[0], i[1], c = 'green')
plt.show()


# In[66]:


#Search minimum value in data
kecil = final_data[0][1]
for no in final_data:
    for x in no:
        if x < kecil:
            kecil = x

print(kecil)

#Search maximum value in data
besar = final_data[0][1]
for no in final_data:
    for x in no:
        if x > besar:
            besar = x
print(besar)


# In[67]:


#determine number of cluster or k object
centroid = [[]]
k = 3
#generate centroid as much as number of cluster or k object
for i in range(k):
    array = [] 
    #generate random number for centroid
    x = random.randint(kecil,besar)
    y = random.randint(kecil,besar)
    #input array k objects
    array.append(x)
    array.append(y)
    centroid.append(array)

centroid.pop(0)
print(centroid)

#Visualize data with initial centroid
plt.scatter(centroid[0][0],centroid[0][1], c = 'blue')
plt.scatter(centroid[1][0],centroid[1][1], c = 'magenta')
plt.scatter(centroid[2][0],centroid[2][1], c = 'orange')
for i in final_data:
    plt.scatter(i[0], i[1], c = 'green')


# In[68]:


#clustering data into their cluster
def clustering(centroid,cluster,final_data):
    obj = 0
    for n in range(len(final_data)):
        #determine initial closest distance
        closest = sqrt( (final_data[n][0]-centroid[0][0])**2 + (final_data[n][1]-centroid[0][1])**2 )
        obj = 1
        for i in range(len(centroid)):
            #calculate distance between data and centroid using euclidean distance
            distance = sqrt( (final_data[n][0]-centroid[i][0])**2 + (final_data[n][1]-centroid[i][1])**2 )
            #finding the closest distance 
            if distance <= closest:
                closest = distance
                obj = i+1
        cluster.append(obj)
    print(cluster)


# In[69]:


#optimalisasi centroid
def center(centroid,cluster,newcentroid,final_data):
    #newcentroid = []
    for i in range(len(centroid)):
        x = 0
        y = 0
        jum = 0
        array = []
        for n in range(len(final_data)):
            if cluster[n] == i+1:
                x = x + final_data[n][0]
                y = y + final_data[n][1]
                jum = jum + 1
        #determine new centroid 
        if jum != 0:
            x = x/jum
            y = y/jum
            array.append(x)
            array.append(y)
            newcentroid.append(array)
        else: 
            array.append(centroid[i][0])
            array.append(centroid[i][1])
            newcentroid.append(array)
    newcentroid.pop(0)
    newcentroid = np.ceil(newcentroid)
    newcentroid = np.array(newcentroid).tolist()
    print(newcentroid)

   # plt.scatter(newcentroid[0][0],newcentroid[0][1], c = 'cyan')
   # plt.scatter(newcentroid[1][0],newcentroid[1][1], c = 'red')
   # plt.scatter(newcentroid[2][0],newcentroid[2][1], c = 'violet')
   # plt.scatter(centroid[0][0],centroid[0][1], c = 'blue')
   # plt.scatter(centroid[1][0],centroid[1][1], c = 'pink')
   # plt.scatter(centroid[2][0],centroid[2][1], c = 'purple')
   # for i in range(len(final_data)):
    #    if cluster[i] == 1:
     #       plt.scatter(final_data[i][0],final_data[i][1], c = 'blue')
      #  if cluster[i] == 2:
       #     plt.scatter(final_data[i][0],final_data[i][1], c = 'pink')
        #if cluster[i] == 3:
         #   plt.scatter(final_data[i][0],final_data[i][1], c = 'purple')
    #plt.show


# In[70]:


#Main programe
newcentroid = [[]]
cluster = []
#final_data = [[]]
# clustering(centroid,cluster,final_data)
# center(centroid,cluster,newcentroid,final_data)
itr = 0
shift = True
while shift:
    #centroid = newcentroid.copy()
    cluster = []
    newcentroid = [[]]
    clustering(centroid,cluster,final_data)
    center(centroid,cluster,newcentroid,final_data)
    itr = itr+1
    if centroid == newcentroid:
        shift = False
    else:
        centroid = newcentroid.copy()
#print(centroid)
print('jumlah iterasi hingga mendapat centorid yang optimal: ', itr)
#print(itr)
for i in range(3):
    print("Data yang termasuk kedalam cluster ",i+1, ":")
    for n in range(len(cluster)):
        if (cluster[n] == i+1):
            print(n+1)
            
#Visualize clustered data
for i in range(len(cluster)):
    if cluster[i] == 1:
        plt.scatter(final_data[i][0],final_data[i][1], c = 'blue')
    if cluster[i] == 2:
        plt.scatter(final_data[i][0],final_data[i][1], c = 'magenta')
    if cluster[i] == 3:
        plt.scatter(final_data[i][0],final_data[i][1], c = 'orange')

#Visualize centroid
for i in range(len(centroid)):
    plt.scatter(centroid[i][0],centroid[i][1], marker='*', s=150, c='red')

plt.title('Clusters Non-Library K=3')
plt.xlabel('X')
plt.ylabel('Y')
plt.show


# In[ ]:




