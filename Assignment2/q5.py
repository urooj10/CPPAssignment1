#program to find the largest number in  a list
list1=[8,6,4,3,9,1,0,5,12,11,13,0,200,11]
temp=0
for i in list1:
    if(i>temp):
        temp=i
    else:
        continue

print("Largest number is ",temp)
