total=[]
b=int(input("How many grades would you like to calculate the average from? "))
for i in range(0,b):
    grade=float(input("Enter numerical grade without percentage symbol: "))
    total.append(grade)
avg=sum(total)/ b
print("Average of all grades is: ", round(avg, 1),"\nHighest number is: ", max(total), "\nLowest number is: ", min(total))
