########TASK 1###########
try:
    a = input("Enter the name of the student:")
    marks_list={"Shridhar":70,"Shrish":77,"Prajwal":90,"virat":18,"Ganesh":90}
    print("{}'s Marks IS {}".format(a,marks_list[a]))
except:
    print("The student name not found")
finally:
    print("THANK YOU")


#############TASK 2#########
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[0:5]
print(list2)
list2.reverse()
print("The reversed list2 is:",list2)
