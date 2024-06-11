
def length(lst):
    user_name=""
    max_lengt=0
    for i in lst:
        user_length=len(i)
        if user_length>len(user_name):
            max_lengt=len(i)
            user_name=i
    return user_name


user_input = input("Enter elements separated by spaces: ")
#lst=['vasu','vani','renukamma','shreenivasappa']
# Split the user input by spaces to get individual elements
lst = user_input.split()


user_name = length(lst)
print(user_name)
print("highest length user name: {} ".format(user_name))