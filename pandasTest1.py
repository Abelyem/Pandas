import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

"""" 
COMMENTING OUT SECTIONS RELATING TO EACH OTHER 

# Reads column headers
df.columns 

# Prints out the rows of each column titled below (E.g prints Names, types, HP etc of each pokemon)
print(df[['Name', 'Type 1', 'HP', 'Attack', 'Defense', 'Speed']])

"""


"""
# Reads each row from index 0 to 49
print(df.iloc[0:50])
"""

"""
# Read a specific location (e.g indexing + specific column)
# this goes down by 2 indexes on columns ( to get to Venusaur), then goes across 1 index on row to get to the 'Name'
print(df.iloc[2,1])

# this goes down by 2 indexes on columns ( to get to Venusaur), then goes across 5 indexes on row to get to the 'Attack'
print(df.iloc[2,1])
"""

"""
# Prints out the indexes and the name affialiated on each row 
for index, row in df.iterrows():
    print(index, row['Name'])

"""

"""

# loc looks at labels (e.g Type 1 in this case)
# iloc looks at INTEGER location

print(df.loc[df['Type 1'] == "Fire" ])

# Prints out pokemon at index 10 (refer to line 27/28 for more info on what you can do with this)
print(df.iloc[10])

"""

"""
********** READING AND SORTING THE DATA ***************

# Describes the data (shows count, mean, min, max etc of all column headers)
print(df.describe())

# Sorts name in alphabetical order
print(df.sort_values('Name')) 

# Sorts name in descending alphabetical order
print(df.sort_values('Name', ascending=False)) 

# Sorting using multiple column headers 
print(df.sort_values(['Type 1', 'HP'])) 

# Sorting using multiple column headers - this time asecnding is TRUE (1) for type 1, but FALSE (0) for HP
# Can also just do ascending=False/True to set both to the same thing 
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0])) 

"""



"""
**********  ADDING A COLUMN USING EXISTING DATA ***************

# Creates a new column called 'Total' which consists of the addition of each of the specials below
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# this prints out first and last 5 rows (shows the new total column)
print(df.head(5))

# You can drop the new column created by using the below
df = df.drop(columns=['Total'])
"""



"""
********** ADDING A COLUMN USING EXISTING DATA -- IN A DIFFERENT WAY ***************

# Does same as above (line 77) but cleaner 
# 4:9 is in the index of df['HP'] filtering all the way to df['Speed'] 
# sums this up - axis=1 means it is summed horizontally (axis=0 means adding vertically)

df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(5))

"""


"""
********** Re-ordering columns ***************

# Re-creates the 'Total' column
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# Makes headers into a list 
cols = list(df.columns)

# Uses concatenation to re-order columns -- THIS IS VISUAL ONLY, does not change original data source
df = df[cols[0:2] + cols[4:10] + [cols[-1]] + [cols[3]] + cols[10:12]]

# Printing out result set to see if columns are re-ordered
print(df.head(10))

"""


"""

************  SAVING OUR DATA ************

# to_csv is a save features - creates new file with name 'modified.csv' in same directory you are working on
# index=False removes index if csv file opened with Excel
df.to_csv('modified.csv', index=False)

# Creates a modified file that's now txt and not csv (check file name)
# the list of items are separated by tab (hence \t) - if separated by a comma then would be
# sep=","
df.to_csv('modified.txt', index=False, sep="\t")

"""

"""

************  FILTERING OUR DATA ************

# Filters through to bring back Pokemons which have Type 1 = Grass
print(df.loc[df['Type 1'] == "Grass"])

# Filters through to bring back Pokemons which have Type 1 = Grass AND Type 2 = Poison
print(df.loc[(df['Type 1'] == "Grass") & (df['Type 2'] == "Poison")])

# Filters through to bring back Pokemons which have Type 1 = Grass OR Type 2 = Poison
print(df.loc[(df['Type 1'] == "Grass") | (df['Type 2'] == "Poison")]) 

# Filters and returns names that contain 'mega'
print(df.loc[df['Name'].str.contains('Mega')])

**
# Filters and returns names that DO NOT contain 'mega' (refer to ~ sign written prior to df)
# Did not work at time of testing - cannot find any docs on this
print(~df.loc[df['Name'].str.contains('Mega')])
**

# Filters through Type 1 to get EITHER Fire OR Grass Pokemons
# second filter looks through Type 2 to make sure its a Flying Pokemon
#Conditions = FLYING (Type 2) POKEMON THAT HAS TO BE FIRE OR GRASS BASED (Type 1)
print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True) & df['Type 2'].str.contains('Flying')])


#Same as above (Finds either Fire OR Grass pokemons) 
# flags=re.I -- allows it to ignore the case so we can do fire|grass and
# it still finds any capitalized version (data source has Fire / Grass as Type 1)
print(df.loc[df['Type 1'].str.contains('fire|grass', regex=True, flags=re.I)])

# Filters through all Names and finds any name which has 'pi' in it (anywhere in the name)
print(df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)])


# Filters through all Names and finds any name which has 'pi' in it 
# HOWEVER due to '^' it means the name MUST begin with Pi (^ = start of line)
print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

"""



"""
******************** CONDITIONAL CHANGES ********************

"""