from random import randint                                 #random library

#variables
N = 100
data_list = []
new_list = []
sum_cht = 0
sum_ncht = 0
avg_cht = 0
avg_ncht = 0
count_cht = 0
count_ncht = 0

#creatint list of 100 random numbers from 0 to 1000
for i in range(N):
    data_list.append(randint(0, 1000))                      #writing random number.

#sort list from min to max
while data_list:                                            #execute while there is numbers in the list
    minimum = data_list[0]                                  #assign a variable the value of list with zero key
    for c in data_list:                                     #take the value from the list with zero key and then next keys
        if c < minimum:                                     #check the condition
            minimum = c                                     #writing a value to a variable
    new_list.append(minimum)                                #when minimal value is found writing this value to the new list
    data_list.remove(minimum)                               #found value is removed from the first list (data_list)

#calculating average for even and odd numbers

for i in new_list:                                          #take the value from the list with zero key and then next keys
    if i % 2 == 0:                                          #condition for finding even and odd numbers
        sum_cht += i                                        #summ of found even numbers
        count_cht += 1                                      #count of even numbers
    else:
        sum_ncht += i                                       #summ of found odd numbers
        count_ncht += 1                                     #count of odd numbers
try:                                                        #checking for error
    avg_cht = sum_cht/count_cht                             #calculating the average value for even numbers
    avg_ncht = sum_ncht/count_ncht                          #calculating the average value for odd numbers
except ZeroDivisionError:                                   #expected exception
    print("ERROR: Division by zero")                        #printing text error


print("List of values: " + str(new_list))                   #printing the list of values
print("Average value for even numbers: " + str(avg_cht))    #printing average value for even numbers
print("Average value for odd numbers: " + str(avg_ncht))    #printing average value for odd numbers
