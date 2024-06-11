import modules

a=10
b=20
c=modules.add(a,b)
print(c)
print("Demo says"+__name__)#special variable based on the place of usage ,it will print the output
#if you are refering another module to print then it will print hte module name , if using in the slef module then it will print __main__as the execution starts from main()
