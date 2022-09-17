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
np.arange('2021-01-01', '2021-02-01', dtype='datetime64[D]') #this also works here
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

#---------------------------------------------------------------------------------------------------------------------------Section 6
#saving into binary file the array and then reloading it
np.save('abc.npy',A)
A=np.load('abc.npy') 
#basically dumps and loads
#similarly we have for text files
np.savetxt(filename='abc.txt',X=A)
A=np.loadtxt('abc.txt')

#converting an array to a list
#***** most usefult function
A.tolist()

A[::-1] #reverses the array in python + slicing is supported in array
newrow = [1, 2, 3]
A = numpy.vstack([A, newrow]) #appending a row in numpy

np.pad(A, pad_width=1, constant_values=0) #padding / adding values to the boundaries of the array

A[::2, ::2] = 10 #We can assign the values likewise using slicing
A[1::2, ::2] = 5 # This is appropriate way to set the data 

C=np.append(A,B,axis=0) #we will get the appended values inside the newly created C

#intersection of values in two numpy array
C= np.intersect1d(A, B)

#to get the unique values of the numpy array
C=np.unique(A) 

#printing the maximum of each row/col 
np.argmax(A,axis=0) #returns list of indexes where the maximum element can be found
np.max(A,axis=0) #returns the maximum element in each row/column based on axis 

#----------------------------------------------------------------------------------------------------------------Section 7 started
A=np.sort(A,axis=1) #sorting in terms of column or row in numpy

#finding all rows and columns based on codition 
A[A>8] #applying conditions over there inside brackets

np.where(A>10.0,11.0,A) #used where we have to replace the given value applying the condition 

np.ravel(A) #flattens the numpy array into single array

np.zeros_like(A) #create a similar size array with all the values as zeros

np.full_like(A,1) #same as above just putting a constant values instead of zeros

'''[[1. 0. 0. 0. 0.]
 [1. 1. 0. 0. 0.]
 [1. 1. 1. 0. 0.]
 [1. 1. 1. 1. 0.]
 [1. 1. 1. 1. 1.]]
''' 
#creating an array like this

np.tri(5,5) or np.tri(N=5) 

#creating an array of random integers within a specific range and specific size

np.random.randint(low=0,high=256,size(200,300),dtype = np.uint8)

#-------------------------------------------------------------------------------------------------------- Section 8
np.expand_dims(A,axis=0) #increases the dimention like (2,3)->(1,2,3) 2D changed to 3D

np.squeeze(A,axis=0) #decreases 1 dimention like (1,2,3)->(2,3) 3D->2D

#*** fetch out the values of specific column or columns 
A[:,1] #fecth out whole first column as a series
A[:[1,5]] #fetch out the first and the fifth column 
#similarily we can do for rows

#-------------------------------------------------------------------------------------------------------- Section 9
np.concatenate((A,B),axis=0) #concatinating 2 arrays 

np.column_stack((A,B)) #convert column to rows basically does the transpose

a,b,c=np.split(A,[2,6],axis=1) #spliting basically into different parts 

np.count_nonzero(A) #returns the count of non zero element

np.set_printoptions(precision=4) #setting the precison to a specific value to all the float elements
np.set_printoptions(suppress=True,precision=8)#similar as above just supressing mathematical notations
np.set_printoptions(edgeitems=10) #setting edgeitems here.

#** removes|Deletes particular column/row from the numpy array
np.delete(A,[2],axis=1) #3rd column will be deleted

np.linalg.norm(A) #calculate the norm of the array

#------------------------------------------------------------------------------------------------------------ Section 10
#*****arithmetic mean element wise not whole
(A+B)/2 or np.divide(np.add(A,B),2)

#*** element wise multiplication 
A*B or np.multiply(A,B)

#*** element wise square root
np.sqrt(A)

#*** element wise power
A**2 or np.power(A,2)

#sine/cosine and all trigos
np.sin(A)/np.cos(A)

#compare 2 numpy arrays as element wise equal within a tolerance
np.allclose(A,B)

#*** Matrix multiplication 
A@B or np.dot(A,B) or A.dot(B)

#determinant calculation 
np.linalg.det(A)
np.linalg.eig(A) #eigen values
np.linalg.inv(A) #inverse 

#Trace of array i.e sum of diagonal 
np.trace(A)

#-------------------------------------------------Section 11
#randomly shuffle the values inside array
np.random.shuffle(A[1:]) #**** no need to make it equal to A it will automatically change the values inside the Array
#[1:] means keeping first row same and below values shuffle

#indexes that would sort an array 
np.argsort(A)

#rounding values to n decimal places 
np.round(A,decimals=3)

#**********calculating the roots of a polynomial equation
W = np.array([4, 5, 1]) #this is equivalent to (4x**2+ 5x + 1)
print(np.roots(W))

# Polynomial addition 
W = np.array([4, 5, 1])
Q = np.array([2, 4, -5, 1])
 
print(np.polyadd(W, Q))
print(np.polysub(W, Q))
print(np.polymul(W, Q))
print(np.polyadd(W, 2 * Q))

#** sign function returning if the number is positive negative or zero
np.sign(A)

#*** printing todays date
np.datetime64('today')

#----------------------------------------Section 12
