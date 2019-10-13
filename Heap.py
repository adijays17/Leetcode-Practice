#!/usr/bin/env python
# coding: utf-8

# Write a program that takes as input a set of sorted sequences and computes the union of these
# sequences as a sorted sequence. For example, if the input is (3,5,7), (0,5), and (0,6,28), then the
# output is (0, 0, 3, 5, 6, 6,7, 28).
# 
# Merge Sorted Files

# In[9]:


import heapq 

def merge_sorted_array(x):
    if (len(x)<2):
        return x[0]
    l = []
    heapq.heapify(l)
    for e in x:
        l = list(heapq.merge(l, e))
    return l

x = [[0,0,4,6,7], [9,10,90,900], [1,4,7,9]]
print(merge_sorted_array(x))


# Sort increasing decreasing Array

# In[10]:


def sort_increasing_decreasing_array(l):
    if len(l)<2:
        return sorted(l)
    else:
        master_list = []
        prev = l[0]
        flag = 'i'
        
        prev_flag = 'i'
        sub_list = []
        sub_list.append(prev)
        for e in l[1:]:
            if e < prev:
                flag = 'd'
            else:
                flag = 'i'

            if prev_flag != flag:
                prev_flag = flag
                if flag == 'i':
                    sub_list = sub_list[::-1]
                master_list.append(sub_list)
                sub_list = []
                sub_list.append(e)
            else:
                sub_list.append(e)
            prev = e
        if flag == 'd':
            master_list.append(sub_list[::-1])
        else:
            master_list.append(sub_list)
    return master_list


# In[11]:


l = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
merge_sorted_array(sort_increasing_decreasing_array(l))


# In[12]:


l = [180, 130, 120, 110, 160, 170, 100, 80, 70]
merge_sorted_array(sort_increasing_decreasing_array(l))


# In[13]:


l = [40]
merge_sorted_array(sort_increasing_decreasing_array(l))


# You want to compute the running median of a sequence of numbers. The sequence is presented to
# you in a streaming fashion-you carmot back up to read an earlier value, and you need to output
# the median after reading in each new element. For example, if the input is 1,0,3,5,2,0,1 the output
# is 1, 0.5, 1, 2, 2, 1.5, 1.
# 
# Design an algorithm for computing the running median of a sequence.

# In[14]:


def find_running_median(y):
    min_heap = []
    max_heap = []
    result = []

    for e in y:
        heapq.heappush (max_heap , -heapq.heappushpop(min_heap , e))
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if (len(max_heap) == len(min_heap)):
            result.append((-max_heap[0]+min_heap[0])/2)
        else:
            result.append(min_heap[0])
    return result
  
y = [1,0,3,5,2,0,1]
find_running_median(y)


# Compute the K closet Stars

# In[15]:


import math 

def compute_k_closet_stars(points, K):
    l = []
    for e in points:
        heapq.heappush(l , (math.sqrt(e[0]**2 + e[1]**2 + e[2]**2),e))
    return [x[1] for x in heapq.nsmallest(K, l)]

print(compute_k_closet_stars([[1,1,1], [4,4,4], [2,2,2], [6,6,6], [3,3,3], [5,5,5]],3))


# Compute the K largest elements in the Max Heap

# In[18]:


li = [3,34,123,2123,12,12343,213454,4321,5432,65432345,4231,321234]

def k_largest(li, k):
    heapq.heapify(li) 
    return heapq.nlargest(k, li)


# In[19]:


k_largest(li, 4)


# In[ ]:




