#This is based on udemy tutorial
import pandas as pd
#------------------------------------------------------------------------------Section 15
#creating a series of list
stocks = ['PLW', 'CDR', '11B', 'TEN']
print(pd.Series(data=stocks))
'''0    PLW
1    CDR
2    11B
3    TEN
dtype: object'''
#we can create a series using dictionary key value pairs as well

#converting a series to a list datastructure
A.tolist()

#converting a series to a Dataframe assigning a column name
pd.DataFrame(quotations, columns=['price']) #quotations is a series

#creating series using help of numpy
s = pd.Series(
    data=np.arange(10, 100, 10),
    index=np.arange(101, 110),
    dtype='float',
)

#converting the datatypes
pd.to_numeric(s) or s.astype(int)

#appending elements in series
quotations.append(pd.Series({'BBT': 25.5, 'F51': 19.2}))

#resetting indexes in dataframe
df1.reset_index()

#setting columns names
df1.columns = list('ab')


#basic method to create a datafram
data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}
 
companies = pd.DataFrame(data=data_dict)

#****** converting a specific column to index of the data
companies.set_index('company')



 
