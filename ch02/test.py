import numpy as np
a = np.array([1,2,3])
print(a)
print(np.zeros(2))
print(np.ones(3))
print(np.arange(4)) #０から並べる
print(np.arange(2, 9, 3)) #(start, finish(この値は含まない), space) >>> [2, 5, 8]
print(np.linspace(0, 10, num = 4)) #(開始, 終了, 要素) >>> 一定の間隔で作成

b = np.array([4, 5, 6])
c = np.concatenate((a, b))
print(c)
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])
print(np.concatenate((x, y), axis=0))
print(np.eye(3)) #単位行列
