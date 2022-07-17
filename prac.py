#operations on str obj
# 1)indexing
# 2)slicing
# ------1)indexing
# eg-1
from msilib import sequence


strob="chakri"
print(strob[5])
# ------>2)slicing
# syntax-1)(starting index :end index)
strob="chakri"
print(strob[0:5])
# syntax-2)(starting index :)
strob="chakri"
print(strob[0:])
# syntax-3)(:end index)
strob="chakri"
print(strob[:1])
# syntax-4)(:)
strob="chakri"
print(strob[:])
# syntax-5)(begin index:end index:step)
# cahkri
strob="chakri"
print(strob[:])
# print(s[0:6:2])
# print(s[::2])
# print(s[-6:-1:2])
# print(s[-6::2])
# print(s[-6:-1:2])
# print(s[0:5:-1])
# print(s[5:0:-1])
# print(s[0:9:-2])



#---------------type casting techniques in python
# the purpose of type casting tec is convert one type date vlaue into another type of value
#we have 5 type casting
# 1)int()
# 2)float()
# 3)str()
# 4)bool()
# 5)complex()
#-------- sequence data type
# 2)bytes
# b=[1,2,3,0,255]
# b1=bytes(b)
# print(b1,type(b1))
# 3)bytearray
# b=[1,2,3,0,255]
# b1=bytearray(b)
# print(b1,type(b1))
# 4)range
# r=range(0,5)
# print(r)
# r=range(0,5,2)
# r=range(0,9)
# print(r[3],type(r))

