my_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#        0   1  2 3  4  5  6  7  8  9
#       -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# list[start:end:step] 
print (my_list[3:8])
print(my_list[-10:])
print(my_list[-3:-7])# here the slicin g always happens in the farward direction 
#to reverse printing 
print(my_list[-1:-8:-1])
print(my_list[-1:-8:-2])  
print(my_list[1:-1])
print(my_list[:])
print(my_list[:9])
print(my_list[2:-1:-1])# That’s impossible, because index 2 is before index 9 in the list.
print(my_list[::-1]) 
# reverse the url
sample='chatgpt.com'
print(sample[::-1]) 
#get the top level domain 
print(sample[-4: ])