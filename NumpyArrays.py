
from numpy import  *

#Creating array using arange()
arr1 = arange(1, 20, 5)
for i in range(len(arr1)):
    if i == len(arr1):
        print('%.2f' %arr1[i], end="")
    else:
        print('%.2f' % arr1[i], end=", ")

#Creaing array using linspace()
arr2 = linspace(1, 10, 8)
for j in range(len(arr2)):
    if j == len(arr2):
        print('%.2f' %arr2[j], end="")
    else:
        print('%.2f' % arr2[j], end=", ")

#Creaing array using logspace()
arr3 = logspace(1, 10, 8)
for k in range(len(arr3)):
    if k == len(arr3):
        print('%.2f' %arr3[k], end="")
    else:
        print('%.2f' % arr3[k], end=", ")

#zeros()
zeroarray = zeros(5)
print(zeroarray)

#ones()
onearray = ones(5, int) #Converts all elements to ones in a list
print(onearray)

