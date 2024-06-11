
def count(lst):

    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

user_input = input("Enter elements separated by spaces: ")
#lst=[2,3,4,5,6,7]
# Split the user input by spaces to get individual elements
lst = user_input.split()

# Convert the elements to integers
lst = [int(element) for element in lst]
even, odd = count(lst)
print("even : {} and odd : {}".format(even,odd))








