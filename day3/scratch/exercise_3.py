"""
1. Create a function that has four parameters named var1, var2, var3, var4).

2. In the function print out each variable and indicate which variable it is.

3. Call the function using entirely positional arguments.

4. Call the function using entirely named arguments.

5. Call the function with var1 as a positional argument and var2 through var4 as named 
arguments.

6. Try to call the function with var1 specified first and using a named argument (and 
var2 through var4 as positional arguments, but specified after var1). This will generate 
an error.
"""


def my_variables(var1, var2, var3, var4):
    print(f"my variable_1 {var1}")
    print(var2)
    print(var3)
    print(var4)


print("objective 3:")
my_variables("ip_address", "model", "type", "variable4")
print("-" * 90)
print("objective 4:")
my_variables(var4="anything", var1="something", var2="no, 2", var3="number3")
print("-" * 90)
print("objective 5:")
my_variables(
    "this is var1", var4="this is var4", var2="not var3", var3="yes this is var3"
)
print("-" * 90)
print("objective 6:")
# my_variables(var1 = "variable 1 text", "variable 2", "variable_3", 'variable 4')
