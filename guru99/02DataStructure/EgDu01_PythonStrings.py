# Python Strings: Replace, Join, Split, Reverse, Uppercase & Lowercase
# https://www.guru99.com/learning-python-strings-replace-join-split-reverse.html

var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])

#Operator	Description	Example
#[]	Slice- it gives the letter from the given index	a[1] will give "u" from the word Guru as such ( 0=G, 1=u, 2=r and 3=u)
x="Guru"
print x[1]

#[ : ]	Range slice-it gives the characters from the given range	x [1:3] it will give "ur" from the word Guru. Remember it will not consider 0 which is G, it will consider word after that is ur.
#x="Guru"
print x[1:3]

#in	Membership-returns true if a letter exist in the given string	u is present in word Guru and hence it will give 1 (True)
x="Guru"
print "u" in x

#not in	Membership-returns true if a letter exist is not in the given string	l not present in word Guru and hence it will give 1
x="Guru"
print "l" not in x

#r/R	Raw string suppresses actual meaning of escape characters.	Print r'\n' prints \n and print R'/n' prints \n
print r'\n'
print R'/n'

#% - Used for string format	%r - It insert the canonical string representation of the object (i.e., repr(o)) %s- It insert the presentation string representation of the object (i.e., str(o)) %d- it will format a number for display	The output of this code will be "guru 99".
name = 'guru'
number = 99
print'%s %d' % (name,number)

# +	It concatenates 2 strings	It concatenate strings and gives the result
x="Guru"
y="99"
print x+y

# *	Repeat	It prints the character twice.
x="Guru"
y="99"
print x*2

#==========================================
print ("Some more examples")

x = "Hello World!"
print(x[:6])
print(x[0:6] + "Guru99")

#Python String replace() Method
#The method replace() returns a copy of the string in which the values of old string have been replaced with the new value.

oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
print(newstring)

# Changing upper and lower case strings
# In Python, you can even change the string to upper case or lower case.

string="python at guru99"
print(string.upper())

#Likewise, you can also do for other function as well like capitalize

string="python at guru99"
print(string.capitalize())

#You can also convert your string to lower case

string="PYTHON AT GURU99"
print(string.lower())

# Using "join" function for the string
# The join function is a more flexible way for concatenating string. With join function, you can add any character into the string.
#
# For example, if you want to add a colon (:) after every character in the string "Python" you can use the following code.

print(":".join("Python"))

# Reversing String
# By using the reverse function, you can reverse the string. For example, if we have string "12345" and then if you apply the code for the reverse function as shown below.

string="12345"
print(''.join(reversed(string)))

# Split Strings
# Split strings is another function that can be applied in Python let see for string "guru99 career guru99". First here we will split the string by using the command word.split and get the result.

word="guru99 career guru99"
print(word.split(' '))

#To understand this better we will see one more example of split, instead of space (' ') we will replace it with ('r') and it will split the string wherever 'r' is mentioned in the string

word="guru99 career guru99"
print(word.split('r'))

#Consider the following code

x = "Guru99"
x.replace("Guru99","Python")
print(x)
#will still return Guru99. This is because x.replace("Guru99","Python") returns a copy of X with replacements made

#You will need to use the following code to observe changes

x = "Guru99"
x = x.replace("Guru99","Python")
print(x)
