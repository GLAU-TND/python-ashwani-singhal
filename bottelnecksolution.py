no_of_bottles = int(input("enter the number of bottles: "))
radius = list(map(int,input("enter the radius of bottles in 1 line: ").split()))

if len(radius) == no_of_bottles:
    print(max([radius.count(i) for i in radius]))
else:
    print("input is more than number of bottles")

#dp = [-1 for i in range(100)]
#print(dp)


#radius.sort()
#count1 = 1
#count2=1

#for i in range(no_of_bottles-1):
#    if radius[i] == radius[i+1]:
#        count1+=1
#    else:
#        if(count1>count2):
#            count2=count1
#        count1=1

#print(count2)