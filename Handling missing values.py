import pandas as pd 
data = {'A': [1, 2, None, 4, 5],       
'B': [None, 6, 7, 8, 9],       
 'C': [10, 11, 12, None, 14]}   
df = pd.DataFrame(data)                
df.fillna(df.mean(), inplace=True) 
print(df)
