# This tutorial is based on the questions faced in Udemy Course so far
import numpy as np

A = np.array([[0, 0, 0],
              [0, 0, 0]])
np.any(A) # returns true or false where the values are 0 or not

A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])
np.isnan(A) # checks if the values are having nan values or not

A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

np.allclose(A,B) # checks if the values are close enough or not 
A==B # here this means to check the values individually and return the array 
#similarily we can do operations like A>B 


np.zeros(shape=(4, 4), dtype='int') #create an array of size 4*4 instead of shape we can also write [4,4]

np.full((10,10),256,dtype=float) # create an array of size 10*10 having a fixed value like here 256 
np.ones(shape=(10, 10), dtype='float') * 255 # this is equivalent to the above function 
