#positive slicing
#syntax str1[start:stop-1:step]
str1="welcome to nandyal"
print(str1)
#case1
print(str1[0:7])


l2=[24,35,67,['abc',[12,56,78,['Ap'],90]],65,98,32,['N','L']]
print(l2[-3])
print(l2[-5][-1][-2])

l3=(l2[3][1][3])
l4=('').join(l3)
print(l4)