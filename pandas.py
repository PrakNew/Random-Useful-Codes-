import pandas as pd
import numpy as np
data = pd.read_csv(url, delimiter=',', na_values=False,index_col = False) # this is done for reading the csv file and storing in multidimensional array basically a 2D array 

############################################
df = pd.DataFrame(np.random.randint(10,size=(3,2)))
#play with pandas by using above data
############################################

data=data.iloc[:,:24] # this is used to fetch specific number of rows and columns 
cols = data.columns # returns the list of all the column headers
data[col].fillna('') # this is used to replace all the NA in a particular col with ''
pd.DataFrame()# this is used for creating a 2D array which is complete and something can be added 
data.groupby(data.iloc[:, 3])# this is like sql like group by in terms of particular columns 
data.iteritems()# this is used to create a tuple over which you can iterate over the items each column at a time
data.reset_index(drop=True)# suppose for the first index elements in each row are [0,1,2,0,1,0,1,2,3,4]---> it needs to be converted to [0,1,2,3,4,5,6,7,8,9] 
#basically drop=True will drop the index column created but still the indexing will be reset
data.shape()# this returns a tuple of [rows,columns]
np.where(data['row_sequence'] == 10, 'Table Header','Value Row')#this is a part of numpy library where we used to check if else condition and put value relatively inside a columns efficiently 
data[data['row_type']=='Table Header'].index.tolist() #this is a special type of filtering we have applied in the data using pandas
data.at[position,data.columns[number]]#retrieves data at a particular row and particular column
data.iterrows()#it is like iterating over each row 

data.drop(data.index[index_list]) #this is basically to drop all the data at particular indexes row wise 
df.drop(['C', 'D'], axis = 1) == df.drop(df.columns[[0, 4, 2]], axis = 1, inplace = True) #dropping the column column wise
#inplace = True means wahi ki wahi drop kardo matlab ki dataframe ko modify kardo now ab drop karne ke baad df = df.drop karne ki jarurat nahi 
df.drop_duplicates(subset=['col1'],keep=False)#removing duplicates from a particular column
del df['one']==df.pop('one') #column wise

df = df.append(df2)#same columns will be appended else the NAN will be present in the place which is not given
#***** this method has be depricated and now we only use pd.concat() function axis=0 instead to do all this appending of dataframes

df.values #this refers to a normal row of data in a list format but if it is used inside a loop of iterrows and done like rows.values[1] this means second element of each row
------------------------------------------------------------------------------------------
Referring to the notes now ---------->

PANDAS->
Pandas is an open-source Python Library providing high-performance data manipulation and analysis tool using its powerful data structures

Two important data types defined by pandas are Series and DataFrame.
DataFrame is a container of Series, Panel is a container of DataFrame.
The name Pandas is derived from the word Panel Data – an Econometrics from Multidimensional data.

-------------------
1> SERIES---> Series is basically a collection of single column like a vertical vector and they are also immutable 
s = pd.Series(np.random.randn(4), name='daily returns')# here a column name is daily returns and a vector of size 4 has been created
s=s * 100 #means each element has been multiplied by 100
np.abs(s)#gives the absolute value of each element 

s.describe()# describes every thing including mean count std, etc of the selected column

s.index = ['AMZN', 'AAPL', 'MSFT', 'GOOG']# we can change from by default indexes to these names
infact now updating and accessing the variable through s['AMZN'] is also possible after above index has been defined 

s.empty# returns true or false
s.ndim #returns the number of dimesions 	
s.size #returns number of columns
--------------------
--------------------
2> DataFrame--> While a Series is a single column of data, a DataFrame is several columns, one for each variable.
************* here we refer rows as indexes and columns remains columns

df = pd.read_csv("<path>")#this is an important method in pandas to read data from CSV
pandas.core.frame.DataFrame----> it is basically a type(df)
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)#this is also a method of creating a dataframe from the data provided
dataflair_df1=pd.DataFrame(7*np.random.randn(6,3),columns=['c1','c2','c3'])#this creates a random dataframe of size 6*3 where each element is multiplied by 7

df.T #this is basically use to transpose in the multidimensional array
df.axes # this basically returning the rows and column labels
df.dtypes #this specifies the data type of each column
df[2:5]# this will select the data from row 2 to 4 and all the columns in it 
df[['<col1>', '<col2>']]# this a method to fetch all the specific columns and the complete rows
now the question arises how can i fetch both rows and columns sidewise

df.iloc[2:5, 0:4]# first part is rows and 2nd part is columns 
**** now over here if we provide df[first][second] first should be the column name/number and second should be the Row/Index
but if we see the df.iloc[first,second] here first is row/index and second is column

df.loc[df.index[2:5], ['country', 'tcgdp']] #this is even better method to fetch using columns name which are specific if you don't know the index
df.loc[df.index[[2,4]],]# this helps in fetching the specific rows only like here 2 and 4rth row only 
print(df.loc[df.index[[2,4]],["c1","c3"]]) #used for fetching specific rows and specific columns
#we also have a hybrid method for indexing in the dataframe to access elements 
df.loc[(df['col1']<=0.3) & (df['col3']>=0.4)] this will return all the rows having col1 values less than 0.3 and col3 should be greater than 0.4---- thats how we apply filters in the pd.DataFrame


df.ix[:,"A"] #this is a small example of how to use the ix[] method 

df = df.set_index('country')#this will replace the normal index of 0,1,2 by country columns elements
df.columns = 'population', 'total GDP'# here we are renaming the columns names which we have used earlier
df['population'] = df['population'] * 1e3# this is like applying a specific operation to each and every element of column population 
df['GDP percap'] = df['total GDP'] * 1e6 / df['population']# this is an example showing that a new column name GDP percap has been formed which consists of the the result applied on each element of the columns in the df
One of the nice things about pandas DataFrame and Series objects is that they have methods for plotting and visualization that work through Matplotlib.
ax = df['GDP percap'].plot(kind='bar')
ax.set_xlabel('country', fontsize=12)
ax.set_ylabel('GDP per capita', fontsize=12)
plt.show()
----> this is an example showing how to use a data in pandas to plot a bar graph

df = df.sort_values(by='GDP percap', ascending=False)# this is a specific method to sorting based on a particular column in a dataframe 


------------------suppose we want to get some file from internet and add it to the pandas then we have to import another library i.e. request 
url = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
source = requests.get(url).content.decode().split("\n")
data = pd.read_csv(url, index_col=0, parse_dates=True)
data.head()  # A useful method to get a quick look at a data frame
pd.set_option('precision', 1)# this will set the precision to a specific value and that can be extracted 

data.describe()  # Your output might differ slightly
df.describe(include=['object'])#this include part along with object used to summarize all the string columns it also include the numbers and all option in include

ax = data['2006':'2012'].plot(title='US Unemployment Rate', legend=False)
ax.set_xlabel('year', fontsize=12)
ax.set_ylabel('%', fontsize=12)
plt.show()# now this is all a normal plotting 


------------------------------------------------
We have one more datastructure in the pandas which is basically Panel, it is basically a collection of dataframes so it is basically 3D
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p['Item1'] #this is a basic method to create and access a panel element 



--------certain specific functions in dataframes

df.sum()  #returns the sum of each and every column
df[df.columns[0]].sum() #specifically the first column sum
df.mean(); df.std() ;prod()

********** for custom wise functions we have 
Table wise Function Application: pipe()

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)

Row or Column Wise Function Application: apply()

df.apply(np.mean)
df.apply(lambda x: x.max() - x.min())
Element wise Function Application: applymap()
df.applymap(lambda x:x*100)

------- if suppose we want to change a specific column only then 
a["c1"]=a["c1"].map(lambda x:x+100)#applied on specific column
df.loc['b'] = np.square(df.loc['b']) #applied on specific row whole slectively

-----------Reindexing
df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])#fetching specified columns and rows
-----------Renaming 
df.rename(columns={'col1' : 'c1', 'col2' : 'c2'},index = {0 : 'apple', 1 : 'banana', 2 : 'durian'})#renames the specified column and rows

----------Iterating over the items in dataframe 
for x in df: print(x) #prints the columns name
df.iteritems()#here a key value pair is there where column_label as key and column value as a Series object.
df.iterrows()#here key is the index in numeric and value is the rows where each element can be easily accessed by either .values() or by square brackets []
************** we cannot modify any value while iterating in the sequence 
for x in df.itertuples():# here each x will be the a tuple of each index then a collection of each row The first element of the tuple will be the row’s corresponding index value, while the remaining values are the row values.

--------------------sorting
.sort_index() #here sorting of the index only not the values ascending=False can be passed as a parameter
***** if we provide the parameter as axis=1 then using the column wise it will sort the complete rows but beware the complete column will be swapped 
df.sort_values(by="col1") #sorting the values in terms of values by column number 1 or we can also do like by=df.columns[1]  

---------applying string operations in the series elements
it can be applied to a series only
df["col1"].str.upper() # taking 1 complete column at a time

------------ some basic statistical function we can apply on the pandas elements
.pct_change()#this is percentage changes which we can see by comparing the previous element with the current element
s1.cov(s2) #covariance
frame['a'].corr(frame['b'])#correlation
s.rank()#it also supports parameters like average min max first 

df.rolling(window=3).mean()#this is a special type of statistically use of mean function as we use n,n-1,n-2 elements to find out the value of the element because the window provided by us is 3 ****note the first 2 values will become null and replaced 
df.expanding(min_periods=3).mean()
df.ewm(com=0.5).mean()
Window functions are majorly used in finding the trends within the data graphically by smoothing the curve and the above 3 are the window functions 


---------------Missing values in the table and its handling 
df['one'].isnull() #checks that the data is NaN or not returns true and false 
Calculations with Missing Data
	When summing data, NA will be treated as Zero
	If the data are all NA, then the result will be NA

df.fillna(0) #this is used to fill and replace the elements with a particular value
**** method='pad' #it is like a parameter which we can pass inside the fillna like here pad means to copy the just above value
method='backfill' #it is to copy the below value to the above NA

df.dropna()#drops all the rows which will have na inside them 

df.replace({1000:10,2000:60})#this is a special method which replaces each element(basically key over here) with a specific value using the dictionary methodology 

------------------------using group by inside the pandas library and doing things like sql
df.groupby(['col1','col2']).groups # returns the dictionary with keys as the actual values on which the data is actually grouped together and the values as the list of all the indexes where the particular key can be found

grouped = df.groupby('Year')
for name,group in grouped: #here name will be the actual value of the grouped column values and the group here represents the complete other data which is left behind 
grouped.get_group(2014) # represents the complete grouped values over a particular grouped value
grouped['Points'].agg(np.mean)#example of a function which we can apply inside the particular column using grouping and aggregation 
grouped['Points'].agg([np.sum, np.mean, np.std])#enhanced values which we can apply inside the aggregation function 
score = lambda x: (x - x.mean()) / x.std()*10
print grouped.transform(score)# this will use a specific function and transform the grouped values in the table
df.groupby('Team').filter(lambda x: len(x) >= 3)# this is an example of filtering the data over a specific teams who have count more than or equal to 3


-------------------------JOining dataframes like sql databases we can easily do and most efficiently do by using the inbuilt funtion here
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,left_index=False, right_index=False, sort=True)

--------------------------CONCTINATING THE DATA similar as above 
 pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)
 pd.concat([one,two],keys=['x','y'])#example
 one.append(two)
