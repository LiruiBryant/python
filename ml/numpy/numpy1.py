import numpy as np

world_alcohl = np.genfromtxt(
    'E:\\baiduyundownload\机器学习\\01.python数据分析与机器学习实战\\课程资料\\唐宇迪-机器学习课程资料\\Python库代码（4个）\\1-科学计算库numpy\\world_alcohol.txt',
    delimiter=",", dtype=str)
print(type(world_alcohl))
print(world_alcohl)
# print(help(np.genfromtxt))

vector = np.array([5, 10, 15, 20])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(vector)
print(matrix)

print(vector.shape)
print(matrix.shape)

number = np.array([1, 2, 3, 4.0])
number1 = np.array([1, 2, 3, 4.0])
print(number)
print(number.dtype)

print(world_alcohl)

uruguay_other_1986 = world_alcohl[1, 4]
third_coutry = world_alcohl[2, 2]
print(uruguay_other_1986)
print(third_coutry)

print(world_alcohl[:, 0:2])

print(number == 4)
print(number.dtype)

print(number == number1)

print(np.arange(15))

a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)

np.zeros((3, 4))

np.ones((2, 3, 5), dtype=np.int32)

np.arange(10, 150, 5)

np.random.random((2, 3))

np.linspace(0, 2 * np.pi, 100)

np.sin(np.linspace(0, 2 * np.pi, 100))

a = np.array([20, 30, 40, 50])

b = np.arange(4)

c = a - b
print(c)

c = c - 1
print(c)

print(b ** 2)

print(a < 35)

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])

print(A * B)

print(A.dot(B))

print(np.dot(A, B))

B = np.arange(3)

print(B)

print(np.exp(B))
print(np.sqrt(B))

a = np.floor(10 * np.random.random((3, 4)))

print(a)

print(a.ravel())

a.shape = (6, 2)
print(a)

print(a.T)

print(a.reshape((3, -1)))

a = np.floor(10 * np.random.random((2, 2)))
b = np.floor(10 * np.random.random((2, 2)))

print(a)

print(b)

print(np.hstack((a, b)))

print(np.vstack((a, b)))

a = np.floor(10 * np.random.random((2, 12)))

print(np.hsplit(a, 3))

print(np.vsplit(a, 1))

print(np.hsplit(a, (3, 4)))
