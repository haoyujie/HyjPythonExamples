# Python Dictionary(Dict): Update, Cmp, Len, Sort, Copy, Items, str Example
# https://www.guru99.com/python-dictionary-beginners-tutorial.html

# Python 2 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print (Dict['Tiffany'])


# Python 3 Example

# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print((Dict['Tiffany']))

#===============================================

# Python 3 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print(studentX)
print(studentY)

# Updating Dictionary
# You can also update a dictionary by adding a new entry or a key-value pair to an existing entry or by deleting an existing entry.
# Here in the example we will add another name "Sarah" to our existing dictionary.

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Dict.update({"Sarah":9})
print(Dict)

Dict.update({"Sarah":90})
print(Dict)

# Dictionary items() Method
# The items() method returns a list of tuple pairs (Keys, Value) in the dictionary.
#
# Python 2 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print "Students Name: %s" % Dict.items()

# python3
# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Students Name: %s" % list(Dict.items()))

# Check if a given key already exists in a dictionary
#
# For a given list, you can also check whether our child dictionary exists in a main dictionary or not. Here we have two sub-dictionaries "Boys" and "Girls", now we want to check whether our dictionary Boys exist in our main "Dict" or not. For that, we use the forloop method with else if method.
#
# Python 2 Example

# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Boys = {'Tim': 18,'Charlie':12,'Robert':25}
# Girls = {'Tiffany':22}
# for key in Dict.keys():
#     if key in Boys.keys():
#         print True
#     else:
#         print False
# Python 3 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:
        print(False)

# Sorting the Dictionary
# In the dictionary, you can also sort the elements. For example, if we want to print the name of the elements of our dictionary alphabetically we have to use the forloop. It will sort each element of dictionary accordingly.
#
# Python 2 Example

# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Boys = {'Tim': 18,'Charlie':12,'Robert':25}
# Girls = {'Tiffany':22}
# Students = Dict.keys()
# Students.sort()
# for S in Students:
#       print":".join((S,str(Dict[S])))
#
# Python 3 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
Students = list(Dict.keys())
print("Students====================")
print(Students)
Students.sort()
for S in Students:
      print(":".join((S,str(Dict[S]))))
#

# Python Dictionary in-built Functions
# Dictionary len() Method
# The len() function gives the number of pairs in the dictionary.

# Python 3 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("Length : %d" % len (Dict))
# When len (Dict) function is executed it gives the output at "4" as there are four elements in our dictionary

# Variable Types
# Python does not require to explicitly declare the reserve memory space; it happens automatically. The assign values to variable "=" equal sign are used. The code to determine the variable type is " %type (Dict)."


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("variable Type: %s" %type (Dict))
# Use the code %type to know the variable type
# When code was executed, it tells a variable type is a dictionary

# Dictionary Str(dict)
# With Str() method, you can make a dictionary into a printable string format.
#
# Python 3 Example

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("printable string:%s" % str (Dict))

# Here is the list of all Dictionary Methods
#
# Method	Description	Syntax
# copy()	Copy the entire dictionary to new dictionary	dict.copy()
# update()	Update a dictionary by adding a new entry or a key-value pair to an
# existing entry or by deleting an existing entry.	Dict.update([other])
# items()	Returns a list of tuple pairs (Keys, Value) in the dictionary.	dictionary.items()
# sort()	You can sort the elements	dictionary.sort()
# len()	Gives the number of pairs in the dictionary.	len(dict)
# cmp()	Compare values and keys of two dictionaries	cmp(dict1, dict2)
# Str()	Make a dictionary into a printable string format	Str(dict)