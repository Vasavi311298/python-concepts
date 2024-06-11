from array import array

# Create an array of integers
arr = array('i', [1, 2, -3, 4, 5])
print(arr.buffer_info())
newarr=array(arr.typecode,(a*a for a in arr))
print(newarr)
newarr.reverse()
newarr.append(8)
print(newarr)
for num in arr:
    print(num)
