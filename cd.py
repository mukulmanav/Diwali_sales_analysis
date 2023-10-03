#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
# %% to avoid encoding error, use 'inocode_escape'
df=pd.read_csv("Datasets/Diwali_Sales_Data.csv",encoding= 'unicode_escape')

# %%
df.shape
# %%
df.describe()
# %%
df.head()
# %% droping blank useless columns
df.drop(['Status','unnamed1'],axis=1,inplace=True)

# %% to check null values
pd.isnull(df).sum()

# %% droping null values
df=df.dropna()
# %%
pd.isnull(df).sum()
# %%
df.dtypes
# %% converting amount float to int
df['Amount']=df['Amount'].astype('int')

# %%
df.rename(columns={'Marital_Status':'Shaadi'})
# %%
plt.figure(figsize=(15,12))

ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)



# %%
plt.figure(figsize=(15,12))
sales_gen=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

ax= sns.barplot(x='Gender', y='Amount' ,data = sales_gen)
for bars in ax.containers:
    ax.bar_label(bars)

# %% Analysis acc to the age

ax = sns.countplot(data=df,x='Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)
# %%Total amount vs Age group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)
# %% total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')

# %% total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')

# %% Marital status
ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)

# %%
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
# %% 
df.columns

# %% Occupation
plt.figure(figsize=(20,5))
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)

# %%
sales_occ = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sales_occ

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_occ, x = 'Occupation',y= 'Amount')
# %%
df.columns
# %% Product_Category
ax=sns.countplot(data=df,x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
# %%
sales_pc=df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_pc, x = 'Product_Category',y= 'Amount')
# %%
df.columns
# %%
sales_pid = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_pid, x = 'Product_ID',y= 'Orders')
# %%
fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
# %%
