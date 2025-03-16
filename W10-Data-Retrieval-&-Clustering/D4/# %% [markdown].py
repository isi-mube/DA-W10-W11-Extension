# %% [markdown]
# # PCA Lab
# In this notebook, you will work with Principal Component Analysis (PCA) using a customer retail dataset.

# %% [markdown]
# ## Step 1: Load our customer data
# 

# %%
import pandas as pd

# Load the dataset
df = pd.read_csv('retail_customer_data.csv')

# Display the first few rows of the dataset
df.head()


# %% [markdown]
# ## Step 2: Standardize the Data
# Standardizing the data is a crucial step before applying PCA. This will ensure each feature has a mean of 0 and a standard deviation of 1.

# %%
from sklearn.preprocessing import StandardScaler

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
scaled_df.head()

# %% [markdown]
# ## Step 3: Apply PCA to Reduce Dimensionality
# Now, apply PCA to reduce the dimensionality of the dataset. Let's start by reducing it to 2 components.

# %%
from sklearn.decomposition import PCA

# Apply PCA with 2 components
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_df)

explained_variance = pca.explained_variance_ratio_
print("Explained variance ratio:", explained_variance)

# %% [markdown]
# ### Exercise 1: Analyze the Explained Variance
# What do the explained variance ratios tell you about the data? How much of the original data's variance is captured by the first two principal components? Write your observations below.

# %%
#Your answer here

# %% [markdown]
# ## Step 4: Visualize the PCA Results
# Let's visualize the dataset in the new PCA-transformed 2D space.

# %%
import matplotlib.pyplot as plt

# Plot the PCA results
plt.figure(figsize=(8, 6))
plt.scatter(pca_result[:, 0], pca_result[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA on Random Dataset')
plt.show()

# %% [markdown]
# ### Exercise 2: Interpretation of the Plot
# Interpret the scatter plot. Do you notice any clusters or patterns? What might this indicate about the underlying structure of the data?

# %%
#Your answer here

# %% [markdown]
# ## Step 5: Experiment with Different Number of Components
# Experiment with applying PCA with a different number of components (e.g., 3 or 4). Observe how the cumulative explained variance changes.

# %%
# Apply PCA with 4 components
pca = PCA(n_components=4)
pca_result = pca.fit_transform(scaled_df)

cumulative_variance = pca.explained_variance_ratio_.cumsum()
print("Cumulative explained variance:", cumulative_variance)

# Plot cumulative explained variance
plt.figure(figsize=(8, 6))
plt.plot(range(1, 5), cumulative_variance, marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Cumulative Explained Variance by PCA Components')
plt.show()

# %% [markdown]
# ### Exercise 3: Reflection on PCA Components
# Reflect on how the cumulative explained variance changes as more components are added. What does this suggest about the number of components needed to adequately represent the data?

# %%
#Your answer here

# %% [markdown]
# ## Conclusion
# In this lab, you applied PCA to a new retail customer dataset. You learned how to standardize data, apply PCA, and interpret the results. Notice how PCA can be useful in reducing dimensionality while retaining as much information as possible.


