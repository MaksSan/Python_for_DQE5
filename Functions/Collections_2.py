from random import randint, choice
from string import ascii_lowercase


def rand_dict():
    create_dict = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]
    return create_dict


def searching_value():
    tempr_dict = {}
    for dictionary in rand_dict():
        for k, v in dictionary.items():
            tempr_dict.setdefault(k, []).append(v)
    return tempr_dict


def biggest_value():
    my_dict = {}
    for k, v in searching_value().items():
        if len(v) > 1:
            my_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
        else:
            my_dict[k] = v[0]
    return my_dict


try:
    biggest_value()
except IndexError:
    print(f'Index is out of range')

print(f'Random dictionary: {rand_dict()}')
print(f'Result: {biggest_value()}')


