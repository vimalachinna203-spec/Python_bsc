#positive slicing
#syntax str1[start:stop-1:step]
str1="welcome to nandyal"
print(str1)
#case1
print(str1[0:7])
#case2
print(str1[0:7:2])

#case3
#print(str1[0:7:0])

#case4
print(str1[0:7:-1])

#case5
print(str1[: :])

#case6
print(str1[5:3])

#Negative slicing
#case1
print(str1[-1:-8:-1])

#case2
print(str1[-1:-8:-2])

#case3
#print(str1[-1:-10:0]) 

#case4
print(str1[-4:-2:-1])

#case5
print(str1[: :-1])


