import matplotlib.pyplot as plt 
import numpy as np 

# try creating own function:
def a_plus_b(a,b):
    c = a + b
    return c
sea=a_plus_b(1,2)

# simple use of numpy and matplotlib.pyplot
x = np.linspace(0,10,1000) 
y = np.sin(x**2) 
plt.plot(x,y)

# define dictionaries dict.keys(),dict.values()
dict1 = {'a':'Thing One', 'b': 'Thing Two', 'c':'Thing Three'}
dict2 = {'light':'10'}

# just an ordered collection of objects, doesnt have to all be str
list1 = ['apple','banana','tortilla'] #list=[], tuple=()
print(list1[1])
list2 = [1,5,20]
# combine 2 equal length lists into a dictionary (1=key,2=val)
dict3=dict(zip(list1,list2))

# make dictionary 3 keys into own list
d3key=list(dict3.keys())
# make dictionary 3 values into own list
d3val=list(dict3.values())
# ask for user input of dictionary keys
#item=input("shopping list?")
# print value associated with that key
#print(d3val[d3key.index(item)])
# in one line:
#print(list(dict3.keys())[list(dict3.values()).index(item)])

# practice for and if statements (dont forget the :)
for x in range(0,5):
    if x == 0:
        print(x)
    elif x >=3:
        print('Big x = ' + str(x))
    else:
        z=x

# practice while statement:
counter = 1
while counter < 10:
    print(counter)
    counter += 1 # same as counter = counter + 1


