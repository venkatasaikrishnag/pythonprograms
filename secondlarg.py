list1 = [1,2,5,10,20,6,50,100]
max_=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
for i in range(2,len(list1)):
    
    if list1[i]>max_:
        secondmax=max_
        max_=list1[i]
        
    else:
        if list1[i]>secondmax:
            secondmax=list1[i]
print("second largest number is the list is : ",str(secondmax))
