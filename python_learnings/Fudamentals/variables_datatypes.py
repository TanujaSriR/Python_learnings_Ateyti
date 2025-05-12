'''1.Variables & Data Types: Learn integers, floats, strings, booleans, and dynamic typing.'''
id=1
name='Tanuja Sri Ramnadham'
percentile=99.86
vegetarian=False
#  Sum of Two Numbers
def sum():
    a=int(input('enter the a value:'))
    b=int(input('enter the b value:'))
    return a+b
print(sum())
def convert_temp():
    celsius=int(input('enter the temp in celcius to convert to farenheit:'))
    return (celsius*9/5)+32
print(convert_temp())
def string_reverse():
    string=input('enter the string you want to reverse:')
    return string[::-1]
print(string_reverse())
def equality_checker(a,b):
    if a==b:
        return True
    else:
        return False
print(equality_checker(10,10))
# to return the which type of datatype we use
l=[1,2,3]
print(type(l))
# swap two numbers
def swap(a,b):
    return b,a
print(swap(1,2))
def str_int(s):
    return int(s)
def int_str(i):
    return str(i)
#DYNAMIC TYPING
#Store different types (int, float, string, bool) in a list and print their types.
def list_types(ls):
    return [type(i).__name__ for i in ls]
print(list_types([1,'tanu','sri',98.78,True]))
# done
