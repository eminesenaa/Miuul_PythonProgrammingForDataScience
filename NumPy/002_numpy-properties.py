import numpy as np

# * ndim: dimension count
# * shape : dimension info
# * size: total element number
# * dtype: array data type

a = np.random.randint(10 , size = 5)
print(a.ndim) # 1
print(a.shape) # 5 
print(a.size) # 5
print(a.dtype) # int


b = np.random.randint(10 , size = (3,4))
print(b)
print(b.ndim) # 1
print(b.shape) # 5 
print(b.size) # 5
print(b.dtype) # int


# ! reshape

np.random.randint(1, 10 , size = 9)
np.random.randint(1, 10 , size = 9).reshape(3,3)  # if size is 10, doesnt work

ar = np.random.randint(1, 10 , size = 9)
ar.reshape(3, 3)



# ! index operations
a = np.random.randint( 10 , size = 10 )

a[0]
a[0 : 5]
a[0] = 999


m = np.random.randint( 10 , size = (3,5))
m
m[0 ,0]
m[1,1]
m[1,1] = 999
m[1,1]

m
m[: , 0]  # 0th index of all rows
m[0, :]   # 0th index of all columns

m
m[0:2 , 0:3]


# ! fancy index

v = np.arange(0 , 30 ,3) # [0,  3,  6,  9, 12, 15, 18, 21, 24, 27]

catch =  [ 1, 2, 3] 
v[catch]   # gets the elements in these indexes, thats reaaly useful when working w huge sizes


# ! conditional action

c = np.array([1,2,3,4,5])
print(c ** 2)

# classic
l = []
for i in c:
    if i < 3:
        l.append(i)


# via numpy
c[c < 3 ] 
c[c > 3 ] 
c[c == 3 ] 
c[c != 3 ] 


# ! mathematical operations

o = np.array([1,2,3,4,5])

o / 5
o * 5 / 10
o ** 2
o - 1 

#####

np.subtract(o , 1)
np.add(o , 1 )
np.mean(o)
np.sum(o)
np.min(o)
np.max(o)
np.var(o)

# ? equation solution

# 5 * x0 + x1 = 12
# x0 + 3 * x1 = 10 

a = np.array([[5,1] , [1 , 3]])
b = np.array([12, 10])
np.linalg.solve(a, b)







