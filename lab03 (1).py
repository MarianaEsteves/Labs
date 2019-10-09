#!/usr/bin/env python
# coding: utf-8

# # Lab 3
# In the following cell cell you have several list. 

# In[7]:


#list of 007 movies where Sean Connery features James Bond
moviesSeanConnery = ["Dr. No (1962)",
"From Russia with Love (1963)",
"Goldfinger (1964)",
"Thunderball (1965)",
"You Only Live Twice (1967)",
"Diamonds Are Forever (1971)",    
"Never Say Never Again (1983)"]  

#list of 007 movies where David Neven features James Bond
moviesDavidNeven=["Casino Royale (1967)"]    

#list of 007 movies where George Lazenby features James Bond
moviesGeorgeLazenby=["On Her Majesty's Secret Service (1969)"]  
          
#list of 007 movies where Roger Moore features James Bond   
moviesRogerMoore=[ "Live and Let Die (1973)",
"The Man with the Golden Gun (1974)",
"The Spy Who Loved Me (1977)",
"Moonraker (1979)",
"For Your Eyes Only (1981)",
"Octopussy (1983)",
"A View to a Kill (1985)"]

#list of 007 movies where Timothy Dalton features James Bond  
moviesTimothyDalton=[
"The Living Daylights (1987)",
"Licence to Kill (1989)"  
]

#list of 007 movies where Pierce Brosnan features James Bond  
moviesPierceBrosnan=[
"GoldenEye (1995)",
"Tomorrow Never Dies (1997)",
"The World Is Not Enough (1999)",
"Die Another Day (2002)"
]

#list of 007 movies where Daniel Craig features James Bond 
moviesDanielCraig=["Casino Royale (2006)",
"Quantum of Solace (2008)",
"Skyfall (2012)",
"Spectre (2015)"]


# **1)** create a list of lists (movies007). The list will be composed by each list of movies featured by each actor.

# In[11]:


movies007List = [moviesSeanConnery, moviesDavidNeven,moviesGeorgeLazenby,moviesRogerMoore,moviesTimothyDalton,moviesPierceBrosnan,moviesDanielCraig]
print (movies007List)


# In[ ]:





# **2)** How many movies were played by the first actor to play James Bond?

# In[14]:


len(movies007List[0])


# In[ ]:





# **3)** How many movies were played by the last actor to play James Bond?

# In[15]:


len(movies007List[-1])


# In[ ]:





# **4)** How many actors played the role of James Bond?

# In[16]:


len (movies007List)


# **5)**  Create a new list with the number of movies played by each actor

# In[17]:


newList = [len(movies007List[0]), len(movies007List[1]), len(movies007List[2]), len(movies007List[3]), len(movies007List[4]),len(movies007List[5]),len(movies007List[6]),len(movies007List[-1])]
print(newList)


# In[ ]:





# In[ ]:





# In[ ]:





# **6)**  How many movies were played by the actor who appeared most often in movies?

# In[18]:


max(newList)


# **7)**  How many movies were played by the actor who appeared in fewer movies?

# In[19]:


min(newList)


# **8)**  Create a new list (movies007a) with all the films. 

# In[ ]:


movies007a


# In[ ]:





# **9)** Sort the elements of the list 

# In[ ]:





# In[ ]:





# **9)** Reverse the order of the list. What will happen if this method is executed twice? Does this method sort the list if it is not sorted?

# In[ ]:





# In[ ]:





# **10)** What is the index of the movie "Spectre (2015)" in the list of movies

# In[ ]:





# **11)** Add the movie "007 and the bad Guy of the climate change (2020)" in the 11th position.

# In[ ]:





# In[ ]:





# **12)** It was a mistake. Remove the movie "007 and the bad Guy of the climate change (2020)"

# In[ ]:





# In[ ]:




