# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:48:57 2021

@author: prakhar.newatia
"""

import camelot
import os
import pandas as pd
import numpy as np

def merging_rows(df):#this function is for removing the blank rows and merging it in the above row
    a=pd.DataFrame(df.iloc[0].values)#taking out the first row values 
    for ind,val in df.iterrows():
        if ind==0:
            continue
        a[0]=a[0].astype(str)+"\n"+df.iloc[ind].values.astype(str)#converting each element as string and then nomally conctinating
    return a.T

file =os.path.abspath(r"C:\Users\prakhar.newatia\Downloads\tosend\Data Ingestion\71169052 W L&P Worcestershire Sauce 150ml.pdf")
tables = camelot.read_pdf(file)
df1=pd.DataFrame()
df1=df1.append(tables[0].df)
df1=df1.append(pd.Series(["ending"]), ignore_index=True)#this is just a normal table which marks the end of the table
initial_ind=0
cleaned_csv=pd.DataFrame()
flag=0
ind=0
#iterating over rows to fetch out the blank rows and then applying fuction over it
for ind,val in df1.iterrows():
    if len(df1.iloc[ind,0])==0:
        flag=1 
    if flag==1 and len(df1.iloc[ind,0])!=0:
        temp=(df1.iloc[initial_ind:ind])
        temp=temp.reset_index(drop=True)
        #print(initial_ind,ind,"\n")
        temp1=merging_rows(temp)
        cleaned_csv=pd.concat([cleaned_csv,temp1])
        initial_ind=ind
        flag=0
    elif flag==0 and ind!=0:
        cleaned_csv=pd.concat([cleaned_csv,pd.DataFrame(df1.iloc[ind-1]).T])
        initial_ind=ind
#print(ind,initial_ind)

cleaned_csv=cleaned_csv.reset_index(drop=True)
cleaned_csv.to_csv(r"C:\Users\prakhar.newatia\Desktop\71169052 W L&P Worcestershire Sauce 150ml.csv",index=None)
#print("%r"%cleaned_csv.iloc[14,0],"herer")

#print("done")
#print('%r'%cleaned_csv.iloc[13,1])
#print('%r'%cleaned_csv.iloc[13,2])
#--------------------------- working on tabular data extraction 

#this function is for converting the single row to multiple rows based on the \n criteria
def converting_rows(df,counter):
    l=[]
    #print(df)
    try:
        for x in range(0,15):
            l.append(df[x].split("\n"))
            #print("--------")        
    except :#this is for the valueerror suppose the series do not have 15 columns then
        pass
    dftemp=pd.DataFrame(l)
    #print(dftemp.T)
    dftemp1=dftemp.T
   # dftemp1.fillna(" ",inplace=True)
    dftemp1= dftemp1.replace(r'^\s*$', np.nan, regex=True)#replacing each empty string or none with NAN
    dftemp1.dropna(axis=0,how="all",inplace=True)
    dftemp1['Table Number']=counter
    dftemp1['Attribute Name']=""
   # print(l)
    return dftemp1
final_output=pd.DataFrame(columns=['Attribute Name','Table Number',0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
count=1
for ind, val in cleaned_csv.iterrows():
    if cleaned_csv.iloc[ind,0].count("\n")>=2:#checking which is table and which is not
        #print(ind)
        final_output=pd.concat([final_output,converting_rows(cleaned_csv.iloc[ind],count)])
        count+=1
final_output.dropna(axis=0,how="all",thresh=None)
final_output=final_output.reset_index(drop=True)
final_output.to_csv(r"C:\Users\prakhar.newatia\Desktop\onlytables71169052 W L&P Worcestershire Sauce 150ml.csv",index=None)


