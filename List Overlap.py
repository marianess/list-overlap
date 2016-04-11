import random

def rand_list():
    return [random.randint(1,100) for x in range(1,11)]

def list_overlap(a, b):
    new_lst = []
    for item in a and b:
        if item in a and b:
            new_lst.append(item)
            return (new_lst)

a,b = rand_list(),rand_list()
print (a,b)

print (list_overlap(a, b))

#function rand_list creates two lists composed by random 10 randm nymbers from 1 to 10.
# function my_function returns a list that contains elements that are
#common between two random lists (without duplicates).
