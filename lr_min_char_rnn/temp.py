import numpy as np


# a = np.array([1, 2, 3])
# # a1 = np.array([11, 12, 13])
# b = np.array([2, 3, 4])
# # b1 = np.array([12, 13, 14])
# c = np.array([3, 4, 5])
# # c1 = np.array([13, 14, 15])
#
# for i in range(2):
#
#     for param, dparam, mem in zip([a], [b], [c]):
#
#         a1 = np.copy(mem) ## should not use a1=mem
#         mem += dparam * dparam
#         print('>>> mem: ', a1, dparam, dparam * dparam, mem)
#         print(c)


# a = np.array([1, 2, 3])
# # a1 = np.array([11, 12, 13])
# b = np.array([2, 3, 4])
# # b1 = np.array([12, 13, 14])
# c = np.array([3, 4, 5])
# # c1 = np.array([13, 14, 15])
#
# # print(zip([a], [b], [c]))
#
# for i in range(2):
#
#     for param, dparam, mem in zip(a, b, c):
#
#
#         a1 = np.copy(mem) ## should not use a1=mem
#         mem += dparam * dparam
#         # print('>>> mem: ', a1, dparam, dparam * dparam, mem)
#         print('param, dparam, dparam: ', param, dparam, mem, a, b, c)
#         print(mem==c[0], )
#         print(c)


a = np.array([1, 2, 3])
b = a
b = b / 2
pass










# pass

# a = 1
# b = a
# b = 2
# print('>>>a: ', a)