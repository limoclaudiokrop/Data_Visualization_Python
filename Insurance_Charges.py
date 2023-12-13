

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
print("Setup Complete")



# Path of the file to read
insurance_filepath = "./insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

insurance_data.head()



plt.figure(figsize=(10,6))
plt.title("Insurance charges relations to bmi")
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])




plt.figure(figsize=(10,6))
plt.title("Effect of smoking on relation of Insurance chargesto bmi")

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)


# ## Categorical Scatter plot / Swarmplot
# Below plot shows that on average, non-smokers are charged less than smokers, and the customers who pay the most are smokers; whereas the customers who pay the least are non-smokers.
# 

# In[12]:


plt.figure(figsize=(10,6))
sns.swarmplot(x=insurance_data['smoker'],
              y=insurance_data['charges'])


# In[ ]:




