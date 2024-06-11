num=[12,23,34,67,49,87]

for i in num:
    if i%5==0:
        print(i)
        break
else:
    print("not found")