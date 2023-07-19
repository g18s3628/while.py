#Assign the total of nd the count to a zero 
total_num = 0
count_num = 0

#Use while loop to request user to input number 
#If the loop is equal to the -1 then breakthe loop
while True:
    num = int(input("Enter a number:"))
    if num == -1:
        break

#The summation of the numbers inserted to find the total and the length of the numbers     
    total_num += num
    count_num += 1
  
#If the count of numbers is greater than zero then calculate the average and print out 
#If the count is zero then print there is no number requested 
if count_num > 0:
    ave = total_num / count_num
    print("The average for the numbers entered is:", ave)
else:
    print("No numbers have been entered")
