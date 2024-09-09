# What You're Aiming For

# Write a Pandas program to create and display a DataFrame from the following dictionary data with index labels.

# exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],

# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],

# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],

# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
import numpy as np 

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print("Print the three first rows using the head() method.")
data = pd.DataFrame(exam_data)
print(data.head(3))

print("\n Delete rows with Nan values.")
clean_data = data.dropna()
print(clean_data)

print("/n Extract the 'name' and 'score' columns from the DataFrame.")
print(data[['name','score']])

# Write a Pandas program to append a new row 'k' to the DataFrame with these values (name: "Suresh", score: 15.5, attempts: 1, qualify: "yes"). please help me put this in print 
data.loc['k'] = ['Suresh','15.5','1','yes']
print(data)

print("/n Write a Pandas program to delete the 'attempts' column from the DataFrame.")
drop_data = data.drop(['attempts'], axis='columns')
print(drop_data)

print("/n Add a new column Success: if the score is higher than 10 we will have 1, else we will have 0.")
data['score'] = pd.to_numeric(data['score'], errors='coerce')
data['Success'] = data['score'].apply(lambda x: 1 if x > 10 else 0)
print(data)


data.to_csv('Data.csv')