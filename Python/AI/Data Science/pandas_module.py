import pandas as pd

df = pd.read_csv('pokemon_data.csv') # -----> df - for Data Frame

# Load all the data 
#print(df)

# Load specific items 
#print(df.head(6)) -----> Show the uper data
#print(df.tail(6)) -----> Show the down data

# Load exel files
# df_xlsx = pd.read_xlsx('pokemon_data.xlsx')

# Load txt files
# df_txt = pd.read_csv('pokemon_data.tex', delimiter = '\t')

# ------------------------------------------------------------------------------------------ #

# Read only the headers 
#print(df.columns)


# Read only the each column
#print(df['Name'])
#print(df['Legendary'])

# And can specify the data 
#print(df['Name'][0:6])

# More than one column
#print(df[['Name', 'Speed', 'Type 1']])


# Read each row
#print(df.iloc[2])
#print(df.iloc[2:4])

#for index, row in df.iterrows(): ------> prints all the rows 
    #print(index, row [you can also 'Name'])

# Specific data in data set
#print(df.loc[df['Type 1'] == 'Fire'])


# Read specific location
#print(df.iloc[3, 1])

# -------------------------------------------------------------------------------------- #

# Sorting the data frame 
#print(df.sort_values('Name')) # -----> Sort the Names Alfabetically
#print(df.sort_values('Name', ascending=False)) # -----> Sort the Names backwords

# Can also combine more than one columns 
#print(df.sort_values(['Type 1', 'HP'])) # -----> Give us the lowest value of the df
#print(df.sort_values(['Type 1', 'HP'], ascending=[1,0])) # -----> Change the output

# ------------------------------------------------------------------------------------------------- #

# Add column to the data frame
#df['Totall'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] 
#print(df.head(6))
 
# Or faster
df['Totall'] = df.iloc[:, 4:10].sum(axis=1)
#print(df.head(3))

# Change the positin of a column
#cols = list(df.columns)
#df = df[cols[0:4] + [cols[-1]] + cols[3:12]]
#print(df.columns)
#print(df.head(5))

# ------------------------------------------------------------------------------------- #

# Saving new to CSV
#df.to_('modified.csv', iondex=False)

# Saving new to Exel
#df.to_excel('modified.xlsx', index=False)

# Saving new to Text
#df.to_csv('modified.txt', index=False, sep='\t')

# ------------------------------------------------------------------------------------------ #

# Filtering Data

#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 90)])
# Insteed of and=& can or=|

# New df 
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 75)]
#print(new_df) can also save the new data frame 

# Reset the index of new df
#new_df = new_df.reset_index(drop=True) #-----> Or not 
#print(new_df)

# Change somehting inside a name etc
#new_df = df.loc[df['Name'].str.contains('Mega')]

# If not
#new_df = df.loc[~df['Name'].str.contains('Mega')]

# Checking something special
import re

new_df = df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]
# All that contains Pi
new_df = df.loc[df['Name'].str.contains('pi[a-z]', flags=re.I, regex=True)]
# All start with Pi
new_df = df.loc[df['Name'].str.contains('^pi[a-z]', flags=re.I, regex=True)]

# ---------------------------------------------------------------------------------------------------------- #

# Conditional Changes

# Change the name of a column
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# Recet
df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'

# Setting all fire pokemon Langendary 
df.loc[df['Type 1'] == 'Fire', 'Lengendary'] = True

# Modifiy defferent conditions
df.loc[df['Totall'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2']


# Reacet all the changes 
df = pd.read_csv('modified.csv')

# ---------------------------------------------------------------------------------------------------- #

# Aggregate Statistics


# Avarage Something per group
df.groupby(['Type 1']).mean()
# Showing hightest Attack etc.
df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
# Sum
df.groupby(['Type 1']).sum()
# Count (How many of each type)
df.groupby(['Type 1']).count() # or
df['count'] = 1
df.groupby(['Type 1', 'Type 2']).count()['count']

# --------------------------------------------------------------------------------------------------- #

# Working with large amounts of data 

# Loading not all the data in the same time (5 is the rows)
#for df in pd.read_csv('modified.csv', chunksize=5):
    #print(df)

# Creating new df with emty columns
df_new = pd.DataFrame(columns=df.columns)

#for df in pd.read_csv('modified.csv', chunksize=5):
    #results = df.groupby(['Type 1']).count()
    #df_new = pd.concat([df_new, results]) # contact combines df's together

# Remove columns
print(df.drop(columns=['Name', 'count'])) # or
newnew_df = df.drop(columns=['Name', 'count'])
