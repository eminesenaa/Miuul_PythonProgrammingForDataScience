import numpy as np

# ! NUMPY = NUMERICAL PYTHON

a = [1,2,3,4]
b = [2,3,4,5]
ab = []

for i in range(len(a)):
    ab.append(a[i] * b[i])

print(ab)

# via numpy

a = np.array([1,2,3,4]) # this is to way to create a numpy array
b = np.array([2,3,4,5])

print(a * b)

print(type(a))

np.zeros(10, dtype = int) # create a list size of 10 only 0s

np.random.randint(0 , 10 , size = 10) # create a list size of 10 w random numbers btw 0 and 10

##############################
# ? avg = 10
# ? st. devia. = 4 
# ? 3 : 4
np.random.normal(10 , 4, (3,4))  
##############################


