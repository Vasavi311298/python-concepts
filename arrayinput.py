from array import array

arr=array('i',[])
n=int(input("enter length of array"))

for i in range(n):
    x=int(input("entervalues int0 areay"))
    arr.append(x)
print(arr)

#to search the index of value
val=int(input("value to seach the index of "))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1
print(arr.index(val))
