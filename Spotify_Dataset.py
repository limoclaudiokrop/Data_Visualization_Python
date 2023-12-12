#!/usr/bin/env python
# coding: utf-8

# # Data Visualization Python

# ## Spotify Dataset
# The dataset for this tutorial tracks global daily streams on the music streaming service Spotify. We focus on five popular songs from 2017 and 2018:
# 
# 1. "Shape of You", by Ed Sheeran (link)
# 2. "Despacito", by Luis Fonzi (link)
# 3. "Something Just Like This", by The Chainsmokers and Coldplay (link)
# 4. "HUMBLE.", by Kendrick Lamar (link)
# 5. "Unforgettable", by French Montana (link)

# ## Set up notebook

# In[2]:


# Imports
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
print("Setup Complete")


# ## Load and Examine Data

# In[6]:


# Path of the file to read
spotify_filepath = "./spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Print the first 5 rows of the data
spotify_data.head()


# In[7]:


# Print the last five rows of the data
spotify_data.tail()


# Notice that the first date that appears is January 6, 2017, corresponding to the release date of "The Shape of You", by Ed Sheeran. And, using the table, you can see that "The Shape of You" was streamed 12,287,078 times globally on the day of its release. Notice that the other songs have missing values in the first row, because they weren't released until later!

# ## Plot the data using lineplot

# In[9]:


# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)


# ## Analysis
# From the above graph, the songs follow a bell curve. That is the streams rapidly grows after the songs is released, reaches a peak and then gradually falls as time passes. Additionally although different songs might have different streams at the begining or the peak, they generally fall to about the same streams in the long run. 

# In[ ]:




