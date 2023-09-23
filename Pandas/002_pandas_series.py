import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
print(type(s))
print(s.index)
print(s.dtype)
print(s.ndim) # pandas series has one dimension
print(s.values) # type of this is numpy.ndarray 
print(s.head()) # displays the first five elements
print(s.tail(3)) # displays as many elements as requested from last