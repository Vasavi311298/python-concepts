num=7
for i in range(2,num):#i will goo until 6 to check ,for 7 it will not check
    if num%i==0:
        print('not prime')
        break
else:
    print('its prime')