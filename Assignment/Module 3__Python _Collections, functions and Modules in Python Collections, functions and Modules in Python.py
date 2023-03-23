"""
# program-8 : Write a Python program to check whether a list contains a sublist

list = ["Python",11,"tops","technology", 12,10,14,13]
s_list = ["Python","tops", 10,14]
result = []

print(list)
print(s_list)


for i in range(len(s_list)+1): 
    if s_list[i] in list:
        result = s_list[i]     

    else:
        
        print("not a sublist") 

print("yes it contain sublist",reslut)    


# program-9 : Write a Python program to find the second smallest number in a list.

def second_smallest(lst):
     smallest = min(lst)
     new_lst = [x for x in lst if x != smallest]
     second_smallest = min(new_lst)
     return second_smallest
my_list = [1,4,5,6,7,8,9,10]
second_min = second_smallest(my_list) 
print(second_min) 

# program-10 : Write a Python program to get unique values from a list.

def uniquel(lst):
    return list(set(lst))

my_list = [2,43,1,2,4,6,4,32,45,44,45,4,5,2]
print(uniquel(my_list))



# program-11 : Write a Python program to unzip a list of tuples into individual lists.

l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))

#program-12 : Write a Python program to convert a list of tuples into a dictionary

lst = [("x",1),("y",2),("x",5)]
d= {}
for a,b in lst:
    d.setdefault(a, []).append(b)
print(d)


#program-13: Write a Python program to sort a dictionary (ascending /descending) by value.
import operator
d ={2:4,4:6,1:5,5:1,0:0}
print("original dictionary",d)
a_dic = sorted(d.items(), 
             key = operator.itemgetter(1))

s_dic   = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))

print(a_dic)
print(s_dic)

"""






