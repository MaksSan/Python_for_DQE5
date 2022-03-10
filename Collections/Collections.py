from random import randint, choice                                              #import random library
from string import ascii_lowercase                                              #import string library

#declaring variables
my_dict = {}
tempr_dict = {}

#creating random dictionaryy
rand_dict = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]

#searching all values for each one key
for dictionary in rand_dict:                                                    #take the key and value from the dict
    for k, v in dictionary.items():                                             #divide it into key and value
        tempr_dict.setdefault(k, []).append(v)                                  #assigning key values and adding

#searching the biggest values for key
try:                                                                            #checking for error
    for k, v in tempr_dict.items():                                             #take the key value from the dict
        if len(v) > 1:                                                          #condition for execution: if the number of values is more than one for key
            my_dict[k+"_"+str(v.index(max(v))+1)] = max(v)                      #searching the biggest value for key
        else:
            my_dict[k] = v[0]                                                   #assigns a value to a key with a zero key
except IndexError:                                                              #expected exception
    print(f'Index is out of range')                                             #printing text error

print(f'Random dictionary: {rand_dict}')                                        #printing the random dictionary
print(f'Result: {my_dict}')                                                     #printing the result



