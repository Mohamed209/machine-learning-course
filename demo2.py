import numpy as np

def center_matrix(array):
    """
    return square matrix center sub matrix
    """
    return array[array.shape[0]//2-1:array.shape[0]//2+1,array.shape[0]//2-1:array.shape[0]//2+1]
a=np.random.randint(low=1,high=10,size=(6,6))
print("original array",a)
print("center matrix ",center_matrix(a))