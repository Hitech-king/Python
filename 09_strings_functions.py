""" Strings are immutable. the in operation like
replace() , this function create oanther string and 
print it 
"""
string = "Hi there , how are you . hi hi hi"

# To fund the first index of given sub string in string 
index = string.find("hi")
print(index)

# To replace the all the occurance of given word
str1= "hi hi hi hi there"
print(str1)
str2 = str1.replace("hi","bye")
print (str2)
print("lenght of string:-",len(str1))
count = str1.count("h")
print(count)
print(str1.capitalize())
print(str2.title())

print(str1.find("there"))

