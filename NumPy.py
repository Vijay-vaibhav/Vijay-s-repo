import numpy as np
print(np.__version__)
a = np.array([1,2,32,31])
## Basic operations ###
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a[0])
a[0] = 10000
print(a)

## Basic math ###
b = a*np.array([9,89,899,657])
print(b)
a = a + np.array([4])
print(a)
a = a*np.array([9])
print(a)
a= np.sqrt(a)
print(a)

## Dot products in python versus numpy ###
l1 = [3,6,9]
l2 = [23,5,9]
dot = 0
for i in range(len(l1)):
    dot += l1[i]*l2[i]
print(dot)
#################
a1 = np.array([23,233,213])
a2 = np.array([78,989,667])
pro = np.dot(a1,a2)
print(pro)
pro = a1 @ a2 
print(pro)

## speed test ###
from timeit import default_timer as timer
a = np.random.randn(999)
b = np.random.randn(999)
A = list(a)
B = list(b)
T = 1000
def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot
def dot2():
    np.dot(a,b)
    
start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end-start

start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end-start

print("time for manual:", t1)
print("time for numpy: ", t2)
print("ratio: ", t1/t2)

a = np.array([[7,2],[4,7]])
print(a)
print(a.shape)
print(a[0,1])
print(a[:,0])
print(a[0,:])
print(a.T)
print(np.linalg.inv(a))
print(np.linalg.det(a))
c = np.diag(a)
print(np.diag(c))

## Indexing/slicing/boolean indexing ###
a = np.array([[2,3,4],[5,4,3],[9,8,1]])
b = a >5
print(b)
print(a[a<5])
a = np.array([1,2,3,4,5,6])
b = [ 2,3,4]
print(a[b])
even = np.argwhere(a%2==0).flatten()
print(a[even])
a = np.arange(1,7)
print(a)
print(a.shape)
b = a.reshape((2,3))
print(b)
b = a[:,np.newaxis]
print(b)
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.hstack((a,b))
print(c)
c = np.vstack((a,b))
print(c)

#----brodcasting-----#
a = np.array([[1,2,3],[34,1,0],[11,21,331],[100,3,99]])
b = np.array([2,21,9])
c = a + b
print(c)
a = np.array([1,2,3])
b = a.copy()
b[0]=7
print(a)
a = np.zeros((2,3)) # similarly for ones full eyes
print(a)
a = np.linspace(1,100,5)
print(a)
a = np.random.random((3,3))
print(a*100)
a = np.random.randn(1000)
print(a)
print(a.mean(), a.var())
a = np.random.randint(10,size =(3,3))
print(a)
a = np.random.choice(5,size = 10)
print(a)

data = np.genfromtxt('spambase.csv', delimiter=',',dtype=np.float32) # or np.loadtxt
print(data)
print(data.shape)

## Linar algebra ###
a = np.array([[1,3],[2,21]])
eigenvalues,eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors)
b = eigenvectors[:,0]*eigenvalues[0]
c = a@eigenvectors[:,0]
print(np.allclose(b,c))

#-----practise problem------#
a = np.array([[1,1],[1.5,4.0]])
b = np.array([2200,5050])
x = np.linalg.solve(a,b)  or x= np.linalg.inv(a)@b
print(x)
