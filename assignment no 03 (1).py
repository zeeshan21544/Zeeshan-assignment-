#!/usr/bin/env python
# coding: utf-8

# In[31]:


val1 = input('enter first value')
val2 = input('enter second value')
operator = input('enter operator')
val1= int(val1)
val2 = int(val2)

if operator == '+':
    val = val1 + val2 
    print(val,'answer')
elif  operator == '-':
    val = val1 - val2 
    print(val,'answer')
elif  operator == '*':
    val = val1 * val2 
    print(val,'answer')
elif  operator == '/':
    val = val1 / val2 
    print(val,'answer') 
elif  operator == '^':
    val = val1 ^ val2 
    print(val,'answer')
else:
        print('enter correct operator')


# 

# In[48]:


test_list = [ 1, 6, 3, 5, 3, 4 ] 
  
print("Checking if 4 exists in list ( using loop ) : ") 
  
# Checking if 4 exists in list  
# using loop 
for i in test_list: 
    if(i == 4) : 
        print ("Element Exists") 
  
print("Checking if 4 exists in list ( using in ) : ") 
  
 # Checking if 4 exists in list  
 # using in 
if (4 in test_list): 
    print ("Element Exists") 
    


# In[49]:


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# In[50]:


my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


# In[ ]:


def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
# Driver Code 
duplicate = [2, 4, 10, 20, 5, 2, 20, 4] 
print(Remove(duplicate))


# In[52]:


d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)


# In[53]:





# In[ ]:




