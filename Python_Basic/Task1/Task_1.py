from random import randint                                 #random library

#variables
data_list = []
new_list = []
sum_cht = 0
sum_ncht = 0
avg_cht = 0
avg_ncht = 0
count_cht = 0
count_ncht = 0

#creatint list of 100 random numbers from 0 to 1000
while len(data_list) < 100:                                 #perform until it reaches the list of 100
    rand_num = randint(0, 1000)                             #random numbers and range
    if rand_num not in data_list:                           #condition for writing random number
        data_list.append(rand_num)                          #writing random number.

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
    if i % 2 == 0:                                        #condition for finding even and odd numbers
        sum_cht += i                                        #summ of found even numbers
        count_cht += 1                                      #count of even numbers
    else:
        sum_ncht += i                                       #summ of found odd numbers
        count_ncht += 1                                     #count of odd numbers
avg_cht = sum_cht/count_cht                                 #calculating the average value for even numbers
avg_ncht = sum_ncht/count_ncht                              #calculating the average value for odd numbers

print("List of values: " + str(new_list))
print("Average value for even numbers: " + str(avg_cht))
print("Average value for odd numbers: " + str(avg_ncht))
