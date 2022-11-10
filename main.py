# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     VARIABLES, TYPES, INPUT
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#%% create and print variable
a = 1
print(a)


#%% how print works
print('value of a=', a)

#%% what are types
print('type of a=', type(a))

#%% what other types are there
a = 3.14
print('value of a=', a)
print('type of a=', type(a))

#%% let's get input from the user
a = input('insert value for a:')
print('value of a=', a)
print('type of a=', type(a))

#%% convert string to number
a = int(a)
print('value of a=', a)
print('type of a=', type(a))

#%% let's convert the str to a type we can parse
a = float(a)
print('value of a=', a)
print('type of a=', type(a))

#%%
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     CONDITIONS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


#%%
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     LISTS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#%% what about lists?
lst = [1, 2, 3, 4, 5, 6]
print('lst=', lst)
print('type of lst=', type(lst))


#%% what is the size of the list?

lst[0] = a
print(lst)
print('lst=', lst)
print('size of lst=', len(lst))

#%% can we add values to the list?

lst.append(42)
print(lst)

#%% how to remote? if we know a specific element, we can just
lst.remove(42)
print(lst)

#%% or we can remove the element on a particular index
lst.pop(0)
print(lst)



#%%
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     LOOPS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#%% how can we go through every value of a list? we can use cycles
for i in range(len(lst)):
    print(lst[i])

#%% we could also change the values of the list
print(lst)
for i in range(len(lst)):
    lst[i] = lst[i]*2
print(lst)





#%% what if we wanted to print each element of the list with 1 second delay?

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     EXTERNAL CODE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# we need to import outside modules
import time


for i in range(len(lst)):
    print(lst[i])
    time.sleep(1)

#%% let's also know when we printed each value
import datetime

for i in range(len(lst)):
    print(datetime.datetime.now(), lst[i])
    time.sleep(1)


#%%
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     FILES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#%% how to store data outside the program? we use files
with open('test.txt', 'w') as f:
    f.write('hello world!')

#%% how to read it?
with open('test.txt', 'r') as f:
    print(f.read())


#%% files: error when not writing str for text files
with open('test.txt', 'w') as f:
    f.write(lst)

#%% convert to string and write
with open('test.txt', 'w') as f:
    f.write(str(lst))


#%% read from file
with open('test.txt', 'r') as f:
    lst2 = f.read()

print(lst2)

#%% we have a string, so we need to parse the content, let's try to directly convert it to a list
lst2_ = list(lst2)
print(lst2_)

#%% didn't work so well, let's remove the square brackets

lst2_ = lst2[1:-1]
print(lst2_)
#%% now let's split the values
lst2_ = lst2[1:-1].split(',')
print(lst2_)

#%% now let's conver the strings to real numbers
lst3 = []
for i in range(len(lst2_)):
    val = float(lst2_[i])
    lst3.append(val)
print(lst3)


#%% write in a format that can be easily parsed after reading

for i in range(len(lst)):
    with open('test.txt', 'a') as f:
        f.write(str(lst[i]) + '\n')
# %%
