#marksheet
input("Enter your name: ")
input("Enter your Roll number: ")
s1=int(input("Enter marks of Chemistry: "))
s2=int(input("Enter marks for Biology: "))
s3=int(input("Enter marks for English: "))
s4=int(input("Enter marks for  Pak. Studies: "))
s5=int(input("Enter marks for Sindhi "))
TotalObtained=s1+s2+s3+s4+s5
print("Obtained Marks: ", TotalObtained)
Totalmarks=500
perc=(TotalObtained/Totalmarks)*100
print("Percentage is",perc) 
if perc>=90.0 :
    print("YOUR GRADE IS A+")
elif perc>=80.0 and perc<90 :
    print("YOUR GRADE IS A")
elif perc>=70.0 and perc<80.0   :
    print("YOUR GRADE IS B")
elif perc>=60.0 and perc<70.0   :
    print("YOUR GRADE IS C")
elif perc>=50.0 and perc<60.0   :
    print("YOUR GRADE IS D")
else   :
    print("YOU ARE FAIL! WORK HARD")




   
