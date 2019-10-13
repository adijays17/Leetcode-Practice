#!/usr/bin/env python
# coding: utf-8

# <h1> Tower of Hanoi </h1>

# In[119]:


def tower_of_hanoi(number_of_blocks, From, Spare, To):
    if number_of_blocks==1:
        print("Move block ",number_of_blocks," from ", From, " to ", To)
        return 
    tower_of_hanoi(number_of_blocks-1, From, To, Spare)
    print("Move block ", number_of_blocks," from ", From, " to ", To)
    tower_of_hanoi(number_of_blocks-1, Spare, From, To) 


# In[132]:


tower_of_hanoi(3, "A", "B", "C")


# <h1> N Queens Problem </h1>

# In[ ]:





# In[ ]:





# <h1>Permutations</h1>

# In[1]:


def permute(nums):
    def swap (arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    def permutations(nums, start, results):
        if start >= len(nums):
            results.append(nums.copy())
        else:
            for i in range(start, len(nums)):
                swap(nums, start, i)
                permutations(nums, start+1, results)
                swap(nums, start, i) #This is backtracking   
    results = []
    permutations(nums, 0, results)
    return results


# In[2]:


permute([1, 2, 3])


# <h1>Power set</h1>

# In[3]:


def power_set(input_set):
    results = []
    subset = []
    def find_all_subsets(input_set, start_index, subset):
        results.append(subset.copy())
        for i in range(start_index, len(input_set)):
            subset.append(input_set[i])
            start_index += 1
            find_all_subsets(input_set, start_index, subset)
            del subset[-1]    #This is backtracking step
    find_all_subsets(input_set, 0, subset)
    return results
    


# In[4]:


power_set([2, 1, 0])


# In[5]:


power_set([1, 3, 2])


# <h1>Power set for K</h1>

# In[8]:


def power_set_k(input_set, k):
    results = []
    if len(input_set) < 1:
        return 
    subset = []
    
    def find_all_subsets(results, input_set, start_index, subset):
        if len(subset) == k:
            results.append(subset.copy())
        for i in range(start_index, len(input_set)):
            subset.append(input_set[i])
            if len(subset) > k:
                del subset[-1] #This is backtracking
                return
            start_index += 1
            find_all_subsets(results, input_set, start_index, subset)
            del subset[-1] #This is backtracking
            
    find_all_subsets(results, input_set, 0, subset)
    return results


# In[9]:


power_set_k([0, 1, 2, 3, 4], 2)


# <h1>Generate strings of matched parens</h1>

# In[1]:


def genrate_matched_parens(n):
    results = []
    def generate_brackets(left, right, bracket):
        #print(left, right)
        if left == 0 and right == 0:
            results.append(bracket)
            return 
        if left == right:
            bracket += '('
            generate_brackets(left-1, right, bracket)
        elif left > 0 and left < right:
            bracket += '('
            generate_brackets(left-1, right, bracket)
            bracket = bracket[:-1]               #This is backtracking
            bracket += ')'
            generate_brackets(left, right-1, bracket)
        elif left == 0 and right > 0:
            bracket += ')'
            generate_brackets(left, right-1, bracket)
    generate_brackets(n, n,"")
    return results        


# In[2]:


genrate_matched_parens(3)


# <h1>Generate palindromic decomposition</h1>

# In[3]:


def generate_palindomic_decompostion(s):
    result = []
    def is_palindrome(s):
        if s == s[::-1]:
            return True
        return False
    
    def perform_recursion(st, start, decompose):
        if start == len(s):
            result.append(decompose)
        else:
            for i in range(start, len(st)):
                if is_palindrome(st):
                    decompose.append(st)
                    
            

    perform_recursion(s, 0, [])
    return result


# In[4]:


generate_palindomic_decompostion('aba')


# In[21]:


s = "abc"
i = 0
s[i:len(s)]


# In[ ]:




