
"""
Multiple Assignment
Python allows you to assign a single value to several variables simultaneously.

For example −

a = b = c = 1
Here, an integer object is created with the value 1, and all the three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example −

	a, b, c = 1, 2, "john"
Here, two integer objects with values 1 and 2 are assigned to the variables a and b respectively, and one string object with the value "john" is assigned to the variable c.

Standard Data Types
The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

Python has five standard data types −

Numbers
String
List
Tuple
Dictionary
Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them. For example −

var1 = 1
var2 = 10
You can also delete the reference to a number object by using the del statement. The syntax of the del statement is −

del var1[,var2[,var3[....,varN]]]]
You can delete a single object or multiple objects by using the del statement.

For example −

del var
del var_a, var_b
Python supports three different numerical types −

int (signed integers)
float (floating point real values)
complex (complex numbers)
All integers in Python3 are represented as long integers. Hence, there is no separate number type as long.

Examples
Here are some examples of numbers −

int	float	complex
10	0.0	3.14j
100	15.20	45.j
-786	-21.9	9.322e-36j
080	32.3+e18	.876j
-0490	-90.	-.6545+0J
-0x260	-32.54e100	3e+26J
0x69	70.2-E12	4.53e-7j
A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are real numbers and j is the imaginary unit."""

var1 = 1
var2 = 10
print(var1)
print(var2)
