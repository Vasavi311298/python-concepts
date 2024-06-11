a=5
b=2

try:
    print("resource open")
    print(a/b)
    k = int(input("enter anumber"))
    print(k)

except ZeroDivisionError as e:
    print("cant devide by zero",e)

except ValueError as e:
    print("Invalid input",e)

except Exception as  e:
    print("Something went wrong")

finally:
    print("resource closed")

