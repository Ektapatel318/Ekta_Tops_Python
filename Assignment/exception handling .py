#Explain Exception handling? What is an Error in Python?
# exception which disturb the normal flow of program. Exception which is handled by try and except block it is called exception handling.
# error are problem that occurs in the program due to the illegal operation performed by the user or by the fault of a programmer , which is the normal flow of program


#How many except statements can a try-except block have? Name Some built-in exception classes: 
# ans: there has to be atleast one expect statement.
#for ex: ZeroDivisionError
#ValueError
#KeyError 
#IndexError
#TypeError etc.


# When will the else part of try-except-else be executed?
# ans: when no exception occurs.
#else:
    #without exception


# Can one block of except statements handle multiple exception? 
# yes 

## When is the finally block executed?
# it always executed whether exception occurs or not.
#finally:
    #it is always occurs


# What happens when „1‟== 1 is executed?
# it simply evaluate to false does not raise any ecxeption


# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets
# ans:
"""
try:
    exception code
except:
    statement
else:
    without exception
finally:
    it always occurs

"""
#example

try:
    a = 20
    b = 40
    ans = a+b
    print(ans)
except:
    print("invalid input")
else:
    print("welcome to math world")
finally:
    print("THANK YOU FOR USING THIS APPLICATON")

# Write python program that user to enter only odd numbers, else will raise an exception. 

while True:
    try:
        n = int(input("enter any odd number: "))
        if n%2 == 0:
            raise ValueError("Even number are not allowed !")
        break
    except ValueError as e:
        print(e)











