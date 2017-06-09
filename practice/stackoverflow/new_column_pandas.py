"""
https://stackoverflow.com/questions/44415009/create-a-new-pandas-column-with-a-value-from-a-user-defined-function

I am getting a SettingWithCopyWarning when attempting to create a new column on a pandas dataframe using a function I created to return a value for that new column. I am using the movielens dataset and predicting the rating of a user on a movie.

This is an example of my dataframe:

enter image description here

Now if I want to add a new column called 'prediction' that sends the user_id and item_id to my function and return the prediction I have followed the advice of this other question

Hence using the code:

df['pred'] = df.apply(lambda x: predict_rating(x['user_id'], x['item_id']), axis =1)
Yet I keep getting the SettingWithCopyWarning.

:44: SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value instead See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy

Any advice would be welcome.

"""
#%%
import pandas as pd

df = pd.DataFrame({'user_id':[22,224], 'item_id': [377,29], 'rating': [1,3]})
#%%
def prediction_func(row):
    return row['user_id'] + row['item_id']
    
#%%
df['prediction'] = df.apply(prediction_func, axis=1)
#%%
print(df.head())

"""
Author said this still gives them the same error, yet I cant reproduce it. 
Prehaps I am using a different python version
"""
