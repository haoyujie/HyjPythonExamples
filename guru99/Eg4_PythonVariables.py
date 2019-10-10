# https://www.guru99.com/variables-in-python.html#1
# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)
print("======func2============")
# Global vs.local variables in functions
def someFunction2():
  global f
  print(f)
  f = "changing global variable"
someFunction2()
print(f)

print("======del============")

fwillbe_del = 11;
print(fwillbe_del)
del fwillbe_del
print(fwillbe_del)

