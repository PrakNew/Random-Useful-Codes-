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


a=np.arange(10,100) # for creating a array of a specific range
#always assign the reshape to the variable
a=a.reshape((9,10))

#create an Identity matrix
np.eye(6,dtype='int') #6*6 matrix is created
#suppose we wanted to create a matrix with diagonal set to specific values rest all 0
np.diag(range(6))

#creating random array
np.random.seed(0) # basically saves the state of the np.random so like now if we again call np.random.seed(same_integer) followed by np.random.rand(same as used) it will generate the exact same numbers and not just the random numbers available
np.random.rand(5,10) #a 5*10 array of random float numbers 
np.random.rand(5,10) + 100 # this is basically returning us the randomly generated values in addition with 100 to each of the value


#iterate over all the values in an array in numpy
for i in np.nditer(a): # it will print all the numbers sequentially not need to apply 2 for loops
    print(i)  

# linear spacing between the specific range

np.linspace(start,stop,num) # as the name suggest it will create an array of length num with linear spacing between the start and stop point where start in inclusive and stop is exclusive

np.random.randint(start,stop,num)# getting the integer values between the specific range

#when we have a specific choice
np.random.choice(range(1,50),size=6,replace=False) # here replace=False means we need no repetition in our choices  
