import pandas as pd

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
print(df.iloc[10])