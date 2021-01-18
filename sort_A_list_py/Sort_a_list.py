## Sorting a list using bubble method

list=[]
nums=int(input("Enter the number of list elements : "))
for i in range(nums):
    val=int(input("Enter element %d : " %(i+1))) #enter list elements
    list.append(val)

i = 0
for i in range(nums):
    for j in range(nums):
        if(list[i] < list[j]):
            list[i],list[j]=list[j],list[i]
            
print(list)
