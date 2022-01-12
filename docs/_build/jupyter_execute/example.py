#!/usr/bin/env python
# coding: utf-8

# # Example usage
# 
# To use `pycounts` in a project:

# In[1]:


import pycounts

print(pycounts.__version__)


# # Imports

# In[2]:


from pycounts.pycounts import count_words
from pycounts.plotting import plot_words


# # Create a text file

# In[3]:


quote = """Insanity is doing the same thing over and over and              expecting different results."""
with open ("einstein.txt", "w") as file:
    file.write(quote)


# # Count Words
# 
# We can count the words in our text file using the `count_words()` function. Note that this removes punctuation and makes all words lower case before counting.

# In[4]:


counts = count_words("einstein.txt")
print(counts)


# # Plot Words
# 
# We can now plot the results using the `plot_words()` function:

# In[5]:


fig = plot_words(counts, n = 5)


# In[ ]:




