"""
#program-1 : Program to sum of n positive integer.
sum = 0
no = int(input("enter the no : "))
for i in range(1,no+1):
    sum = sum + i
print("sum of entered no:",sum)




#program-2 : program to count occurance of substring in string.

s = input("Enter any string : ")
print(s)
o = input("ener a substring which you want to count the occurance : ")

print("no of occurance of ",o, " : ",s.count(o))




#program-3 : program to count the occurance of each word in a given sentence


s = "Module 2 : Python Fundamentals"

d = dict()
s1 = s.split(" ")

for i in s1:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
print(d)



#program-4 :  program to get a single string from two given strings, separated by a space and swap the first 
#two characters of each string.

s1 = input("Enter any string 1: ")
s2 = input("Enter any string 2: ")

s = s1.split()+s2.split()
print(s)

new_s1 = s2[:2] + s1[2:]
new_s2 = s1[:2] + s2[2:]

print(new_s1,new_s2)


#program-5 :  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
#If the given string already ends with 'ing' then add 'ly' instead If the string length of the given 
#string is less than 3, leave it unchanged

s = input("enter string : ")
l = len(s)

if l>2:
    print("befor : ",s)
    if s[-3:]=="ing":
        s += "ly"
    else:
        s += "ing"
    print("after : ",s)

else:
    print(s)




#program -6 :  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 
# 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
# Return the resulting string

s = input("enter a string : ")
sn = s.find("not")
sp = s.find("poor")

s = s.replace(s[sn:(sp+4)],"good")
print(s)


"""

#program - 7 : Program to find Greatest Common Divisor of two numbers.


n1 = int(input("enter no 1: "))
n2 = int(input("enter no 2: "))

if n1>n2:
    smaller = n2
else:
    smaller = n1

for i in range(1,(smaller+1)):
    if n1%i == 0 and n2%i == 0:
        GCD = i
print("GCD of ",n1,"and ",n2,"is ",GCD)
    



    
    













